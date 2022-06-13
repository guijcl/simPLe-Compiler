
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVMODleftEQUALNEQUALLTELTGTGTEleftANDORAND ARRAY ASSIGNMENT BOOL COLON COMMA COMMENT DIV ELSE EQUAL FLOAT GT GTE IDENTIFIER IF INTEGER LBRACKET LBRACKET_S LPAREN LT LTE MINUS MOD NEQUAL NOT OR PLUS RBRACKET RBRACKET_S RETURN RPAREN SEMICOLON STRING TARRAY TBOOL TFLOAT TIMES TINTEGER TSTRING TVOID VOID WHILE definition_sequence : definition definition_sequence\n\t| definition  definition : function_declaration\n\t| variable_declaration  variable_declaration : identifier COLON type SEMICOLON\n\t| identifier COLON type ASSIGNMENT expression SEMICOLON  function_declaration : function_heading body \n\t| identifier COLON type LPAREN parameter_list RPAREN SEMICOLON  function_heading : identifier COLON type LPAREN parameter_list RPAREN  parameter_list : parameter COMMA parameter_list\n\t| parameter \n\t|  parameter : identifier COLON type  statement_part : LBRACKET statement_sequence RBRACKET  statement_sequence : statement statement_sequence\n\t| statement  statement : statement_part\n\t | assignment_statement\n\t | if_statement\n\t | while_statement\n\t | return_statement\n\t | function_call\n     | expression\n\t |  body : statement  function_call : identifier LPAREN param_list RPAREN SEMICOLON  param_list : param COMMA param_list\n\t | param \n\t |  param : expression  assignment_statement : identifier COLON type ASSIGNMENT expression SEMICOLON  if_statement : IF expression body ELSE body\n\t| IF expression body  while_statement : WHILE expression body  return_statement : RETURN expression SEMICOLON  expression : expression_m\n\t| expression and_or expression_m  expression_m : expression_e\n\t| expression_m sign expression_e  and_or : AND\n\t| OR  sign : TIMES \n\t| DIV\n\t| PLUS\n\t| MINUS\n\t| MOD\n\t| EQUAL\n\t| NEQUAL\n\t| LT\n\t| LTE\n\t| GT\n\t| GTE  expression_e : identifier\n    | array\n\t| integer\n\t| float\n\t| string\n\t| bool\n\t| LPAREN expression RPAREN \n\t| NOT expression\n    | function_call_inline  function_call_inline : identifier LPAREN param_list RPAREN  identifier : IDENTIFIER  integer : INTEGER  float : FLOAT  string : STRING  bool : BOOL  array : identifier LBRACKET_S expression RBRACKET_S\n    | identifier LBRACKET_S expression RBRACKET_S SEMICOLON  type : TINTEGER\n\t| TFLOAT\n\t| TSTRING \n\t| TBOOL \n\t| TARRAY '
    
