RETURN_CODE = "$ret"

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

class Context(object):
    def __init__(self):
        self.stack = [{}]
    
    def get_type(self, name):
        for scope in self.stack:
            if name in scope:
                return scope[name]
        return ""
    
    def set_type(self, name, value):
        scope = self.stack[0]
        scope[name] = value

    def has_var(self, name):
        for scope in self.stack:
            if name in scope:
                return True
        return False

    def has_var_in_current_scope(self, name):
        return name in self.stack[0]

    def enter_scope(self):
        self.stack.insert(0, {})

    def exit_scope(self):
        self.stack.pop(0)

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

def codegen(node, ctx:Context, emitter=None):
    if type(node) is list:
        emitter = Emitter()
        for stmt in node:
            codegen(stmt, ctx, emitter)

        emitter << "define i32 @main() #0 {"
        emitter << "   ret i32 0"
        emitter << "}"

        return emitter.get_code()
    elif node["nt"] == "var_defined":
        vname = node["identifier"]
        pname = "@" + emitter.get_pointer_name(vname)
        v_t = get_type(node["type"])
        emitter << f"{pname} = global {v_t} 0, align 4"

        if "value_types" in node: #array
            ctx.set_type(pname, array_type(node)) #array (corrigir)
        else:
            ctx.set_type(pname, v_t)
    elif node["nt"] == "var_declared":
        vname = node["identifier"]
        expr = node["e"]
        v_t = get_type(node["type"])
        pname = "@" + emitter.get_pointer_name(vname)
        registo = codegen(expr, ctx, emitter)
        emitter << f"{pname} = global {v_t} {registo[0]}, align 4"

        ctx.set_type(pname, v_t)
    elif node["nt"] == "function_declared":
        f_name = node["identifier"]
        f_type = get_type(node["type"])
        assinatura = ()
        if "parameters" in node:
            assinatura = (node["type"], [node["type"] for par in node["parameters"]])
        else:
            assinatura = f_type
        ctx.set_type(f_name, assinatura)

        ctx.enter_scope()
        ctx.set_type(RETURN_CODE, node["type"])
        p_str = "("
        if "parameters" in node:
            params = node["parameters"]
            for n in range(0, len(params)):
                if n != (len(params) - 1):
                    p_str += get_type(params[n]["type"]) + ", "
                else:
                    p_str += get_type(params[n]["type"])
                ctx.set_type(params[n]["type"])
        p_str += ")"
                
        ctx.exit_scope()
        emitter << f"declare {f_type} @{f_name}{p_str}"
    elif node["nt"] == "function_defined":
        f_name = node["identifier"]
        f_type = get_type(node["type"])
        assinatura = ()
        if "parameters" in node:
            assinatura = (node["type"], [node["type"] for par in node["parameters"]])
        else:
            assinatura = f_type
        ctx.set_type(f_name, assinatura)

        ctx.enter_scope()
        ctx.set_type(RETURN_CODE, (None, get_type(node["type"])))
        p_str = "("
        if "parameters" in node:
            params = node["parameters"]
            for n in range(0, len(params)):
                pname = "%" + emitter.get_pointer_name(params[n]["identifier"])
                if n != (len(params) - 1):
                    p_str += get_type(params[n]["type"]) + f" {pname}, "
                else:
                    p_str += get_type(params[n]["type"]) + f" {pname}"
                ctx.set_type(pname, get_type(params[n]["type"]))
            p_str += ")"
        ctx.enter_scope()
        emitter << "define %s @%s%s {" % (f_type, f_name, p_str)
        for elem in node["body"]:
            codegen(elem, ctx, emitter)
        emitter << "}"
        ctx.exit_scope()
        ctx.exit_scope()
    elif node["nt"] == "function_call":
        pname = node["identifier"]
        e = ctx.get_type(node["identifier"])
        if type(e) != tuple:
            ftype = e[0]
            id_call = emitter.get_id()
            call_str = f"%{id_call} = call {get_type(ftype)} @{pname} ()"
        else:
            (ftype, parameter_types) = e
            id_call = emitter.get_id()
            call_str = f"%{id_call} = call {get_type(ftype)} @{pname} ("
            for (i, (arg, par_t)) in enumerate(zip(node["parameters"], parameter_types)):
                call_str += f"{get_type(par_t)} {codegen(arg, ctx, emitter)[0]}, "
            call_str = call_str[:-2]
            call_str += f")"
        emitter << call_str
        return ("%" + id_call, get_type(ftype))

    elif node["nt"] == "array_call":
        return

    elif node["nt"] == "var_assignment":
        vname = node["identifier"]
        expr = node["e"] 
        pname = emitter.get_pointer_name(vname)
        emitter << f"{pname} = alloca i32, align 4"
        registo = codegen(expr, ctx, emitter)
        emitter << f"store i32 {registo}, i32* {pname}, align 4"
        ctx.set_type(name, node["type"])

    elif node["nt"] == "array_assignment":
        return

    elif node["nt"] == "if_else":
        cond = node["cond"]
        if_blocks = node["if"]["body"]
        else_blocks = node["else"]["body"]

        id_if_else = emitter.get_id()
        label_if_then = "if_then_" + id_if_else
        label_else_then = "else_then" + id_if_else
        label_fim = "if_else_fim_" + id_if_else

        decision = codegen(cond, ctx, emitter)[0]
        emitter << f"br i1 {decision}, label %{label_if_then}, label %{label_else_then}"

        emitter << f"{label_if_then}:"
        ctx.enter_scope()
        for b in if_blocks:
            codegen(b, ctx, emitter)
        emitter << f"br label %{label_fim}"
        emitter << f"{label_else_then}:"
        ctx.enter_scope()
        for b in else_blocks:
            codegen(b, ctx, emitter)
        emitter << f"{label_fim}:"
        ctx.exit_scope()
        return
    elif node["nt"] == "if":
        cond = node["cond"]
        blocks = node["body"]

        id_if = emitter.get_id()
        label_then = "if_then_" + id_if
        label_fim = "if_fim_" + id_if

        decision = codegen(cond, ctx, emitter)[0]
        emitter << f"br i1 {decision}, label %{label_then}, label %{label_fim}"

        emitter << f"{label_then}:"
        ctx.enter_scope()
        for b in blocks:
            codegen(b, ctx, emitter)
        ctx.exit_scope()
        emitter << f"{label_fim}:"
        return
    elif node["nt"] == "while":
        blocks = node["body"]
        cond = node["cond"]

        id_while = emitter.get_id()
        label_inicio = "while_inicio_" + id_while
        label_body = "while_body_" + id_while
        label_fim = "while_fim_" + id_while

        emitter << f"br label %{label_inicio}"
        emitter << f"{label_inicio}:"
        decision = codegen(cond, ctx, emitter)[0]
        emitter << f"br i1 {decision}, label %{label_body}, label %{label_fim}"

        emitter << f"{label_body}:"
        ctx.enter_scope()
        for b in blocks:
            codegen(b, ctx, emitter)
        ctx.exit_scope()
        emitter << f"br label %{label_inicio}"
        emitter << f"{label_fim}:"
        return
    elif node["nt"] == "return":
        elem = codegen(node["ret_e"], ctx, emitter)
        t = elem[1]
        emitter << f"ret {t} {elem[0]}"
    elif node["nt"] == "not":
        return

    elif node["nt"] == "expr":
        vt1 = codegen(node["left"], ctx, emitter)
        vt2 = codegen(node["right"], ctx, emitter)

        if "sign" in node:
            vt_s = node["sign"]
        if "and_or" in node:
            vt_s = node["and_or"]

        if vt_s == '&&':
            v_t = vt1[1]
            rcomp = emitter.get_id()
            emitter << f"%{rcomp} = and i1 {vt1[0]}, {vt2[0]}"
            return ("%" + rcomp, v_t)

        elif vt_s == '||':
            v_t = vt1[1]
            rcomp = emitter.get_id()
            emitter << f"%{rcomp} = or i1 {vt1[0]}, {vt2[0]}"
            return ("%" + rcomp, v_t)

        elif vt_s == '+':
            v_t = vt1[1]
            rcomp = emitter.get_id()
            if v_t == "float":
                emitter << f"%{rcomp} = fadd {v_t} {vt1[0]}, {vt2[0]}"
                return ("%" + rcomp, v_t)
            emitter << f"%{rcomp} = add {v_t} {vt1[0]}, {vt2[0]}"
            return ("%" + rcomp, v_t)

        elif vt_s == '-':
            v_t = vt1[1]
            rcomp = emitter.get_id()
            if v_t == "float":
                emitter << f"%{rcomp} = fsub {v_t} {vt1[0]}, {vt2[0]}"
                return ("%" + rcomp, v_t)
            emitter << f"%{rcomp} = sub {v_t} {vt1[0]}, {vt2[0]}"
            return ("%" + rcomp, v_t)

        elif vt_s == '*':
            v_t = vt1[1]
            rcomp = emitter.get_id()
            if v_t == "float":
                emitter << f"%{rcomp} = fmul {v_t} {vt1[0]}, {vt2[0]}"
                return ("%" + rcomp, v_t)
            emitter << f"%{rcomp} = mul {v_t} {vt1[0]}, {vt2[0]}"
            return ("%" + rcomp, v_t)

        elif vt_s == '/':
            v_t = vt1[1]
            rcomp = emitter.get_id()
            if v_t == "float":
                emitter << f"%{rcomp} = fdiv {v_t} {vt1[0]}, {vt2[0]}"
                return ("%" + rcomp, v_t)
            emitter << f"%{rcomp} = sdiv {v_t} {vt1[0]}, {vt2[0]}"
            return ("%" + rcomp, v_t)

        elif vt_s == '%':
            v_t = vt1[1]
            rcomp = emitter.get_id()
            emitter << f"%{rcomp} = srem {v_t} {vt1[0]}, {vt2[0]}"
            return ("%" + rcomp, v_t)

        elif vt_s == '==':
            v_t = vt1[1]
            rcomp = emitter.get_id()
            emitter << f"%{rcomp} = icmp eq {v_t} {vt1[0]}, {vt2[0]}"
            return ("%" + rcomp, v_t)

        elif vt_s == '<=':
            v_t = vt1[1]
            rcomp = emitter.get_id()
            emitter << f"%{rcomp} = icmp sle {v_t} {vt1[0]}, {vt2[0]}"
            return ("%" + rcomp, v_t)

        elif vt_s == '>=':
            v_t = vt1[1]
            rcomp = emitter.get_id()
            emitter << f"%{rcomp} = icmp sge {v_t} {vt1[0]}, {vt2[0]}"
            return ("%" + rcomp, v_t)

        elif vt_s == '>':
            v_t = vt1[1]
            rcomp = emitter.get_id()
            emitter << f"%{rcomp} = icmp sgt {v_t} {vt1[0]}, {vt2[0]}"
            return ("%" + rcomp, v_t)

        elif vt_s == '<':
            v_t = vt1[1]
            rcomp = emitter.get_id()
            emitter << f"%{rcomp} = icmp slt {v_t} {vt1[0]}, {vt2[0]}"
            return ("%" + rcomp, v_t)

        elif vt_s == '!=':
            v_t = vt1[1]
            rcomp = emitter.get_id()
            emitter << f"%{rcomp} = icmp ne {v_t} {vt1[0]}, {vt2[0]}"
            return ("%" + rcomp, v_t)
        return

    elif node["nt"] == "expr_e":
        elem = node["e"]
        if "nt" not in elem:
            if "identifier" in elem:
                pname = emitter.get_pointer_name(elem["identifier"])
                if ctx.get_type("@" + pname) != "":
                    tmpname = pname
                    pname = "@" + pname
                    ptype = ctx.get_type(pname)
                    id_global = emitter.get_id()
                    emitter << f"%{id_global} = load {ptype},  {ptype}* @{tmpname}"
                    return ("%" + id_global, ptype)
                pname = "%" + pname
                return (pname, ctx.get_type(pname))
            elif "integer" in elem:
                return (elem["integer"], get_type("integer"))
            elif "string" in elem:
                return (elem["string"], get_type("string"))
            elif "float" in elem:
                return (elem["float"], get_type("float"))
            elif "bool" in elem:
                res = elem["bool"]
                if res == "true":
                    return ("1", get_type("bool"))
                return ("0", get_type("bool"))
            elif "array" in elem:
                return ("array", codegen(elem["array"], ctx))
        else:
            return codegen(elem, ctx, emitter)
    else:
        pass