
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVMODleftEQUALNEQUALLTELTGTGTEleftANDORAND ARRAY ASSIGNMENT BOOL COLON COMMA COMMENT DIV ELSE EQUAL FLOAT GT GTE IDENTIFIER IF INTEGER LBRACKET LBRACKET_S LPAREN LT LTE MINUS MOD NEQUAL NOT OR PLUS RBRACKET RBRACKET_S RETURN RPAREN SEMICOLON STRING TARRAY TBOOL TFLOAT TIMES TINTEGER TSTRING TVOID VOID WHILE definition_sequence : definition definition_sequence\n\t| definition  definition : function_declaration\n\t| variable_declaration  variable_declaration : identifier COLON type SEMICOLON\n\t| identifier COLON type ASSIGNMENT element SEMICOLON  function_declaration : function_heading body \n\t| identifier COLON type LPAREN parameter_list RPAREN SEMICOLON  function_heading : identifier COLON type LPAREN parameter_list RPAREN  parameter_list : parameter COMMA parameter_list\n\t| parameter  parameter : identifier COLON type  statement_part : LBRACKET statement_sequence RBRACKET  statement_sequence : statement statement_sequence\n\t| statement  statement : statement_part\n\t | assignment_statement\n\t | if_statement\n\t | while_statement\n\t | return_statement\n\t | function_call\n     | expression\n\t |  body : statement  function_call : identifier LPAREN param_list RPAREN SEMICOLON\n\t| identifier LPAREN RPAREN SEMICOLON  param_list : param_list COMMA param\n\t | param  param : expression  assignment_statement : identifier COLON type ASSIGNMENT element SEMICOLON  if_statement : IF expression body ELSE body\n\t| IF expression body  while_statement : WHILE expression body  return_statement : RETURN expression SEMICOLON  expression : expression_m\n\t| expression and_or expression_m  expression_m : expression_s\n\t| expression_m sign expression_s  expression_s : element \n\t| expression_s psign element  and_or : AND\n\t| OR  psign : TIMES \n\t| DIV  sign : PLUS\n\t| MINUS\n\t| MOD\n\t| EQUAL\n\t| NEQUAL\n\t| LT\n\t| LTE\n\t| GT\n\t| GTE  element : identifier\n    | array\n\t| integer\n\t| float\n\t| string\n\t| bool\n\t| LPAREN expression RPAREN \n\t| NOT element \n    | function_call_inline  function_call_inline : identifier LPAREN param_list RPAREN  identifier : IDENTIFIER  integer : INTEGER  float : FLOAT  string : STRING  bool : BOOL  array : identifier LBRACKET_S element RBRACKET_S\n    | identifier LBRACKET_S element RBRACKET_S SEMICOLON  type : TINTEGER\n\t| TFLOAT\n\t| TSTRING \n\t| TBOOL \n\t| TARRAY '
    
