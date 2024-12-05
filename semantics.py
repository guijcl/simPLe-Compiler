RETURN_CODE = "$ret"

class TypeError(Exception):
    pass

class Context(object):
    def __init__(self):
        self.stack = [{}]
    
    def get_type(self, name):
        for scope in self.stack:
            if name in scope:
                return scope[name]
        raise TypeError(f"Variavel {name} nao esta no contexto")
    
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

def array_type(node):
   if "type" in node:
      return node["type"]
   elif "value_types" in node:
      return ("array", array_type(node["value_types"]))

def check(ctx:Context, node):
   if type(node) is list:
      for i in node:
         check(ctx, i)

   elif node["nt"] == "var_defined":
      name = node["identifier"]
      if ctx.has_var(name):
         raise TypeError(f"Variable {name} is already defined in the context")
      if "value_types" in node:
         return ctx.set_type(name, array_type(node))
      if node["type"] == "void":
         raise TypeError(f"Variable cannot be of void type")
      return ctx.set_type(name, node["type"])

   elif node["nt"] in ["var_declared", "local_var_declared"]:
      name = node["identifier"]
      var_t = node["type"]
      value_t = check(ctx, node["e"])
      if ctx.has_var(name):
         raise TypeError(f"Variable {name} is already defined in the context")
      if node["type"] == "void":
         raise TypeError(f"Variable cannot be of void type")
      if var_t != value_t:
         raise TypeError(f"Type {var_t} and {value_t} don't match.")
      return ctx.set_type(name, node["type"])

   elif node["nt"] == "function_declared":
      name = node["identifier"]
      if ctx.has_var(name):
         raise TypeError(f"Function {name} is already defined in the context")
      assinatura = ()
      if "parameters" in node:
         assinatura = (node["type"], [par["type"] for par in node["parameters"]])
      else:
         assinatura = node["type"]
      ctx.set_type(name, assinatura)

      ctx.enter_scope()
      ctx.set_type(RETURN_CODE, node["type"])
      if "parameters" in node:
         for par in node["parameters"]:
            ctx.set_type(par["identifier"], par["type"])
      ctx.exit_scope()

   elif node["nt"] == "function_defined":
      name = node["identifier"]
      if ctx.has_var(name):
         raise TypeError(f"Function {name} is already defined in the context")
      assinatura = ()
      if "parameters" in node:
         assinatura = (node["type"], [par["type"] for par in node["parameters"]])
      else:
         assinatura = node["type"]
      ctx.set_type(name, assinatura)

      ctx.enter_scope()
      ctx.set_type(RETURN_CODE, node["type"])
      if "parameters" in node:
         for par in node["parameters"]:
            ctx.set_type(par["identifier"], par["type"])
      ctx.enter_scope()
      if node["body"] != [None]:
         for elem in node["body"]:
            check(ctx, elem)
      ctx.exit_scope()
      ctx.exit_scope()

   elif node["nt"] == "function_call":
      e = ctx.get_type(node["identifier"])
      if type(e) != tuple:
         return e
      (expected_return, parameter_types) = e
      for (i, (arg, par_t)) in enumerate(zip(node["parameters"], parameter_types)):
         arg_t = check(ctx, arg)
         if arg_t != par_t:
            index = i + 1
            raise TypeError(f"Argument #{index} expected {par_t} but received {arg_t}") 
      return expected_return

   elif node["nt"] == "array_call":
      index_t = check(ctx, node["index"])
      if index_t != 'int':
         TypeError(f"Index {vt_s} has to be an Integer.")
      return ctx.get_type(node["identifier"])[1]

   elif node["nt"] == "var_assignment":
      name = node["identifier"]
      value_t = check(ctx, node["e"])
      if not ctx.has_var(name):
         raise TypeError(f"Variable {name} is not defined in the context")
      var_t = ctx.get_type(name)
      if type(var_t) == tuple:
         var_t = var_t[0]
      if var_t != value_t:
         raise TypeError(f"Types {var_t} and {value_t} don't match.")
      return ctx.set_type(name, var_t)

   elif node["nt"] == "array_assignment":
      index_t = check(ctx, node["index"])
      if index_t != 'int':
         TypeError(f"Index {vt_s} has to be an Integer.")
      v_types = check(ctx, node["e"])
      a_types = ctx.get_type(node["identifier"])
      if v_types != a_types[1]:
         raise TypeError(f"Types {v_types} and {a_types[1]} don't match.")
      return v_types

   elif node["nt"] == "if_else":
      cond = node["cond"]
      if check(ctx, cond) != "bool":
         raise TypeError(f"If condition {cond} is not boolean")
      ctx.enter_scope()
      for st in node["if"]["body"]:
         check(ctx, st)
      for st in node["else"]["body"]:
         check(ctx, st)
      ctx.exit_scope()

   elif node["nt"] in ["if", "while"]:
      cond = node["cond"]
      if check(ctx, cond) != "bool":
         raise TypeError(f"Condition requires {cond} to be a boolean")
      ctx.enter_scope()
      for st in node["body"]:
         check(ctx, st)
      ctx.exit_scope()

   elif node["nt"] == "return":
      if "ret_e" not in node:
         t = "void"
      elif node["ret_e"]["nt"] == "function_call" and check(ctx, node["ret_e"]) == "void":
         t = "void"
      else:
         t = check(ctx, node["ret_e"])
      expected_t = ctx.get_type(RETURN_CODE)
      if t != expected_t:
         raise TypeError(f"Return expected {expected_t} but received {t}")

   elif node["nt"] == "not":
      cond = node["e"]
      if check(ctx, cond) != "bool":
         raise TypeError(f"Condition requires {cond} to be a boolean") 
      return check(ctx, cond)

   elif node["nt"] == "expr":
      vt1 = check(ctx, node["left"])
      vt2 = check(ctx, node["right"])

      if "sign" in node:
         vt_s = node["sign"]
      if "and_or" in node:
         vt_s = node["and_or"]

      if vt1 != vt2:
         raise TypeError(f"Arguments of operation {vt_s} must be of the same type. Got {vt1} and {vt2}.")

      if vt_s in ["&&", "||"]:
         if vt1 != 'bool':
            raise TypeError(f"Operation {vt_s} requires booleans.")

      if vt_s in ['+', '-', '*', '/']:
         if vt1 not in ['integer', 'int'] and vt1 != 'float':
            raise TypeError(f"Operation {vt_s} requires integers or floats.")

      if vt_s == '%':
         if vt1 not in ['integer', 'int']:
            raise TypeError(f"Operation {vt_s} requires integers.")
      
      if vt_s in ['==', '!=']:
         if vt1 == "string":
            raise TypeError(f"Operation {vt_s} requires non strings.")
         return 'bool'
      elif vt_s in ['<=', '>=', '>', '<']:
         if vt1 == "bool" or vt1 == "string":
            raise TypeError(f"Operation {vt_s} requires non booleans or strings.")
         return 'bool'
      else:
         return vt1

   elif node["nt"] == "expr_e":
      elem = node["e"]
      if "nt" not in elem:
         if "identifier" in elem:
            i = elem["identifier"]
            if not(ctx.has_var(i)):
               raise TypeError(f"{i} not found.")
            return ctx.get_type(i)
         elif "integer" in elem:
            return "int"
         elif "string" in elem:
            return "string"
         elif "float" in elem:
            return "float"
         elif "bool" in elem:
            return "bool"
         elif "array" in elem:
            return ("array", check(ctx, elem["array"]))
      else:
         return check(ctx, elem)

   else:
      print("Semantic missing: ", node["nt"])