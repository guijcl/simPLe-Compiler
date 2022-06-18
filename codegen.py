def get_type(type):
    if type == "string":
        pass
    elif type == "integer" or type == "int":
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
        return f"%pont_{n}"

def codegen(node, emitter=None):
    if type(node) is list:
      for stmt in node:
        codegen(stmt, emitter)
    elif node["nt"] == "var_defined":
        vname = node["identifier"]
        pname = emitter.get_pointer_name(vname)
        emitter << f"{pname} = alloca i32, align 4"
    elif node["nt"] == "var_declared":
        vname = node["identifier"]
        expr = node["e"] 
        pname = emitter.get_pointer_name(vname)
        emitter << f"{pname} = alloca i32, align 4"
        registo = codegen(expr, emitter)
        emitter << f"store i32 {registo}, i32* {pname}, align 4"
    elif node["nt"] == "function_declared":
      pass
    elif node["nt"] == "function_defined":
      pass
    elif node["nt"] in ["function_call", "function_call_inline"]:
      pass
    elif node["nt"] == "assign":
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

        rcomp = "%" + emitter.get_id()
        emitter << f"{rcomp} = {rcond}"
        emitter << f"br i1 {rcomp}, label %{label_then}, label %{label_exit}"

        emitter << f"br label %{label_if_then}"
        for b in blocks:
            codegen(b, emitter)
        rcond = codegen(cond, emitter)
        emitter << f"{label_else_then}:"
        for b in blocks:
            codegen(b, emitter)
        rcond = codegen(cond, emitter)
        return
    elif node["nt"] == "if":
        cond = node["cond"]
        blocks = node["body"]

        id_if = emitter.get_id()
        label_then = "if_then_" + id_if
        label_exit = "if_else_" + id_if

        rcomp = "%" + emitter.get_id()
        emitter << f"{rcomp} = {rcond}"
        emitter << f"br i1 {rcomp}, label %{label_then}, label %{label_exit}"

        emitter << f"br label %{label_then}"
        for b in blocks:
            codegen(b, emitter)
        rcond = codegen(cond, emitter)
        emitter << f"{label_fim}:"
        return
    elif node["nt"] == "while":
        blocks = node["body"]
        cond = node["cond"]

        id_while = emitter.get_id()
        label_inicio = "while_inicio_" + id_while
        label_body = "while_body_" + id_while
        label_fim = "while_fim_" + id_while

        rcomp = "%" + emitter.get_id()
        emitter << f"{rcomp} = {rcond}"
        emitter << f"br i1 {rcomp}, label %{label_inicio}, label %{label_fim}"

        emitter << f"br label %{label_body}"
        for b in blocks:
            codegen(b, emitter)
        rcond = codegen(cond, emitter)
        emitter << f"br label %{label_inicio}"
        emitter << f"{label_fim}:"
        return
    elif node["nt"] == "return":
      pass
    elif node["nt"] == "not":
      pass
    elif node["nt"] == "expr":
      pass
    elif node["nt"] == "expr_e":
      pass
    else:
        pass