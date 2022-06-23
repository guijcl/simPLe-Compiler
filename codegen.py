def get_type(type):
    if type == "string":
        pass
    elif type in ["integer","int"]:
        return "i32"
    elif type == "float":
        return "float"
    elif type == "bool":
        return "i1"
    elif type == "array":
        pass
    elif type == "void":
        return "void"


class Emitter(object):
    def __init__(self):
        self.count = 0
        self.lines = []

    def get_count(self):
        self.count += 1
        return self.count

    def get_id(self):
        id = self.get_count()
        return f"cas_{id}"

    def __lshift__(self, v):
        self.lines.append(v)

    def get_code(self):
        return "\n".join(self.lines)

    def get_pointer_name(self, n):
        return f"pont_{n}"

def codegen(node, emitter=None):
    if type(node) is list:
        emitter = Emitter()
        for stmt in node:
            codegen(stmt, emitter)

        emitter << "define i32 @main() #0 {"

        #id_t = emitter.get_id()
        #emitter << f"%{id_t} = alloca i32, align 4"
        #emitter << f"store i32 1, i32* %{id_t}, align 4"
        #llvm::Value::getType()

        emitter << "   ret i32 0"
        emitter << "}"
        return emitter.get_code()
    elif node["nt"] == "var_defined":
        vname = node["identifier"]
        pname = emitter.get_pointer_name(vname)
        #emitter << f"{pname} = alloca i32, align 4"
        emitter << f"@{pname} = global i32 0, align 4"
    elif node["nt"] == "var_declared":
        vname = node["identifier"]
        expr = node["e"] 
        pname = emitter.get_pointer_name(vname)
        #emitter << f"{pname} = alloca i32, align 4"
        registo = codegen(expr, emitter)
        #emitter << f"store i32 {registo[0]}, i32* {pname}, align 4"
        emitter << f"@{pname} = global i32 {registo[0]}, align 4"
    elif node["nt"] == "function_declared":
        f_name = node["identifier"]
        f_type = get_type(node["type"])
        p_str = "("
        params = node["parameters"]
        for n in range(0, len(params)):
            if n == (len(params) - 1):
                p_str += get_type(params[n]["type"]) + "noundef, "
            else:
                p_str += get_type(params[n]["type"]) + "noundef)"
        emitter << f"declare {f_type} @{f_name}{p_str}"
    elif node["nt"] == "function_defined":
      pass
    elif node["nt"] in ["function_call", "function_call_inline"]:
      pass
    elif node["nt"] == "var_assignment":
        vname = node["identifier"]
        expr = node["e"] 
        pname = emitter.get_pointer_name(vname)
        emitter << f"{pname} = alloca i32, align 4"
        registo = codegen(expr, emitter)
        emitter << f"store i32 {registo}, i32* {pname}, align 4"
    elif node["nt"] == "if_else":
        cond = node["cond"]
        if_blocks = node["if"]["body"]
        else_blocks = node["else"]["body"]

        id_if_else = emitter.get_id()
        label_if_then = "if_then_" + id_if_else
        label_else_then = "else_then" + id_if_else
        label_fim = "if_else_fim_" + id_if

        '''rcomp = "%" + emitter.get_id()
        rcond = codegen(cond, emitter)
        emitter << f"{rcomp} = {rcond}"
        emitter << f"br i1 {rcomp}, label %{label_if_then}, label %{label_else_then}"'''
        decision = codegen(cond, emitter)
        if decision in ["label_progress", "label_skip"]:
            if decision == "label_progress":
                emitter << f"br label %{label_if_then}"
            else:
                emitter << f"br label %{label_else_then}"
        else:
            emitter << f"br i1 {decision}, label %{label_if_then}, label %{label_else_then}"

        emitter << f"{label_if_then}:"
        for b in blocks:
            codegen(b, emitter)
        emitter << f"br label %{label_fim}"
        emitter << f"{label_else_then}:"
        for b in blocks:
            codegen(b, emitter)
        emitter << f"{label_fim}:"
        return
    elif node["nt"] == "if":
        cond = node["cond"]
        blocks = node["body"]

        id_if = emitter.get_id()
        label_then = "if_then_" + id_if
        label_fim = "if_fim_" + id_if

        '''rcomp = "%" + emitter.get_id()
        rcond = codegen(cond, emitter)
        emitter << f"{rcomp} = {rcond}"
        emitter << f"br i1 {rcomp}, label %{label_then}, label %{label_fim}"'''
        decision = codegen(cond, emitter)
        if decision in ["label_progress", "label_skip"]:
            if decision == "label_progress":
                emitter << f"br label %{label_then}"
            else:
                emitter << f"br label %{label_fim}"
        else:
            emitter << f"br i1 {decision}, label %{label_then}, label %{label_fim}"

        emitter << f"{label_then}:"
        for b in blocks:
            codegen(b, emitter)
        emitter << f"{label_fim}:"
        return
    elif node["nt"] == "while":
        blocks = node["body"]
        cond = node["cond"]

        id_while = emitter.get_id()
        label_inicio = "while_inicio_" + id_while
        label_body = "while_body_" + id_while
        label_fim = "while_fim_" + id_while

        '''rcomp = "%" + emitter.get_id()
        rcond = codegen(cond, emitter)
        emitter << f"{rcomp} = {rcond}"
        emitter << f"br label %{label_inicio}"
        emitter << f"{label_inicio}:"
        emitter << f"br i1 {rcomp}, label %{label_body}, label %{label_fim}"'''

        emitter << f"br label %{label_inicio}"
        emitter << f"{label_inicio}:"
        decision = codegen(cond, emitter)
        if decision in ["label_progress", "label_skip"]:
            if decision == "label_progress":
                emitter << f"br label %{label_body}"
            else:
                emitter << f"br label %{label_fim}"
        else:
            emitter << f"br i1 {decision}, label %{label_body}, label %{label_fim}"

        emitter << f"{label_body}:"
        for b in blocks:
            codegen(b, emitter)
        emitter << f"br label %{label_inicio}"
        emitter << f"{label_fim}:"
        return
    elif node["nt"] == "return":
        elem = codegen(node["ret_e"], emitter)[0]
        t = get_type(elem[1])
        emitter << f"ret {t} {elem}"
    elif node["nt"] == "not":
        pass
    elif node["nt"] == "expr":
        vt1 = codegen(node["left"], emitter)
        vt2 = codegen(node["right"], emitter)

        if "sign" in node:
            vt_s = node["sign"]
        if "and_or" in node:
            vt_s = node["and_or"]

        if vt_s == '&&':
            # ===== vt1 =====
            if vt1 not in ["label_progress", "label_skip"]:
                emitter << f"{vt1}"

            id_and = emitter.get_id()
            label_and = "and_next" + id_and
            label_skip = "and_skip" + id_and
            label_return = "and_return" + id_and

            if vt1 not in ["label_progress", "label_skip"]:
                emitter << f"br i1 {vt1}, label %{label_and}, label %{label_skip}"
            else:
                if vt1 == "label_progress":
                    b = 1
                else:
                    b = 0
                emitter << f"br i1 {b}, label %{label_and}, label %{label_skip}"
            emitter << f"{label_and}:"

            # ===== vt2 =====
            if vt2 not in ["label_progress", "label_skip"]:
                emitter << f"{vt2}"
            
            if vt2 not in ["label_progress", "label_skip"]:
                emitter << f"br i1 {vt2}, label %{label_return}, label %{label_skip}"
            else:
                if vt2 == "label_progress":
                    b = 1
                else:
                    b = 0
                emitter << f"br i1 {b}, label %{label_return}, label %{label_skip}"

            emitter << f"{label_return}:"
            return "label_progress"

            emitter << f"{label_skip}:"
            return "label_skip"

        elif vt_s == '||':
            # ===== vt1 =====
            if vt1 not in ["label_progress", "label_skip"]:
                emitter << f"{vt1}"

            id_and = emitter.get_id()
            label_and = "and_next" + id_and
            label_skip = "and_skip" + id_and
            label_return = "and_return" + id_and

            if vt1 not in ["label_progress", "label_skip"]:
                emitter << f"br i1 {vt1}, label %{label_skip}, label %{label_and}"
            else:
                if vt1 == "label_progress":
                    b = 1
                else:
                    b = 0
                emitter << f"br i1 {b}, label %{label_skip}, label %{label_and}"
            emitter << f"{label_and}:"

            # ===== vt2 =====
            if vt2 not in ["label_progress", "label_skip"]:
                emitter << f"{vt2}"
            
            if vt2 not in ["label_progress", "label_skip"]:
                emitter << f"br i1 {vt2}, label %{label_return}, label %{label_skip}"
            else:
                if vt2 == "label_progress":
                    b = 1
                else:
                    b = 0
                emitter << f"br i1 {b}, label %{label_return}, label %{label_skip}"

            emitter << f"{label_return}:"
            return "label_progress"

            emitter << f"{label_skip}:"
            return "label_skip"

        elif vt_s == '+':
            v_t = get_type(vt1[1])
            rcomp = "%" + emitter.get_id()
            if v_t == "float":
                return "%{rcomp} = fadd {v_t} {vt1}, {vt2}"
            return "%{rcomp} = add {v_t} {vt1}, {vt2}"

        elif vt_s == '-':
            v_t = get_type(vt1[1])
            rcomp = "%" + emitter.get_id()
            if v_t == "float":
                return "%{rcomp} = fsub {v_t} {vt1}, {vt2}"
            return "%{rcomp} = sub {v_t} {vt1}, {vt2}"

        elif vt_s == '*':
            v_t = get_type(vt1[1])
            rcomp = "%" + emitter.get_id()
            if v_t == "float":
                return "%{rcomp} = fmul {v_t} {vt1}, {vt2}"
            return "%{rcomp} = mul {v_t} {vt1}, {vt2}"

        elif vt_s == '/':
            v_t = get_type(vt1[1])
            rcomp = "%" + emitter.get_id()
            if v_t == "float":
                return "%{rcomp} = fdiv {v_t} {vt1}, {vt2}"
            return "%{rcomp} = sdiv {v_t} {vt1}, {vt2}"

        elif vt_s == '%':
            v_t = get_type(vt1[1])
            rcomp = "%" + emitter.get_id()
            return "%{rcomp} = srem {v_t} {vt1}, {vt2}"

        elif vt_s == '==':
            v_t = get_type(vt1[1])
            rcomp = "%" + emitter.get_id()
            return "%{rcomp} = icmp eq {v_t} {vt1}, {vt2}"

        elif vt_s == '<=':
            v_t = get_type(vt1[1])
            rcomp = "%" + emitter.get_id()
            return "%{rcomp} = icmp sle {v_t} {vt1}, {vt2}"

        elif vt_s == '>=':
            v_t = get_type(vt1[1])
            rcomp = "%" + emitter.get_id()
            return "%{rcomp} = icmp sge {v_t} {vt1}, {vt2}"

        elif vt_s == '>':
            v_t = get_type(vt1[1])
            rcomp = "%" + emitter.get_id()
            return "%{rcomp} = icmp sgt {v_t} {vt1}, {vt2}"

        elif vt_s == '<':
            v_t = get_type(vt1[1])
            rcomp = "%" + emitter.get_id()
            return "%{rcomp} = icmp slt {v_t} {vt1}, {vt2}"

        elif vt_s == '!=':
            v_t = get_type(vt1[1])
            rcomp = "%" + emitter.get_id()
            return "%{rcomp} = icmp ne {v_t} {vt1}, {vt2}"

        return
    elif node["nt"] == "expr_e":
        elem = node["e"]
        if "nt" not in elem:
            if "identifier" in elem:
                identifier_id = "%" + emitter.get_id()
                pname = emitter.get_pointer_name(elem["identifier"])
                #emitter << f"{identifier_id} = load type"
                return identifier_id
            elif "integer" in elem:
                return (elem["integer"], "integer")
            elif "string" in elem:
                return (elem["string"], "string")
            elif "float" in elem:
                return (elem["float"], "float")
            elif "bool" in elem:
                res = elem["bool"]
                if res:
                    return ("1", "bool")
                return ("0", "bool")
            elif "array" in elem:
                return ("array", check(ctx, elem["array"]))
    else:
        pass