_lr_action_items = {'IDENTIFIER':([0,2,3,4,5,7,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,39,40,41,43,45,46,47,48,49,52,53,54,55,56,57,58,59,60,61,62,63,64,65,72,73,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,103,105,106,107,109,110,111,112,114,],[7,7,-3,-4,7,-64,-7,-24,-16,-17,-18,-19,-20,-21,-22,7,-54,-39,7,7,7,7,-35,-37,-55,-56,-57,-58,-59,7,-62,-65,-66,-67,-68,7,-41,-42,7,7,7,7,-54,7,7,-45,-46,-47,-48,-49,-50,-51,-52,-53,7,-43,-44,-61,-36,-13,-32,7,-33,-34,-60,-38,-40,7,-5,7,7,-63,7,-26,-69,7,-25,-70,-31,-63,-9,7,-6,-30,-8,]),'$end':([1,2,3,4,5,7,8,9,10,11,12,13,14,15,16,17,19,20,25,26,27,28,29,30,31,33,34,35,36,37,47,48,49,65,72,73,81,83,84,85,86,87,89,92,94,95,96,103,105,106,107,109,111,112,114,],[0,-2,-3,-4,-23,-64,-1,-7,-24,-16,-17,-18,-19,-20,-21,-22,-54,-39,-35,-37,-55,-56,-57,-58,-59,-62,-65,-66,-67,-68,-23,-54,-23,-61,-36,-13,-32,-33,-34,-60,-38,-40,-5,-63,-26,-69,-23,-25,-70,-31,-63,-9,-6,-30,-8,]),'LBRACKET':([5,7,10,11,12,13,14,15,16,17,18,19,20,25,26,27,28,29,30,31,33,34,35,36,37,43,47,48,49,65,72,73,81,83,84,85,86,87,92,94,95,96,103,105,106,107,109,112,],[18,-64,-24,-16,-17,-18,-19,-20,-21,-22,18,-54,-39,-35,-37,-55,-56,-57,-58,-59,-62,-65,-66,-67,-68,18,18,-54,18,-61,-36,-13,-32,-33,-34,-60,-38,-40,-63,-26,-69,18,-25,-70,-31,-63,-9,-30,]),'IF':([5,7,10,11,12,13,14,15,16,17,18,19,20,25,26,27,28,29,30,31,33,34,35,36,37,43,47,48,49,65,72,73,81,83,84,85,86,87,92,94,95,96,103,105,106,107,109,112,],[21,-64,-24,-16,-17,-18,-19,-20,-21,-22,21,-54,-39,-35,-37,-55,-56,-57,-58,-59,-62,-65,-66,-67,-68,21,21,-54,21,-61,-36,-13,-32,-33,-34,-60,-38,-40,-63,-26,-69,21,-25,-70,-31,-63,-9,-30,]),'WHILE':([5,7,10,11,12,13,14,15,16,17,18,19,20,25,26,27,28,29,30,31,33,34,35,36,37,43,47,48,49,65,72,73,81,83,84,85,86,87,92,94,95,96,103,105,106,107,109,112,],[22,-64,-24,-16,-17,-18,-19,-20,-21,-22,22,-54,-39,-35,-37,-55,-56,-57,-58,-59,-62,-65,-66,-67,-68,22,22,-54,22,-61,-36,-13,-32,-33,-34,-60,-38,-40,-63,-26,-69,22,-25,-70,-31,-63,-9,-30,]),'RETURN':([5,7,10,11,12,13,14,15,16,17,18,19,20,25,26,27,28,29,30,31,33,34,35,36,37,43,47,48,49,65,72,73,81,83,84,85,86,87,92,94,95,96,103,105,106,107,109,112,],[23,-64,-24,-16,-17,-18,-19,-20,-21,-22,23,-54,-39,-35,-37,-55,-56,-57,-58,-59,-62,-65,-66,-67,-68,23,23,-54,23,-61,-36,-13,-32,-33,-34,-60,-38,-40,-63,-26,-69,23,-25,-70,-31,-63,-9,-30,]),'LPAREN':([5,7,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,39,40,41,43,45,46,47,48,49,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,81,82,83,84,85,86,87,90,91,92,93,94,95,96,103,105,106,107,109,112,],[24,-64,-24,-16,-17,-18,-19,-20,-21,-22,24,45,-39,24,24,24,24,-35,-37,-55,-56,-57,-58,-59,24,-62,-65,-66,-67,-68,24,-41,-42,24,24,24,24,82,24,24,-45,-46,-47,-48,-49,-50,-51,-52,-53,24,-43,-44,-61,88,-71,-72,-73,-74,-75,-36,-13,-32,24,-33,-34,-60,-38,-40,24,24,-63,24,-26,-69,24,-25,-70,-31,-63,-9,-30,]),'NOT':([5,7,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,39,40,41,43,45,46,47,48,49,52,53,54,55,56,57,58,59,60,61,62,63,64,65,72,73,81,82,83,84,85,86,87,90,91,92,93,94,95,96,103,105,106,107,109,112,],[32,-64,-24,-16,-17,-18,-19,-20,-21,-22,32,-54,-39,32,32,32,32,-35,-37,-55,-56,-57,-58,-59,32,-62,-65,-66,-67,-68,32,-41,-42,32,32,32,32,-54,32,32,-45,-46,-47,-48,-49,-50,-51,-52,-53,32,-43,-44,-61,-36,-13,-32,32,-33,-34,-60,-38,-40,32,32,-63,32,-26,-69,32,-25,-70,-31,-63,-9,-30,]),'INTEGER':([5,7,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,39,40,41,43,45,46,47,48,49,52,53,54,55,56,57,58,59,60,61,62,63,64,65,72,73,81,82,83,84,85,86,87,90,91,92,93,94,95,96,103,105,106,107,109,112,],[34,-64,-24,-16,-17,-18,-19,-20,-21,-22,34,-54,-39,34,34,34,34,-35,-37,-55,-56,-57,-58,-59,34,-62,-65,-66,-67,-68,34,-41,-42,34,34,34,34,-54,34,34,-45,-46,-47,-48,-49,-50,-51,-52,-53,34,-43,-44,-61,-36,-13,-32,34,-33,-34,-60,-38,-40,34,34,-63,34,-26,-69,34,-25,-70,-31,-63,-9,-30,]),'FLOAT':([5,7,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,39,40,41,43,45,46,47,48,49,52,53,54,55,56,57,58,59,60,61,62,63,64,65,72,73,81,82,83,84,85,86,87,90,91,92,93,94,95,96,103,105,106,107,109,112,],[35,-64,-24,-16,-17,-18,-19,-20,-21,-22,35,-54,-39,35,35,35,35,-35,-37,-55,-56,-57,-58,-59,35,-62,-65,-66,-67,-68,35,-41,-42,35,35,35,35,-54,35,35,-45,-46,-47,-48,-49,-50,-51,-52,-53,35,-43,-44,-61,-36,-13,-32,35,-33,-34,-60,-38,-40,35,35,-63,35,-26,-69,35,-25,-70,-31,-63,-9,-30,]),'STRING':([5,7,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,39,40,41,43,45,46,47,48,49,52,53,54,55,56,57,58,59,60,61,62,63,64,65,72,73,81,82,83,84,85,86,87,90,91,92,93,94,95,96,103,105,106,107,109,112,],[36,-64,-24,-16,-17,-18,-19,-20,-21,-22,36,-54,-39,36,36,36,36,-35,-37,-55,-56,-57,-58,-59,36,-62,-65,-66,-67,-68,36,-41,-42,36,36,36,36,-54,36,36,-45,-46,-47,-48,-49,-50,-51,-52,-53,36,-43,-44,-61,-36,-13,-32,36,-33,-34,-60,-38,-40,36,36,-63,36,-26,-69,36,-25,-70,-31,-63,-9,-30,]),'BOOL':([5,7,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,39,40,41,43,45,46,47,48,49,52,53,54,55,56,57,58,59,60,61,62,63,64,65,72,73,81,82,83,84,85,86,87,90,91,92,93,94,95,96,103,105,106,107,109,112,],[37,-64,-24,-16,-17,-18,-19,-20,-21,-22,37,-54,-39,37,37,37,37,-35,-37,-55,-56,-57,-58,-59,37,-62,-65,-66,-67,-68,37,-41,-42,37,37,37,37,-54,37,37,-45,-46,-47,-48,-49,-50,-51,-52,-53,37,-43,-44,-61,-36,-13,-32,37,-33,-34,-60,-38,-40,37,37,-63,37,-26,-69,37,-25,-70,-31,-63,-9,-30,]),'COLON':([6,7,19,98,],[38,-64,44,108,]),'LBRACKET_S':([7,19,48,],[-64,46,46,]),'TIMES':([7,19,20,26,27,28,29,30,31,33,34,35,36,37,48,65,85,86,87,92,95,105,107,],[-64,-54,-39,63,-55,-56,-57,-58,-59,-62,-65,-66,-67,-68,-54,-61,-60,63,-40,-63,-69,-70,-63,]),'DIV':([7,19,20,26,27,28,29,30,31,33,34,35,36,37,48,65,85,86,87,92,95,105,107,],[-64,-54,-39,64,-55,-56,-57,-58,-59,-62,-65,-66,-67,-68,-54,-61,-60,64,-40,-63,-69,-70,-63,]),'PLUS':([7,19,20,25,26,27,28,29,30,31,33,34,35,36,37,48,65,72,85,86,87,92,95,105,107,],[-64,-54,-39,53,-37,-55,-56,-57,-58,-59,-62,-65,-66,-67,-68,-54,-61,53,-60,-38,-40,-63,-69,-70,-63,]),'MINUS':([7,19,20,25,26,27,28,29,30,31,33,34,35,36,37,48,65,72,85,86,87,92,95,105,107,],[-64,-54,-39,54,-37,-55,-56,-57,-58,-59,-62,-65,-66,-67,-68,-54,-61,54,-60,-38,-40,-63,-69,-70,-63,]),'MOD':([7,19,20,25,26,27,28,29,30,31,33,34,35,36,37,48,65,72,85,86,87,92,95,105,107,],[-64,-54,-39,55,-37,-55,-56,-57,-58,-59,-62,-65,-66,-67,-68,-54,-61,55,-60,-38,-40,-63,-69,-70,-63,]),'EQUAL':([7,19,20,25,26,27,28,29,30,31,33,34,35,36,37,48,65,72,85,86,87,92,95,105,107,],[-64,-54,-39,56,-37,-55,-56,-57,-58,-59,-62,-65,-66,-67,-68,-54,-61,56,-60,-38,-40,-63,-69,-70,-63,]),'NEQUAL':([7,19,20,25,26,27,28,29,30,31,33,34,35,36,37,48,65,72,85,86,87,92,95,105,107,],[-64,-54,-39,57,-37,-55,-56,-57,-58,-59,-62,-65,-66,-67,-68,-54,-61,57,-60,-38,-40,-63,-69,-70,-63,]),'LT':([7,19,20,25,26,27,28,29,30,31,33,34,35,36,37,48,65,72,85,86,87,92,95,105,107,],[-64,-54,-39,58,-37,-55,-56,-57,-58,-59,-62,-65,-66,-67,-68,-54,-61,58,-60,-38,-40,-63,-69,-70,-63,]),'LTE':([7,19,20,25,26,27,28,29,30,31,33,34,35,36,37,48,65,72,85,86,87,92,95,105,107,],[-64,-54,-39,59,-37,-55,-56,-57,-58,-59,-62,-65,-66,-67,-68,-54,-61,59,-60,-38,-40,-63,-69,-70,-63,]),'GT':([7,19,20,25,26,27,28,29,30,31,33,34,35,36,37,48,65,72,85,86,87,92,95,105,107,],[-64,-54,-39,60,-37,-55,-56,-57,-58,-59,-62,-65,-66,-67,-68,-54,-61,60,-60,-38,-40,-63,-69,-70,-63,]),'GTE':([7,19,20,25,26,27,28,29,30,31,33,34,35,36,37,48,65,72,85,86,87,92,95,105,107,],[-64,-54,-39,61,-37,-55,-56,-57,-58,-59,-62,-65,-66,-67,-68,-54,-61,61,-60,-38,-40,-63,-69,-70,-63,]),'AND':([7,17,19,20,25,26,27,28,29,30,31,33,34,35,36,37,47,48,49,50,51,65,72,79,85,86,87,92,95,105,107,],[-64,40,-54,-39,-35,-37,-55,-56,-57,-58,-59,-62,-65,-66,-67,-68,40,-54,40,40,40,-61,-36,40,-60,-38,-40,-63,-69,-70,-63,]),'OR':([7,17,19,20,25,26,27,28,29,30,31,33,34,35,36,37,47,48,49,50,51,65,72,79,85,86,87,92,95,105,107,],[-64,41,-54,-39,-35,-37,-55,-56,-57,-58,-59,-62,-65,-66,-67,-68,41,-54,41,41,41,-61,-36,41,-60,-38,-40,-63,-69,-70,-63,]),'RBRACKET':([7,10,11,12,13,14,15,16,17,18,19,20,25,26,27,28,29,30,31,33,34,35,36,37,42,43,47,48,49,65,72,73,74,81,83,84,85,86,87,92,94,95,96,103,105,106,107,112,],[-64,-24,-16,-17,-18,-19,-20,-21,-22,-23,-54,-39,-35,-37,-55,-56,-57,-58,-59,-62,-65,-66,-67,-68,73,-15,-23,-54,-23,-61,-36,-13,-14,-32,-33,-34,-60,-38,-40,-63,-26,-69,-23,-25,-70,-31,-63,-30,]),'ELSE':([7,10,11,12,13,14,15,16,17,19,20,25,26,27,28,29,30,31,33,34,35,36,37,47,48,49,65,72,73,81,83,84,85,86,87,92,94,95,96,103,105,106,107,112,],[-64,-24,-16,-17,-18,-19,-20,-21,-22,-54,-39,-35,-37,-55,-56,-57,-58,-59,-62,-65,-66,-67,-68,-23,-54,-23,-61,-36,-13,96,-33,-34,-60,-38,-40,-63,-26,-69,-23,-25,-70,-31,-63,-30,]),'SEMICOLON':([7,20,25,26,27,28,29,30,31,33,34,35,36,37,48,50,65,66,67,68,69,70,71,72,77,85,86,87,92,95,101,102,105,107,109,],[-64,-39,-35,-37,-55,-56,-57,-58,-59,-62,-65,-66,-67,-68,-54,84,-61,89,-71,-72,-73,-74,-75,-36,94,-60,-38,-40,103,105,111,112,-70,-63,114,]),'RPAREN':([7,20,25,26,27,28,29,30,31,33,34,35,36,37,45,48,51,65,67,68,69,70,71,72,76,78,79,85,86,87,95,97,99,100,104,105,107,113,115,],[-64,-39,-35,-37,-55,-56,-57,-58,-59,-62,-65,-66,-67,-68,77,-54,85,-61,-71,-72,-73,-74,-75,-36,92,-28,-29,-60,-38,-40,-69,107,109,-11,-27,-70,-63,-12,-10,]),'COMMA':([7,20,25,26,27,28,29,30,31,33,34,35,36,37,48,65,67,68,69,70,71,72,76,78,79,85,86,87,95,97,100,104,105,107,113,],[-64,-39,-35,-37,-55,-56,-57,-58,-59,-62,-65,-66,-67,-68,-54,-61,-71,-72,-73,-74,-75,-36,93,-28,-29,-60,-38,-40,-69,93,110,-27,-70,-63,-12,]),'RBRACKET_S':([7,27,28,29,30,31,33,34,35,36,37,48,65,80,85,95,105,107,],[-64,-55,-56,-57,-58,-59,-62,-65,-66,-67,-68,-54,-61,95,-60,-69,-70,-63,]),'TINTEGER':([38,44,108,],[67,67,67,]),'TFLOAT':([38,44,108,],[68,68,68,]),'TSTRING':([38,44,108,],[69,69,69,]),'TBOOL':([38,44,108,],[70,70,70,]),'TARRAY':([38,44,108,],[71,71,71,]),'ASSIGNMENT':([66,67,68,69,70,71,75,],[90,-71,-72,-73,-74,-75,91,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'definition_sequence':([0,2,],[1,8,]),'definition':([0,2,],[2,2,]),'function_declaration':([0,2,],[3,3,]),'variable_declaration':([0,2,],[4,4,]),'function_heading':([0,2,],[5,5,]),'identifier':([0,2,5,18,21,22,23,24,32,39,43,45,46,47,49,52,62,82,88,90,91,93,96,110,],[6,6,19,19,48,48,48,48,48,48,19,48,48,19,19,48,48,48,98,48,48,48,19,98,]),'body':([5,47,49,96,],[9,81,83,106,]),'statement':([5,18,43,47,49,96,],[10,43,43,10,10,10,]),'statement_part':([5,18,43,47,49,96,],[11,11,11,11,11,11,]),'assignment_statement':([5,18,43,47,49,96,],[12,12,12,12,12,12,]),'if_statement':([5,18,43,47,49,96,],[13,13,13,13,13,13,]),'while_statement':([5,18,43,47,49,96,],[14,14,14,14,14,14,]),'return_statement':([5,18,43,47,49,96,],[15,15,15,15,15,15,]),'function_call':([5,18,43,47,49,96,],[16,16,16,16,16,16,]),'expression':([5,18,21,22,23,24,43,45,47,49,82,93,96,],[17,17,47,49,50,51,17,79,17,17,79,79,17,]),'element':([5,18,21,22,23,24,32,39,43,45,46,47,49,52,62,82,90,91,93,96,],[20,20,20,20,20,20,65,20,20,20,80,20,20,20,87,20,101,102,20,20,]),'expression_m':([5,18,21,22,23,24,39,43,45,47,49,82,93,96,],[25,25,25,25,25,25,72,25,25,25,25,25,25,25,]),'expression_s':([5,18,21,22,23,24,39,43,45,47,49,52,82,93,96,],[26,26,26,26,26,26,26,26,26,26,26,86,26,26,26,]),'array':([5,18,21,22,23,24,32,39,43,45,46,47,49,52,62,82,90,91,93,96,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'integer':([5,18,21,22,23,24,32,39,43,45,46,47,49,52,62,82,90,91,93,96,],[28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'float':([5,18,21,22,23,24,32,39,43,45,46,47,49,52,62,82,90,91,93,96,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'string':([5,18,21,22,23,24,32,39,43,45,46,47,49,52,62,82,90,91,93,96,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'bool':([5,18,21,22,23,24,32,39,43,45,46,47,49,52,62,82,90,91,93,96,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'function_call_inline':([5,18,21,22,23,24,32,39,43,45,46,47,49,52,62,82,90,91,93,96,],[33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'and_or':([17,47,49,50,51,79,],[39,39,39,39,39,39,]),'statement_sequence':([18,43,],[42,74,]),'sign':([25,72,],[52,52,]),'psign':([26,86,],[62,62,]),'type':([38,44,108,],[66,75,113,]),'param_list':([45,82,],[76,97,]),'param':([45,82,93,],[78,78,104,]),'parameter_list':([88,110,],[99,115,]),'parameter':([88,110,],[100,100,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> definition_sequence","S'",1,None,None,None),
  ('definition_sequence -> definition definition_sequence','definition_sequence',2,'p_definition_sequence','rules2.py',11),
  ('definition_sequence -> definition','definition_sequence',1,'p_definition_sequence','rules2.py',12),
  ('definition -> function_declaration','definition',1,'p_definition','rules2.py',19),
  ('definition -> variable_declaration','definition',1,'p_definition','rules2.py',20),
  ('variable_declaration -> identifier COLON type SEMICOLON','variable_declaration',4,'p_variable_declaration','rules2.py',24),
  ('variable_declaration -> identifier COLON type ASSIGNMENT element SEMICOLON','variable_declaration',6,'p_variable_declaration','rules2.py',25),
  ('function_declaration -> function_heading body','function_declaration',2,'p_function_declaration','rules2.py',32),
  ('function_declaration -> identifier COLON type LPAREN parameter_list RPAREN SEMICOLON','function_declaration',7,'p_function_declaration','rules2.py',33),
  ('function_heading -> identifier COLON type LPAREN parameter_list RPAREN','function_heading',6,'p_function_heading','rules2.py',40),
  ('parameter_list -> parameter COMMA parameter_list','parameter_list',3,'p_parameter_list','rules2.py',44),
  ('parameter_list -> parameter','parameter_list',1,'p_parameter_list','rules2.py',45),
  ('parameter -> identifier COLON type','parameter',3,'p_parameter','rules2.py',52),
  ('statement_part -> LBRACKET statement_sequence RBRACKET','statement_part',3,'p_statement_part','rules2.py',56),
  ('statement_sequence -> statement statement_sequence','statement_sequence',2,'p_statement_sequence','rules2.py',60),
  ('statement_sequence -> statement','statement_sequence',1,'p_statement_sequence','rules2.py',61),
  ('statement -> statement_part','statement',1,'p_statement','rules2.py',68),
  ('statement -> assignment_statement','statement',1,'p_statement','rules2.py',69),
  ('statement -> if_statement','statement',1,'p_statement','rules2.py',70),
  ('statement -> while_statement','statement',1,'p_statement','rules2.py',71),
  ('statement -> return_statement','statement',1,'p_statement','rules2.py',72),
  ('statement -> function_call','statement',1,'p_statement','rules2.py',73),
  ('statement -> expression','statement',1,'p_statement','rules2.py',74),
  ('statement -> <empty>','statement',0,'p_statement','rules2.py',75),
  ('body -> statement','body',1,'p_body','rules2.py',80),
  ('function_call -> identifier LPAREN param_list RPAREN SEMICOLON','function_call',5,'p_function_call','rules2.py',84),
  ('function_call -> identifier LPAREN RPAREN SEMICOLON','function_call',4,'p_function_call','rules2.py',85),
  ('param_list -> param_list COMMA param','param_list',3,'p_param_list','rules2.py',92),
  ('param_list -> param','param_list',1,'p_param_list','rules2.py',93),
  ('param -> expression','param',1,'p_param','rules2.py',100),
  ('assignment_statement -> identifier COLON type ASSIGNMENT element SEMICOLON','assignment_statement',6,'p_assignment_statement','rules2.py',104),
  ('if_statement -> IF expression body ELSE body','if_statement',5,'p_if_statement','rules2.py',108),
  ('if_statement -> IF expression body','if_statement',3,'p_if_statement','rules2.py',109),
  ('while_statement -> WHILE expression body','while_statement',3,'p_while_statement','rules2.py',116),
  ('return_statement -> RETURN expression SEMICOLON','return_statement',3,'p_return_statement','rules2.py',120),
  ('expression -> expression_m','expression',1,'p_expression','rules2.py',124),
  ('expression -> expression and_or expression_m','expression',3,'p_expression','rules2.py',125),
  ('expression_m -> expression_s','expression_m',1,'p_expression_m','rules2.py',132),
  ('expression_m -> expression_m sign expression_s','expression_m',3,'p_expression_m','rules2.py',133),
  ('expression_s -> element','expression_s',1,'p_expression_s','rules2.py',140),
  ('expression_s -> expression_s psign element','expression_s',3,'p_expression_s','rules2.py',141),
  ('and_or -> AND','and_or',1,'p_and_or','rules2.py',148),
  ('and_or -> OR','and_or',1,'p_and_or','rules2.py',149),
  ('psign -> TIMES','psign',1,'p_psign','rules2.py',153),
  ('psign -> DIV','psign',1,'p_psign','rules2.py',154),
  ('sign -> PLUS','sign',1,'p_sign','rules2.py',158),
  ('sign -> MINUS','sign',1,'p_sign','rules2.py',159),
  ('sign -> MOD','sign',1,'p_sign','rules2.py',160),
  ('sign -> EQUAL','sign',1,'p_sign','rules2.py',161),
  ('sign -> NEQUAL','sign',1,'p_sign','rules2.py',162),
  ('sign -> LT','sign',1,'p_sign','rules2.py',163),
  ('sign -> LTE','sign',1,'p_sign','rules2.py',164),
  ('sign -> GT','sign',1,'p_sign','rules2.py',165),
  ('sign -> GTE','sign',1,'p_sign','rules2.py',166),
  ('element -> identifier','element',1,'p_element','rules2.py',170),
  ('element -> array','element',1,'p_element','rules2.py',171),
  ('element -> integer','element',1,'p_element','rules2.py',172),
  ('element -> float','element',1,'p_element','rules2.py',173),
  ('element -> string','element',1,'p_element','rules2.py',174),
  ('element -> bool','element',1,'p_element','rules2.py',175),
  ('element -> LPAREN expression RPAREN','element',3,'p_element','rules2.py',176),
  ('element -> NOT element','element',2,'p_element','rules2.py',177),
  ('element -> function_call_inline','element',1,'p_element','rules2.py',178),
  ('function_call_inline -> identifier LPAREN param_list RPAREN','function_call_inline',4,'p_function_call_inline','rules2.py',187),
  ('identifier -> IDENTIFIER','identifier',1,'p_identifier','rules2.py',191),
  ('integer -> INTEGER','integer',1,'p_integer','rules2.py',199),
  ('float -> FLOAT','float',1,'p_float','rules2.py',203),
  ('string -> STRING','string',1,'p_str','rules2.py',207),
  ('bool -> BOOL','bool',1,'p_bool','rules2.py',211),
  ('array -> identifier LBRACKET_S element RBRACKET_S','array',4,'p_array','rules2.py',215),
  ('array -> identifier LBRACKET_S element RBRACKET_S SEMICOLON','array',5,'p_array','rules2.py',216),
  ('type -> TINTEGER','type',1,'p_type','rules2.py',220),
  ('type -> TFLOAT','type',1,'p_type','rules2.py',221),
  ('type -> TSTRING','type',1,'p_type','rules2.py',222),
  ('type -> TBOOL','type',1,'p_type','rules2.py',223),
  ('type -> TARRAY','type',1,'p_type','rules2.py',224),
]