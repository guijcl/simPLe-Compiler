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

'''def get_array_value_node_type(tup):
   if type(tup[1]) != tuple:
      return tup[1]
   else:
      return get_array_value_node_type(tup[1])'''

def check(ctx:Context, node):
   if type(node) is list:
      for i in node:
         check(ctx, i)

   elif node["nt"] == "var_defined":
      name = node["identifier"]
      if ctx.has_var(name):
         raise TypeError(f"Variavel {name} ja esta definida no contexto")
      if "value_types" in node: #array
         return ctx.set_type(name, array_type(node)) #array
      if node["type"] == "void":
         raise TypeError(f"Variavel nao pode ser do tipo void")
      return ctx.set_type(name, node["type"])

   elif node["nt"] == "var_declared":
      name = node["identifier"]
      var_t = node["type"]
      value_t = check(ctx, node["e"])
      if ctx.has_var(name):
         raise TypeError(f"Variavel {name} ja esta definida no contexto")
      if node["type"] == "void":
         raise TypeError(f"Variavel nao pode ser do tipo void")
      if var_t != value_t:
         raise TypeError(f"Type {var_t} and {value_t} don't match.")
      return ctx.set_type(name, node["type"])

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

   elif node["nt"] == "function_call":
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

   elif node["nt"] == "array_call":
      index_t = check(ctx, node["index"])
      if index_t != 'int':
         TypeError(f"Index {vt_s} has to be an Integer.")
      return ctx.get_type(node["identifier"])[1]

   elif node["nt"] == "var_assignment":
      name = node["identifier"]
      value_t = check(ctx, node["e"])
      if not ctx.has_var(name):
         raise TypeError(f"Variavel {name} nao esta definida no contexto")
      var_t = ctx.get_type(name)
      if type(var_t) == tuple:
         var_t = var_t[0]
      if var_t != value_t:
         raise TypeError(f"Types {var_t} and {value_t} don't match.")
      return ctx.set_type(name, (var_t, value_t))

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
      if "ret_e" not in node:
         t = "void"
      elif node["ret_e"]["nt"] == "function_call" and check(ctx, node["ret_e"]) == "void":
         t = "void"
      else:
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
         if vt1 == 'integer' or vt1 == 'float':
            raise TypeError(f"Operation {vt_s} requires integers or floats.")

      if vt_s == '%':
         if vt1 != 'integer':
            raise TypeError(f"Operation {vt_s} requires integers.")
      
      if vt_s in ['==', '!=']:
         return 'bool'
      elif vt_s in ['<=', '>=', '>', '<']:
         if vt1 == "bool":
            raise TypeError(f"Operation {vt_s} requires non booleans.")
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


code = [
   {
      "nt":"var_defined",
      "identifier":"arr1",
      "value_types":{
         "value_types":{
            "type":"string"
         }
      }
   },
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
      "identifier":"teste",
      "type":"int",
      "body":[
         {
            "nt":"return",
            "ret_e":{
               "nt":"expr_e",
               "e":{
                  "integer":"5"
               }
            }
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
                     "nt":"function_call_inline",
                     "identifier":"teste"
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
            "nt":"array_assign",
            "identifier":"arr1",
            "index":{
               "nt":"expr_e",
               "e":{
                  "integer":"0"
               }
            },
            "e":{
               "nt":"expr_e",
               "e":{
                  "array":{
                     "nt":"expr_e",
                     "e":{
                        "string":"a"
                     }
                  }
               }
            }
         },
         {
            "nt":"array_call",
            "identifier":"arr1",
            "index":{
               "nt":"expr_e",
               "e":{
                  "integer":"0"
               }
            }
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