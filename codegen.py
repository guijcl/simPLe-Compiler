RETURN_CODE = "$ret"

def get_type(type):
    if type == "string":
        return "i8*"
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

def llvm_string(emitter, string):
    str_name = f"@.casual_str_" + emitter.get_id()
    str_decl = f"""{str_name} = private unnamed_addr constant [{len(string) + 1} x i8] c"{string}\\00", align 1"""
    emitter.lines.insert(0, str_decl)

    return f"i8* getelementptr inbounds ([{len(string) + 1} x i8], [{len(string) + 1} x i8]* {str_name}, i64 0, i64 0)"

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

        return emitter.get_code()
    elif node["nt"] == "var_defined":
        vname = node["identifier"]
        pname = "@" + emitter.get_pointer_name(vname)
        v_t = get_type(node["type"])
        if v_t == 'i8*':
            emitter << f"{pname} = global {v_t} null, align 8"
        elif v_t == "float":
            emitter << f"{pname} = global {v_t} 0.0, align 4"
        else:
            emitter << f"{pname} = global {v_t} 0, align 4"

        ctx.set_type(pname, v_t)
    elif node["nt"] == "var_declared":
        vname = node["identifier"]
        expr = node["e"]
        v_t = get_type(node["type"])
        pname = emitter.get_pointer_name(vname)
        registo = codegen(expr, ctx, emitter)
        if registo[1] == "i8*":
            str_v = registo[0]
            str_name = f"@.casual_str_{pname}"
            str_decl = f"""{str_name} = private unnamed_addr constant [{len(str_v) + 1} x i8] c"{str_v}\\00", align 1"""
            emitter.lines.insert(0, str_decl)

            n_var = "@" + pname
            emitter << f"{n_var} = global {v_t} getelementptr inbounds ([{len(str_v) + 1} x i8], [{len(str_v) + 1} x i8]* {str_name}, i32 0, i32 0)"
            ctx.set_type(n_var, v_t)
        else:
            emitter << f"@{pname} = global {v_t} {registo[0]}, align 4"
            ctx.set_type("@" + pname, v_t)

    elif node["nt"] == "local_var_declared":
        vname = node["identifier"]
        expr = node["e"]
        v_t = get_type(node["type"])
        pname = emitter.get_pointer_name(vname)
        registo = codegen(expr, ctx, emitter)
        if registo[1] == "i8*":
            str_v = registo[0]
            str_name = f"@.casual_str_{pname}"
            str_decl = f"""{str_name} = private unnamed_addr constant [{len(str_v) + 1} x i8] c"{str_v}\\00", align 1"""
            emitter.lines.insert(0, str_decl)

            emitter << f"%{pname} = alloca {v_t}"
            emitter << f"store {v_t} getelementptr inbounds ([{len(str_v) + 1} x i8], [{len(str_v) + 1} x i8]* {str_name}, i64 0, i64 0), {v_t}* %{pname}"
            v_t += "*"
        else:
            if not ctx.has_var("%" + vname):
                emitter << f"%{pname} = alloca {v_t}"

            emitter << f"store {v_t} {registo[0]}, {v_t}* %{pname}, align 4"  
        ctx.set_type("%" + pname, v_t)

    elif node["nt"] == "function_declared":
        f_name = node["identifier"]
        f_type = get_type(node["type"])
        assinatura = ()
        if "parameters" in node:
            assinatura = (node["type"], [par["type"] for par in node["parameters"]])
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
                ctx.set_type(None, params[n]["type"])
        p_str += ")"
                
        ctx.exit_scope()
        emitter << f"declare {f_type} @{f_name}{p_str}"
    elif node["nt"] == "function_defined":
        f_name = node["identifier"]
        f_type = get_type(node["type"])
        assinatura = ()
        if "parameters" in node:
            assinatura = (node["type"], [par["type"] for par in node["parameters"]])
        else:
            assinatura = f_type
        ctx.set_type(f_name, assinatura)

        ctx.enter_scope()
        ctx.set_type(RETURN_CODE, (None, get_type(node["type"])))
        p_str = "("
        param_tuples = []
        if "parameters" in node:
            params = node["parameters"]
            for n in range(0, len(params)):
                pname = "%" + emitter.get_id()
                param_tuples.append(((params[n]["identifier"], params[n]["type"]), pname))
                if n != (len(params) - 1):
                    p_str += get_type(params[n]["type"]) + f" {pname}, "
                else:
                    p_str += get_type(params[n]["type"]) + f" {pname}"
                ctx.set_type(pname, get_type(params[n]["type"]))
        p_str += ")"
        ctx.enter_scope()
        emitter << "define %s @%s%s {" % (f_type, f_name, p_str)

        for e in param_tuples:
            pname = "%" + emitter.get_pointer_name(e[0][0])
            ptype = get_type(e[0][1])
            emitter << f"{pname} = alloca {ptype}"
            emitter << f"store {ptype} {e[1]}, {ptype}* {pname}, align 4"
            ctx.set_type(pname, ptype)

        if node["body"] != [None]:
            for elem in node["body"]:
                codegen(elem, ctx, emitter)

        if node["type"] == "void":
            emitter << "ret void"

        emitter << "}"
        ctx.exit_scope()
        ctx.exit_scope()
    elif node["nt"] == "function_call":
        pname = node["identifier"]
        e = ctx.get_type(node["identifier"])
        if type(e) != tuple:
            ftype = e
            id_call = emitter.get_id()
            if ftype == "void":
                call_str = f"call {ftype} @{pname}()"
            else:
                call_str = f"%{id_call} = call {ftype} @{pname}()"
        else:
            (ftype, parameter_types) = e
            ftype = get_type(ftype)
            id_call = emitter.get_id()
            if ftype == "void":
                call_str = f"call {ftype} @{pname} ("
            else:
                call_str = f"%{id_call} = call {ftype} @{pname} ("
            for (i, (arg, par_t)) in enumerate(zip(node["parameters"], parameter_types)):
                elem = codegen(arg, ctx, emitter)
                if elem[1] == "i8*":
                    call_str += f"{llvm_string(emitter, elem[0])}, "
                else:
                    call_str += f"{get_type(par_t)} {elem[0]}, "
            call_str = call_str[:-2]
            call_str += f")"
        emitter << call_str
        return ("%" + id_call, ftype)

    elif node["nt"] == "array_call":
        return

    elif node["nt"] == "var_assignment":
        vname = node["identifier"]
        expr = node["e"]
        pname = emitter.get_pointer_name(vname)
        registo = codegen(expr, ctx, emitter)
        if registo[1] == "i8*":
            v_t = ctx.get_type("@" + pname)
            str_v = registo[0]
            str_name = f"@.casual_str_{pname}_{emitter.get_id()}"
            str_decl = f"""{str_name} = private unnamed_addr constant [{len(str_v) + 1} x i8] c"{str_v}\\00", align 1"""
            emitter.lines.insert(0, str_decl)

            n_var = "@" + pname
            emitter << f"store {v_t} getelementptr inbounds ([{len(str_v) + 1} x i8], [{len(str_v) + 1} x i8]* {str_name}, i64 0, i64 0), {v_t}* {n_var}"
        else:
            if ctx.has_var("%" + pname):
                vname = "%" + pname
            elif ctx.has_var("@" + pname):
                vname = "@" + pname
            v_t = ctx.get_type(vname)
            emitter << f"store {v_t} {registo[0]}, {v_t}* {vname}, align 4"  

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
        emitter << f"br label %{label_fim}"
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
        emitter << f"br label %{label_fim}"
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
        if t != "void":
            if t == 'i8*':
                emitter << f"ret {llvm_string(emitter, elem[0])}"
            else:
                emitter << f"ret {t} {elem[0]}"

    elif node["nt"] == "not":
        res = codegen(node["e"], ctx, emitter)
        rcomp = emitter.get_id()
        emitter << f"%{rcomp} = xor i1 1, {res[0]}"
        return ("%" + rcomp, 'i1')

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
            return ("%" + rcomp, 'i1')

        elif vt_s == '||':
            v_t = vt1[1]
            rcomp = emitter.get_id()
            emitter << f"%{rcomp} = or i1 {vt1[0]}, {vt2[0]}"
            return ("%" + rcomp, 'i1')

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
            if v_t == "float":
                emitter << f"%{rcomp} = fcmp oeq {v_t} {vt1[0]}, {vt2[0]}"
                return ("%" + rcomp, 'i1')
            emitter << f"%{rcomp} = icmp eq {v_t} {vt1[0]}, {vt2[0]}"
            return ("%" + rcomp, 'i1')

        elif vt_s == '<=':
            v_t = vt1[1]
            rcomp = emitter.get_id()
            if v_t == "float":
                emitter << f"%{rcomp} = fcmp ole {v_t} {vt1[0]}, {vt2[0]}"
                return ("%" + rcomp, 'i1')
            emitter << f"%{rcomp} = icmp sle {v_t} {vt1[0]}, {vt2[0]}"
            return ("%" + rcomp, 'i1')

        elif vt_s == '>=':
            v_t = vt1[1]
            rcomp = emitter.get_id()
            if v_t == "float":
                emitter << f"%{rcomp} = fcmp oge {v_t} {vt1[0]}, {vt2[0]}"
                return ("%" + rcomp, 'i1')
            emitter << f"%{rcomp} = icmp sge {v_t} {vt1[0]}, {vt2[0]}"
            return ("%" + rcomp, 'i1')

        elif vt_s == '>':
            v_t = vt1[1]
            rcomp = emitter.get_id()
            if v_t == "float":
                emitter << f"%{rcomp} = fcmp ogt {v_t} {vt1[0]}, {vt2[0]}"
                return ("%" + rcomp, 'i1')
            emitter << f"%{rcomp} = icmp sgt {v_t} {vt1[0]}, {vt2[0]}"
            return ("%" + rcomp, 'i1')

        elif vt_s == '<':
            v_t = vt1[1]
            rcomp = emitter.get_id()
            if v_t == "float":
                emitter << f"%{rcomp} = fcmp olt {v_t} {vt1[0]}, {vt2[0]}"
                return ("%" + rcomp, 'i1')
            emitter << f"%{rcomp} = icmp slt {v_t} {vt1[0]}, {vt2[0]}"
            return ("%" + rcomp, 'i1')

        elif vt_s == '!=':
            v_t = vt1[1]
            rcomp = emitter.get_id()
            if v_t == "float":
                emitter << f"%{rcomp} = fcmp one {v_t} {vt1[0]}, {vt2[0]}"
                return ("%" + rcomp, 'i1')
            emitter << f"%{rcomp} = icmp ne {v_t} {vt1[0]}, {vt2[0]}"
            return ("%" + rcomp, 'i1')
        return

    elif node["nt"] == "expr_e":
        elem = node["e"]
        if "nt" not in elem:
            if "identifier" in elem:
                pname = emitter.get_pointer_name(elem["identifier"])
                if ctx.has_var("@" + pname):
                    tmpname = pname
                    pname = "@" + pname
                    ptype = ctx.get_type(pname)
                    id_global = emitter.get_id()
                    emitter << f"%{id_global} = load {ptype}, {ptype}* @{tmpname}"
                    return ("%" + id_global, ptype)
                elif ctx.has_var("%" + pname):
                    ptype = ctx.get_type("%" + pname)
                    tmpname = f"{emitter.get_id()}"
                    emitter << f"%{tmpname} = load {ptype}, {ptype}* %{pname}"
                    emitter << f"store {ptype} %{tmpname}, {ptype}* %{pname}, align 4"
                    return (f"%{tmpname}", ptype)
                pname = "%" + pname
                ptype = ctx.get_type(pname)
                return (pname, ptype)
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