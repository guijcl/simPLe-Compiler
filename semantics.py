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

def check(ctx:Context, node):
   if type(node) is list:
      for i in node:
         check(ctx, i)
   elif node["nt"] == "var_defined":
      name = node["identifier"]
      if ctx.has_var(name):
         raise TypeError(f"Variavel {name} ja esta definida no contexto")
      return ctx.set_type(name, node["type"])
   elif node["nt"] == "var_declared":
      name = node["identifier"]
      var_t = node["type"]
      value_t = check(ctx, node["e"])
      if ctx.has_var(name):
         raise TypeError(f"Variavel {name} ja esta definida no contexto")
      if var_t != value_t:
         raise TypeError(f"Type {var_t} and {value_t} don't match.")
      return ctx.set_type(name, (node["type"], check(ctx, node["e"])))   
   elif node["nt"] == "function_declared":
      name = node["identifier"]
      if ctx.has_var(name):
         raise TypeError(f"Funcao {name} ja esta definida no contexto")
      assinatura = ()
      if "parameters" in node:
         assinatura = (node["type"], [node["type"] for par in node["parameters"]])
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
         raise TypeError(f"Funcao {name} ja esta definida no contexto")
      assinatura = ()
      if "parameters" in node:
         assinatura = (node["type"], [node["type"] for par in node["parameters"]])
      else:
         assinatura = node["type"]
      ctx.set_type(name, assinatura)

      ctx.enter_scope()
      ctx.set_type(RETURN_CODE, node["type"])
      if "parameters" in node:
         for par in node["parameters"]:
            ctx.set_type(par["identifier"], par["type"])
      ctx.enter_scope()
      for elem in node["body"]:
         check(ctx, elem)
      ctx.exit_scope()
      ctx.exit_scope()
   elif node["nt"] in ["function_call", "function_call_inline"]:
      e = ctx.get_type(node["identifier"])
      if type(e) != tuple:
         return e
      (expected_return, parameter_types) = e
      for (i, (arg, par_t)) in enumerate(zip(node["parameters"], parameter_types)):
         arg_t = check(ctx, arg)
         if arg_t != par_t:
            index = i + 1
            raise TypeError(f"Argumento #{index} esperava {par_t} mas recebe {arg_t}") 
      return expected_return
   elif node["nt"] == "assign":
      name = node["identifier"]
      var_t = node["type"]
      value_t = check(ctx, node["e"])
      if ctx.has_var(name):
         raise TypeError(f"Variavel {name} ja esta definida no contexto")
      if var_t != value_t:
         raise TypeError(f"Type {var_t} and {value_t} don't match.")
      return ctx.set_type(name, (var_t, value_t))
   elif node["nt"] == "if_else":
      cond = node["cond"]
      if check(ctx, cond) != "bool":
         raise TypeError(f"Condicao do if {cond} nao e boolean")
      ctx.enter_scope()
      for st in node["if"]["body"]:
         check(ctx, st)
      for st in node["else"]["body"]:
         check(ctx, st)
      ctx.exit_scope()
   elif node["nt"] in ["if", "while"]:
      cond = node["cond"]
      if check(ctx, cond) != "bool":
         raise TypeError(f"Condicao requer que {cond} seja boolean")
      ctx.enter_scope()
      for st in node["body"]:
         check(ctx, st)
      ctx.exit_scope()
   elif node["nt"] == "return":
      t = check(ctx, node["ret_e"])
      expected_t = ctx.get_type(RETURN_CODE)
      if t != expected_t:
         raise TypeError(f"Return esperava {expected_t} mas recebe {t}")
   elif node["nt"] == "not":
      cond = node["e"]
      if check(ctx, cond) != "bool":
         raise TypeError(f"Condicao requer que {cond} seja boolean") 
   elif node["nt"] == "expr":
      vt1 = check(ctx, node["left"])
      vt2 = check(ctx, node["right"])
      vt_s = node["sign"]

      if vt1 != vt2:
         raise TypeError(f"Arguments of operation {vt_s} must be of the same type. Got {vt1} and {vt2}.")

      if vt_s == 'mod':
         if vt1 != 'integer':
            raise TypeError(f"Operation {vt_s} requires integers.")
      
      if vt_s in ['==', '<=', '>=', '>', '<', '!=']:
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
         elif "float" in elem:
            return "float"
         elif "bool" in elem:
            return "bool"
         elif "array" in elem:
            index_t = check(elem["index"])
            if index_t != 'int':
               TypeError(f"Index {vt_s} has to be an Integer.")
            return "array"
      else:
         return check(ctx, elem)
   else:
      print("Semantic missing: ", node["nt"])


code = [
   {
      "nt":"function_declared",
      "identifier":"min",
      "type":"int",
      "parameters":[
         {
            "identifier":"a",
            "type":"int"
         },
         {
            "identifier":"b",
            "type":"int"
         }
      ]
   },
   {
      "nt":"function_defined",
      "identifier":"max",
      "type":"int",
      "parameters":[
         {
            "identifier":"a",
            "type":"int"
         },
         {
            "identifier":"b",
            "type":"int"
         }
      ],
      "body":[
         {
            "nt":"if",
            "cond":{
               "nt":"expr",
               "sign":">",
               "left":{
                  "nt":"expr_e",
                  "e":{
                     "identifier":"a"
                  }
               },
               "right":{
                  "nt":"expr_e",
                  "e":{
                     "identifier":"b"
                  }
               }
            },
            "body":[
               {
                  "nt":"return",
                  "ret_e":{
                     "nt":"expr_e",
                     "e":{
                        "identifier":"a"
                     }
                  }
               }
            ]
         },
         {
            "nt":"return",
            "ret_e":{
               "nt":"expr_e",
               "e":{
                  "identifier":"b"
               }
            }
         }
      ]
   },
   {
      "nt":"var_declared",
      "type":"int",
      "identifier":"pi",
      "e":{
         "nt":"expr_e",
         "e":{
            "integer":"3"
         }
      }
   }
]


check(Context(), code)