_lr_action_items = {'IDENTIFIER':([0,2,3,4,5,7,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,38,39,40,42,44,45,46,47,48,51,52,53,54,55,56,57,58,59,60,61,62,63,70,71,78,79,80,81,82,83,84,85,86,87,88,89,90,91,98,100,101,102,104,105,106,107,109,],[7,7,-3,-4,7,-63,-7,-25,-17,-18,-19,-20,-21,-22,-23,7,-53,7,7,7,7,-36,-38,-54,-55,-56,-57,-58,7,-61,-64,-65,-66,-67,7,-40,-41,7,7,7,7,-53,7,7,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-60,-37,-14,-33,7,-34,-35,-59,-39,7,-5,7,7,-62,7,-68,7,-26,-69,-32,-62,-9,7,-6,-31,-8,]),'$end':([1,2,3,4,5,7,8,9,10,11,12,13,14,15,16,17,19,24,25,26,27,28,29,30,32,33,34,35,36,46,47,48,63,70,71,78,80,81,82,83,85,88,90,91,98,100,101,102,104,106,107,109,],[0,-2,-3,-4,-24,-63,-1,-7,-25,-17,-18,-19,-20,-21,-22,-23,-53,-36,-38,-54,-55,-56,-57,-58,-61,-64,-65,-66,-67,-24,-53,-24,-60,-37,-14,-33,-34,-35,-59,-39,-5,-62,-68,-24,-26,-69,-32,-62,-9,-6,-31,-8,]),'LBRACKET':([5,7,10,11,12,13,14,15,16,17,18,19,24,25,26,27,28,29,30,32,33,34,35,36,42,46,47,48,63,70,71,78,80,81,82,83,88,90,91,98,100,101,102,104,107,],[18,-63,-25,-17,-18,-19,-20,-21,-22,-23,18,-53,-36,-38,-54,-55,-56,-57,-58,-61,-64,-65,-66,-67,18,18,-53,18,-60,-37,-14,-33,-34,-35,-59,-39,-62,-68,18,-26,-69,-32,-62,-9,-31,]),'IF':([5,7,10,11,12,13,14,15,16,17,18,19,24,25,26,27,28,29,30,32,33,34,35,36,42,46,47,48,63,70,71,78,80,81,82,83,88,90,91,98,100,101,102,104,107,],[20,-63,-25,-17,-18,-19,-20,-21,-22,-23,20,-53,-36,-38,-54,-55,-56,-57,-58,-61,-64,-65,-66,-67,20,20,-53,20,-60,-37,-14,-33,-34,-35,-59,-39,-62,-68,20,-26,-69,-32,-62,-9,-31,]),'WHILE':([5,7,10,11,12,13,14,15,16,17,18,19,24,25,26,27,28,29,30,32,33,34,35,36,42,46,47,48,63,70,71,78,80,81,82,83,88,90,91,98,100,101,102,104,107,],[21,-63,-25,-17,-18,-19,-20,-21,-22,-23,21,-53,-36,-38,-54,-55,-56,-57,-58,-61,-64,-65,-66,-67,21,21,-53,21,-60,-37,-14,-33,-34,-35,-59,-39,-62,-68,21,-26,-69,-32,-62,-9,-31,]),'RETURN':([5,7,10,11,12,13,14,15,16,17,18,19,24,25,26,27,28,29,30,32,33,34,35,36,42,46,47,48,63,70,71,78,80,81,82,83,88,90,91,98,100,101,102,104,107,],[22,-63,-25,-17,-18,-19,-20,-21,-22,-23,22,-53,-36,-38,-54,-55,-56,-57,-58,-61,-64,-65,-66,-67,22,22,-53,22,-60,-37,-14,-33,-34,-35,-59,-39,-62,-68,22,-26,-69,-32,-62,-9,-31,]),'LPAREN':([5,7,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,38,39,40,42,44,45,46,47,48,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,78,79,80,81,82,83,86,87,88,89,90,91,98,100,101,102,104,107,],[23,-63,-25,-17,-18,-19,-20,-21,-22,-23,23,44,23,23,23,23,-36,-38,-54,-55,-56,-57,-58,23,-61,-64,-65,-66,-67,23,-40,-41,23,23,23,23,79,23,23,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-60,84,-70,-71,-72,-73,-74,-37,-14,-33,23,-34,-35,-59,-39,23,23,-62,23,-68,23,-26,-69,-32,-62,-9,-31,]),'NOT':([5,7,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,38,39,40,42,44,45,46,47,48,51,52,53,54,55,56,57,58,59,60,61,62,63,70,71,78,79,80,81,82,83,86,87,88,89,90,91,98,100,101,102,104,107,],[31,-63,-25,-17,-18,-19,-20,-21,-22,-23,31,-53,31,31,31,31,-36,-38,-54,-55,-56,-57,-58,31,-61,-64,-65,-66,-67,31,-40,-41,31,31,31,31,-53,31,31,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-60,-37,-14,-33,31,-34,-35,-59,-39,31,31,-62,31,-68,31,-26,-69,-32,-62,-9,-31,]),'INTEGER':([5,7,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,38,39,40,42,44,45,46,47,48,51,52,53,54,55,56,57,58,59,60,61,62,63,70,71,78,79,80,81,82,83,86,87,88,89,90,91,98,100,101,102,104,107,],[33,-63,-25,-17,-18,-19,-20,-21,-22,-23,33,-53,33,33,33,33,-36,-38,-54,-55,-56,-57,-58,33,-61,-64,-65,-66,-67,33,-40,-41,33,33,33,33,-53,33,33,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-60,-37,-14,-33,33,-34,-35,-59,-39,33,33,-62,33,-68,33,-26,-69,-32,-62,-9,-31,]),'FLOAT':([5,7,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,38,39,40,42,44,45,46,47,48,51,52,53,54,55,56,57,58,59,60,61,62,63,70,71,78,79,80,81,82,83,86,87,88,89,90,91,98,100,101,102,104,107,],[34,-63,-25,-17,-18,-19,-20,-21,-22,-23,34,-53,34,34,34,34,-36,-38,-54,-55,-56,-57,-58,34,-61,-64,-65,-66,-67,34,-40,-41,34,34,34,34,-53,34,34,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-60,-37,-14,-33,34,-34,-35,-59,-39,34,34,-62,34,-68,34,-26,-69,-32,-62,-9,-31,]),'STRING':([5,7,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,38,39,40,42,44,45,46,47,48,51,52,53,54,55,56,57,58,59,60,61,62,63,70,71,78,79,80,81,82,83,86,87,88,89,90,91,98,100,101,102,104,107,],[35,-63,-25,-17,-18,-19,-20,-21,-22,-23,35,-53,35,35,35,35,-36,-38,-54,-55,-56,-57,-58,35,-61,-64,-65,-66,-67,35,-40,-41,35,35,35,35,-53,35,35,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-60,-37,-14,-33,35,-34,-35,-59,-39,35,35,-62,35,-68,35,-26,-69,-32,-62,-9,-31,]),'BOOL':([5,7,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,38,39,40,42,44,45,46,47,48,51,52,53,54,55,56,57,58,59,60,61,62,63,70,71,78,79,80,81,82,83,86,87,88,89,90,91,98,100,101,102,104,107,],[36,-63,-25,-17,-18,-19,-20,-21,-22,-23,36,-53,36,36,36,36,-36,-38,-54,-55,-56,-57,-58,36,-61,-64,-65,-66,-67,36,-40,-41,36,36,36,36,-53,36,36,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-60,-37,-14,-33,36,-34,-35,-59,-39,36,36,-62,36,-68,36,-26,-69,-32,-62,-9,-31,]),'COLON':([6,7,19,93,],[37,-63,43,103,]),'LBRACKET_S':([7,19,47,],[-63,45,45,]),'TIMES':([7,19,24,25,26,27,28,29,30,32,33,34,35,36,47,63,70,82,83,88,90,100,102,],[-63,-53,52,-38,-54,-55,-56,-57,-58,-61,-64,-65,-66,-67,-53,-60,52,-59,-39,-62,-68,-69,-62,]),'DIV':([7,19,24,25,26,27,28,29,30,32,33,34,35,36,47,63,70,82,83,88,90,100,102,],[-63,-53,53,-38,-54,-55,-56,-57,-58,-61,-64,-65,-66,-67,-53,-60,53,-59,-39,-62,-68,-69,-62,]),'PLUS':([7,19,24,25,26,27,28,29,30,32,33,34,35,36,47,63,70,82,83,88,90,100,102,],[-63,-53,54,-38,-54,-55,-56,-57,-58,-61,-64,-65,-66,-67,-53,-60,54,-59,-39,-62,-68,-69,-62,]),'MINUS':([7,19,24,25,26,27,28,29,30,32,33,34,35,36,47,63,70,82,83,88,90,100,102,],[-63,-53,55,-38,-54,-55,-56,-57,-58,-61,-64,-65,-66,-67,-53,-60,55,-59,-39,-62,-68,-69,-62,]),'MOD':([7,19,24,25,26,27,28,29,30,32,33,34,35,36,47,63,70,82,83,88,90,100,102,],[-63,-53,56,-38,-54,-55,-56,-57,-58,-61,-64,-65,-66,-67,-53,-60,56,-59,-39,-62,-68,-69,-62,]),'EQUAL':([7,19,24,25,26,27,28,29,30,32,33,34,35,36,47,63,70,82,83,88,90,100,102,],[-63,-53,57,-38,-54,-55,-56,-57,-58,-61,-64,-65,-66,-67,-53,-60,57,-59,-39,-62,-68,-69,-62,]),'NEQUAL':([7,19,24,25,26,27,28,29,30,32,33,34,35,36,47,63,70,82,83,88,90,100,102,],[-63,-53,58,-38,-54,-55,-56,-57,-58,-61,-64,-65,-66,-67,-53,-60,58,-59,-39,-62,-68,-69,-62,]),'LT':([7,19,24,25,26,27,28,29,30,32,33,34,35,36,47,63,70,82,83,88,90,100,102,],[-63,-53,59,-38,-54,-55,-56,-57,-58,-61,-64,-65,-66,-67,-53,-60,59,-59,-39,-62,-68,-69,-62,]),'LTE':([7,19,24,25,26,27,28,29,30,32,33,34,35,36,47,63,70,82,83,88,90,100,102,],[-63,-53,60,-38,-54,-55,-56,-57,-58,-61,-64,-65,-66,-67,-53,-60,60,-59,-39,-62,-68,-69,-62,]),'GT':([7,19,24,25,26,27,28,29,30,32,33,34,35,36,47,63,70,82,83,88,90,100,102,],[-63,-53,61,-38,-54,-55,-56,-57,-58,-61,-64,-65,-66,-67,-53,-60,61,-59,-39,-62,-68,-69,-62,]),'GTE':([7,19,24,25,26,27,28,29,30,32,33,34,35,36,47,63,70,82,83,88,90,100,102,],[-63,-53,62,-38,-54,-55,-56,-57,-58,-61,-64,-65,-66,-67,-53,-60,62,-59,-39,-62,-68,-69,-62,]),'AND':([7,17,19,24,25,26,27,28,29,30,32,33,34,35,36,46,47,48,49,50,63,70,76,77,82,83,88,90,96,97,100,102,],[-63,39,-53,-36,-38,-54,-55,-56,-57,-58,-61,-64,-65,-66,-67,39,-53,39,39,39,39,-37,39,39,-59,-39,-62,-68,39,39,-69,-62,]),'OR':([7,17,19,24,25,26,27,28,29,30,32,33,34,35,36,46,47,48,49,50,63,70,76,77,82,83,88,90,96,97,100,102,],[-63,40,-53,-36,-38,-54,-55,-56,-57,-58,-61,-64,-65,-66,-67,40,-53,40,40,40,40,-37,40,40,-59,-39,-62,-68,40,40,-69,-62,]),'RBRACKET':([7,10,11,12,13,14,15,16,17,18,19,24,25,26,27,28,29,30,32,33,34,35,36,41,42,46,47,48,63,70,71,72,78,80,81,82,83,88,90,91,98,100,101,102,107,],[-63,-25,-17,-18,-19,-20,-21,-22,-23,-24,-53,-36,-38,-54,-55,-56,-57,-58,-61,-64,-65,-66,-67,71,-16,-24,-53,-24,-60,-37,-14,-15,-33,-34,-35,-59,-39,-62,-68,-24,-26,-69,-32,-62,-31,]),'ELSE':([7,10,11,12,13,14,15,16,17,19,24,25,26,27,28,29,30,32,33,34,35,36,46,47,48,63,70,71,78,80,81,82,83,88,90,91,98,100,101,102,107,],[-63,-25,-17,-18,-19,-20,-21,-22,-23,-53,-36,-38,-54,-55,-56,-57,-58,-61,-64,-65,-66,-67,-24,-53,-24,-60,-37,-14,91,-34,-35,-59,-39,-62,-68,-24,-26,-69,-32,-62,-31,]),'SEMICOLON':([7,24,25,26,27,28,29,30,32,33,34,35,36,47,49,63,64,65,66,67,68,69,70,82,83,88,90,96,97,100,102,104,],[-63,-36,-38,-54,-55,-56,-57,-58,-61,-64,-65,-66,-67,-53,81,-60,85,-70,-71,-72,-73,-74,-37,-59,-39,98,100,106,107,-69,-62,109,]),'RPAREN':([7,24,25,26,27,28,29,30,32,33,34,35,36,44,47,50,63,65,66,67,68,69,70,74,75,76,79,82,83,84,89,90,92,94,95,99,100,102,105,108,110,],[-63,-36,-38,-54,-55,-56,-57,-58,-61,-64,-65,-66,-67,-29,-53,82,-60,-70,-71,-72,-73,-74,-37,88,-28,-30,-29,-59,-39,-12,-29,-68,102,104,-11,-27,-69,-62,-12,-13,-10,]),'COMMA':([7,24,25,26,27,28,29,30,32,33,34,35,36,47,63,65,66,67,68,69,70,75,76,82,83,90,95,100,102,108,],[-63,-36,-38,-54,-55,-56,-57,-58,-61,-64,-65,-66,-67,-53,-60,-70,-71,-72,-73,-74,-37,89,-30,-59,-39,-68,105,-69,-62,-13,]),'RBRACKET_S':([7,24,25,26,27,28,29,30,32,33,34,35,36,47,63,70,77,82,83,90,100,102,],[-63,-36,-38,-54,-55,-56,-57,-58,-61,-64,-65,-66,-67,-53,-60,-37,90,-59,-39,-68,-69,-62,]),'TINTEGER':([37,43,103,],[65,65,65,]),'TFLOAT':([37,43,103,],[66,66,66,]),'TSTRING':([37,43,103,],[67,67,67,]),'TBOOL':([37,43,103,],[68,68,68,]),'TARRAY':([37,43,103,],[69,69,69,]),'ASSIGNMENT':([64,65,66,67,68,69,73,],[86,-70,-71,-72,-73,-74,87,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'definition_sequence':([0,2,],[1,8,]),'definition':([0,2,],[2,2,]),'function_declaration':([0,2,],[3,3,]),'variable_declaration':([0,2,],[4,4,]),'function_heading':([0,2,],[5,5,]),'identifier':([0,2,5,18,20,21,22,23,31,38,42,44,45,46,48,51,79,84,86,87,89,91,105,],[6,6,19,19,47,47,47,47,47,47,19,47,47,19,19,47,47,93,47,47,47,19,93,]),'body':([5,46,48,91,],[9,78,80,101,]),'statement':([5,18,42,46,48,91,],[10,42,42,10,10,10,]),'statement_part':([5,18,42,46,48,91,],[11,11,11,11,11,11,]),'assignment_statement':([5,18,42,46,48,91,],[12,12,12,12,12,12,]),'if_statement':([5,18,42,46,48,91,],[13,13,13,13,13,13,]),'while_statement':([5,18,42,46,48,91,],[14,14,14,14,14,14,]),'return_statement':([5,18,42,46,48,91,],[15,15,15,15,15,15,]),'function_call':([5,18,42,46,48,91,],[16,16,16,16,16,16,]),'expression':([5,18,20,21,22,23,31,42,44,45,46,48,79,86,87,89,91,],[17,17,46,48,49,50,63,17,76,77,17,17,76,96,97,76,17,]),'expression_m':([5,18,20,21,22,23,31,38,42,44,45,46,48,79,86,87,89,91,],[24,24,24,24,24,24,24,70,24,24,24,24,24,24,24,24,24,24,]),'expression_e':([5,18,20,21,22,23,31,38,42,44,45,46,48,51,79,86,87,89,91,],[25,25,25,25,25,25,25,25,25,25,25,25,25,83,25,25,25,25,25,]),'array':([5,18,20,21,22,23,31,38,42,44,45,46,48,51,79,86,87,89,91,],[26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'integer':([5,18,20,21,22,23,31,38,42,44,45,46,48,51,79,86,87,89,91,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'float':([5,18,20,21,22,23,31,38,42,44,45,46,48,51,79,86,87,89,91,],[28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'string':([5,18,20,21,22,23,31,38,42,44,45,46,48,51,79,86,87,89,91,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'bool':([5,18,20,21,22,23,31,38,42,44,45,46,48,51,79,86,87,89,91,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'function_call_inline':([5,18,20,21,22,23,31,38,42,44,45,46,48,51,79,86,87,89,91,],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'and_or':([17,46,48,49,50,63,76,77,96,97,],[38,38,38,38,38,38,38,38,38,38,]),'statement_sequence':([18,42,],[41,72,]),'sign':([24,70,],[51,51,]),'type':([37,43,103,],[64,73,108,]),'param_list':([44,79,89,],[74,92,99,]),'param':([44,79,89,],[75,75,75,]),'parameter_list':([84,105,],[94,110,]),'parameter':([84,105,],[95,95,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> definition_sequence","S'",1,None,None,None),
  ('definition_sequence -> definition definition_sequence','definition_sequence',2,'p_definition_sequence','rules.py',12),
  ('definition_sequence -> definition','definition_sequence',1,'p_definition_sequence','rules.py',13),
  ('definition -> function_declaration','definition',1,'p_definition','rules.py',20),
  ('definition -> variable_declaration','definition',1,'p_definition','rules.py',21),
  ('variable_declaration -> identifier COLON type SEMICOLON','variable_declaration',4,'p_variable_declaration','rules.py',25),
  ('variable_declaration -> identifier COLON type ASSIGNMENT expression SEMICOLON','variable_declaration',6,'p_variable_declaration','rules.py',26),
  ('function_declaration -> function_heading body','function_declaration',2,'p_function_declaration','rules.py',33),
  ('function_declaration -> identifier COLON type LPAREN parameter_list RPAREN SEMICOLON','function_declaration',7,'p_function_declaration','rules.py',34),
  ('function_heading -> identifier COLON type LPAREN parameter_list RPAREN','function_heading',6,'p_function_heading','rules.py',45),
  ('parameter_list -> parameter COMMA parameter_list','parameter_list',3,'p_parameter_list','rules.py',51),
  ('parameter_list -> parameter','parameter_list',1,'p_parameter_list','rules.py',52),
  ('parameter_list -> <empty>','parameter_list',0,'p_parameter_list','rules.py',53),
  ('parameter -> identifier COLON type','parameter',3,'p_parameter','rules.py',60),
  ('statement_part -> LBRACKET statement_sequence RBRACKET','statement_part',3,'p_statement_part','rules.py',64),
  ('statement_sequence -> statement statement_sequence','statement_sequence',2,'p_statement_sequence','rules.py',68),
  ('statement_sequence -> statement','statement_sequence',1,'p_statement_sequence','rules.py',69),
  ('statement -> statement_part','statement',1,'p_statement','rules.py',76),
  ('statement -> assignment_statement','statement',1,'p_statement','rules.py',77),
  ('statement -> if_statement','statement',1,'p_statement','rules.py',78),
  ('statement -> while_statement','statement',1,'p_statement','rules.py',79),
  ('statement -> return_statement','statement',1,'p_statement','rules.py',80),
  ('statement -> function_call','statement',1,'p_statement','rules.py',81),
  ('statement -> expression','statement',1,'p_statement','rules.py',82),
  ('statement -> <empty>','statement',0,'p_statement','rules.py',83),
  ('body -> statement','body',1,'p_body','rules.py',88),
  ('function_call -> identifier LPAREN param_list RPAREN SEMICOLON','function_call',5,'p_function_call','rules.py',92),
  ('param_list -> param COMMA param_list','param_list',3,'p_param_list','rules.py',99),
  ('param_list -> param','param_list',1,'p_param_list','rules.py',100),
  ('param_list -> <empty>','param_list',0,'p_param_list','rules.py',101),
  ('param -> expression','param',1,'p_param','rules.py',108),
  ('assignment_statement -> identifier COLON type ASSIGNMENT expression SEMICOLON','assignment_statement',6,'p_assignment_statement','rules.py',112),
  ('if_statement -> IF expression body ELSE body','if_statement',5,'p_if_statement','rules.py',116),
  ('if_statement -> IF expression body','if_statement',3,'p_if_statement','rules.py',117),
  ('while_statement -> WHILE expression body','while_statement',3,'p_while_statement','rules.py',124),
  ('return_statement -> RETURN expression SEMICOLON','return_statement',3,'p_return_statement','rules.py',128),
  ('expression -> expression_m','expression',1,'p_expression','rules.py',132),
  ('expression -> expression and_or expression_m','expression',3,'p_expression','rules.py',133),
  ('expression_m -> expression_e','expression_m',1,'p_expression_m','rules.py',140),
  ('expression_m -> expression_m sign expression_e','expression_m',3,'p_expression_m','rules.py',141),
  ('and_or -> AND','and_or',1,'p_and_or','rules.py',148),
  ('and_or -> OR','and_or',1,'p_and_or','rules.py',149),
  ('sign -> TIMES','sign',1,'p_sign','rules.py',153),
  ('sign -> DIV','sign',1,'p_sign','rules.py',154),
  ('sign -> PLUS','sign',1,'p_sign','rules.py',155),
  ('sign -> MINUS','sign',1,'p_sign','rules.py',156),
  ('sign -> MOD','sign',1,'p_sign','rules.py',157),
  ('sign -> EQUAL','sign',1,'p_sign','rules.py',158),
  ('sign -> NEQUAL','sign',1,'p_sign','rules.py',159),
  ('sign -> LT','sign',1,'p_sign','rules.py',160),
  ('sign -> LTE','sign',1,'p_sign','rules.py',161),
  ('sign -> GT','sign',1,'p_sign','rules.py',162),
  ('sign -> GTE','sign',1,'p_sign','rules.py',163),
  ('expression_e -> identifier','expression_e',1,'p_expression_e','rules.py',167),
  ('expression_e -> array','expression_e',1,'p_expression_e','rules.py',168),
  ('expression_e -> integer','expression_e',1,'p_expression_e','rules.py',169),
  ('expression_e -> float','expression_e',1,'p_expression_e','rules.py',170),
  ('expression_e -> string','expression_e',1,'p_expression_e','rules.py',171),
  ('expression_e -> bool','expression_e',1,'p_expression_e','rules.py',172),
  ('expression_e -> LPAREN expression RPAREN','expression_e',3,'p_expression_e','rules.py',173),
  ('expression_e -> NOT expression','expression_e',2,'p_expression_e','rules.py',174),
  ('expression_e -> function_call_inline','expression_e',1,'p_expression_e','rules.py',175),
  ('function_call_inline -> identifier LPAREN param_list RPAREN','function_call_inline',4,'p_function_call_inline','rules.py',184),
  ('identifier -> IDENTIFIER','identifier',1,'p_identifier','rules.py',191),
  ('integer -> INTEGER','integer',1,'p_integer','rules.py',199),
  ('float -> FLOAT','float',1,'p_float','rules.py',203),
  ('string -> STRING','string',1,'p_str','rules.py',207),
  ('bool -> BOOL','bool',1,'p_bool','rules.py',211),
  ('array -> identifier LBRACKET_S expression RBRACKET_S','array',4,'p_array','rules.py',215),
  ('array -> identifier LBRACKET_S expression RBRACKET_S SEMICOLON','array',5,'p_array','rules.py',216),
  ('type -> TINTEGER','type',1,'p_type','rules.py',220),
  ('type -> TFLOAT','type',1,'p_type','rules.py',221),
  ('type -> TSTRING','type',1,'p_type','rules.py',222),
  ('type -> TBOOL','type',1,'p_type','rules.py',223),
  ('type -> TARRAY','type',1,'p_type','rules.py',224),
]
