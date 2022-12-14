
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'CHAR COMMA DIVIDE ELSE EQUALS FLOAT FLOATN GE GT ID IF INT INTEGER LBRACES LE LPAREN LT MAIN MINUS NE PLUS POWER RBRACES RPAREN SEMI SEMICOLON STRING TIMESinicio : INT MAIN LPAREN RPAREN blocoprincipalconteudo : declaracoes\n                | declaracoes conteudo\n                | atribuicoes \n                | atribuicoes conteudo\n                | if  \n                | if conteudo \n                | emptyblocoprincipal : LBRACES conteudo RBRACESids : COMMA ID\n            | COMMA ID idsempty :declaracoes : tipo ID SEMICOLON\n                    | tipo ID ids SEMICOLON \n                    | tipo ID EQUALS INTEGER SEMICOLON \n                    | tipo ID EQUALS FLOATN SEMICOLON \n                    | emptyatribuicoes : ID EQUALS INTEGER SEMICOLON\n                    | ID EQUALS FLOATN SEMICOLONcondicao : ID LT INTEGER\n                | ID LE INTEGER \n                | ID LT FLOATN\n                | ID GT INTEGER \n                | ID GE FLOATN\n                | ID GE INTEGER \n                | ID GT FLOATN\n                | ID LE FLOATNbloco : LBRACES  conteudo_if RBRACESconteudo_if : atribuicoes conteudo_if\n                    | operacao conteudo_if\n                    | if\n                    | empty\n    if   : IF LPAREN condicao RPAREN bloco\n            | IF LPAREN condicao RPAREN bloco elseelse : ELSE blocooperador : PLUS\n                | MINUS\n                | TIMES\n                | POWER\n                | DIVIDEoperacao : ID EQUALS ID operador ID SEMICOLON operacao \n                | ID EQUALS ID operador INTEGER SEMICOLON operacao\n                | ID EQUALS ID operador FLOATN SEMICOLON operacao\n                | ID EQUALS INTEGER operador INTEGER SEMICOLON operacao\n                | ID EQUALS FLOATN operador INTEGER SEMICOLON operacao\n                | ID EQUALS INTEGER operador ID SEMICOLON operacao\n                | ID EQUALS FLOATN operador ID SEMICOLON operacao\n                | emptytipo : INT\n            | FLOAT \n            | CHAR'
    
_lr_action_items = {'INT':([0,7,9,10,11,12,26,34,38,39,45,46,48,58,66,67,],[2,16,16,16,16,-17,-13,-14,-18,-19,-15,-16,-33,-34,-35,-28,]),'$end':([1,6,19,],[0,-1,-9,]),'MAIN':([2,],[3,]),'LPAREN':([3,15,],[4,25,]),'RPAREN':([4,32,50,51,52,53,54,55,56,57,],[5,40,-20,-22,-21,-27,-23,-26,-24,-25,]),'LBRACES':([5,40,59,],[7,49,49,]),'ID':([7,9,10,11,12,13,16,17,18,25,26,29,34,38,39,45,46,48,49,58,61,62,64,66,67,70,74,75,76,77,78,79,80,81,89,90,91,92,93,94,95,97,98,99,100,101,102,103,104,105,],[14,14,14,14,-17,23,-49,-50,-51,33,-13,37,-14,-18,-19,-15,-16,-33,65,-34,65,65,-48,-35,-28,71,82,-36,-37,-38,-39,-40,85,87,96,96,96,96,96,96,96,-41,-48,-42,-43,-46,-44,-47,-45,71,]),'IF':([7,9,10,11,12,26,34,38,39,45,46,48,49,58,61,62,64,66,67,89,90,91,92,93,94,95,97,98,99,100,101,102,103,104,],[15,15,15,15,-17,-13,-14,-18,-19,-15,-16,-33,15,-34,15,15,-48,-35,-28,-12,-12,-12,-12,-12,-12,-12,-41,-48,-42,-43,-46,-44,-47,-45,]),'RBRACES':([7,8,9,10,11,12,20,21,22,26,34,38,39,45,46,48,49,58,60,61,62,63,64,66,67,68,69,89,90,91,92,93,94,95,97,98,99,100,101,102,103,104,],[-12,19,-2,-4,-6,-8,-3,-5,-7,-13,-14,-18,-19,-15,-16,-33,-12,-34,67,-12,-12,-31,-32,-35,-28,-29,-30,-12,-12,-12,-12,-12,-12,-12,-41,-48,-42,-43,-46,-44,-47,-45,]),'FLOAT':([7,9,10,11,12,26,34,38,39,45,46,48,58,66,67,],[17,17,17,17,-17,-13,-14,-18,-19,-15,-16,-33,-34,-35,-28,]),'CHAR':([7,9,10,11,12,26,34,38,39,45,46,48,58,66,67,],[18,18,18,18,-17,-13,-14,-18,-19,-15,-16,-33,-34,-35,-28,]),'EQUALS':([14,23,65,96,],[24,28,70,105,]),'SEMICOLON':([23,27,30,31,35,36,37,47,72,73,82,83,84,85,86,87,88,],[26,34,38,39,45,46,-10,-11,38,39,89,90,91,92,93,94,95,]),'COMMA':([23,37,],[29,29,]),'INTEGER':([24,28,41,42,43,44,70,74,75,76,77,78,79,80,81,105,],[30,35,50,52,54,57,72,83,-36,-37,-38,-39,-40,86,88,106,]),'FLOATN':([24,28,41,42,43,44,70,74,75,76,77,78,79,105,],[31,36,51,53,55,56,73,84,-36,-37,-38,-39,-40,107,]),'LT':([33,],[41,]),'LE':([33,],[42,]),'GT':([33,],[43,]),'GE':([33,],[44,]),'ELSE':([48,67,],[59,-28,]),'PLUS':([71,72,73,106,107,],[75,75,75,75,75,]),'MINUS':([71,72,73,106,107,],[76,76,76,76,76,]),'TIMES':([71,72,73,106,107,],[77,77,77,77,77,]),'POWER':([71,72,73,106,107,],[78,78,78,78,78,]),'DIVIDE':([71,72,73,106,107,],[79,79,79,79,79,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'inicio':([0,],[1,]),'blocoprincipal':([5,],[6,]),'conteudo':([7,9,10,11,],[8,20,21,22,]),'declaracoes':([7,9,10,11,],[9,9,9,9,]),'atribuicoes':([7,9,10,11,49,61,62,],[10,10,10,10,61,61,61,]),'if':([7,9,10,11,49,61,62,],[11,11,11,11,63,63,63,]),'empty':([7,9,10,11,49,61,62,89,90,91,92,93,94,95,],[12,12,12,12,64,64,64,98,98,98,98,98,98,98,]),'tipo':([7,9,10,11,],[13,13,13,13,]),'ids':([23,37,],[27,47,]),'condicao':([25,],[32,]),'bloco':([40,59,],[48,66,]),'else':([48,],[58,]),'conteudo_if':([49,61,62,],[60,68,69,]),'operacao':([49,61,62,89,90,91,92,93,94,95,],[62,62,62,97,99,100,101,102,103,104,]),'operador':([71,72,73,106,107,],[74,80,81,80,81,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> inicio","S'",1,None,None,None),
  ('inicio -> INT MAIN LPAREN RPAREN blocoprincipal','inicio',5,'p_inicio','complador.py',77),
  ('conteudo -> declaracoes','conteudo',1,'p_conteudo','complador.py',81),
  ('conteudo -> declaracoes conteudo','conteudo',2,'p_conteudo','complador.py',82),
  ('conteudo -> atribuicoes','conteudo',1,'p_conteudo','complador.py',83),
  ('conteudo -> atribuicoes conteudo','conteudo',2,'p_conteudo','complador.py',84),
  ('conteudo -> if','conteudo',1,'p_conteudo','complador.py',85),
  ('conteudo -> if conteudo','conteudo',2,'p_conteudo','complador.py',86),
  ('conteudo -> empty','conteudo',1,'p_conteudo','complador.py',87),
  ('blocoprincipal -> LBRACES conteudo RBRACES','blocoprincipal',3,'p_blocoprincipal','complador.py',90),
  ('ids -> COMMA ID','ids',2,'p_ids','complador.py',94),
  ('ids -> COMMA ID ids','ids',3,'p_ids','complador.py',95),
  ('empty -> <empty>','empty',0,'p_empty','complador.py',98),
  ('declaracoes -> tipo ID SEMICOLON','declaracoes',3,'p_declaracoes','complador.py',105),
  ('declaracoes -> tipo ID ids SEMICOLON','declaracoes',4,'p_declaracoes','complador.py',106),
  ('declaracoes -> tipo ID EQUALS INTEGER SEMICOLON','declaracoes',5,'p_declaracoes','complador.py',107),
  ('declaracoes -> tipo ID EQUALS FLOATN SEMICOLON','declaracoes',5,'p_declaracoes','complador.py',108),
  ('declaracoes -> empty','declaracoes',1,'p_declaracoes','complador.py',109),
  ('atribuicoes -> ID EQUALS INTEGER SEMICOLON','atribuicoes',4,'p_atribuicoes','complador.py',115),
  ('atribuicoes -> ID EQUALS FLOATN SEMICOLON','atribuicoes',4,'p_atribuicoes','complador.py',116),
  ('condicao -> ID LT INTEGER','condicao',3,'p_condicao','complador.py',119),
  ('condicao -> ID LE INTEGER','condicao',3,'p_condicao','complador.py',120),
  ('condicao -> ID LT FLOATN','condicao',3,'p_condicao','complador.py',121),
  ('condicao -> ID GT INTEGER','condicao',3,'p_condicao','complador.py',122),
  ('condicao -> ID GE FLOATN','condicao',3,'p_condicao','complador.py',123),
  ('condicao -> ID GE INTEGER','condicao',3,'p_condicao','complador.py',124),
  ('condicao -> ID GT FLOATN','condicao',3,'p_condicao','complador.py',125),
  ('condicao -> ID LE FLOATN','condicao',3,'p_condicao','complador.py',126),
  ('bloco -> LBRACES conteudo_if RBRACES','bloco',3,'p_bloco','complador.py',129),
  ('conteudo_if -> atribuicoes conteudo_if','conteudo_if',2,'p_conteudo_if','complador.py',132),
  ('conteudo_if -> operacao conteudo_if','conteudo_if',2,'p_conteudo_if','complador.py',133),
  ('conteudo_if -> if','conteudo_if',1,'p_conteudo_if','complador.py',134),
  ('conteudo_if -> empty','conteudo_if',1,'p_conteudo_if','complador.py',135),
  ('if -> IF LPAREN condicao RPAREN bloco','if',5,'p_if','complador.py',139),
  ('if -> IF LPAREN condicao RPAREN bloco else','if',6,'p_if','complador.py',140),
  ('else -> ELSE bloco','else',2,'p_else','complador.py',145),
  ('operador -> PLUS','operador',1,'p_operador','complador.py',148),
  ('operador -> MINUS','operador',1,'p_operador','complador.py',149),
  ('operador -> TIMES','operador',1,'p_operador','complador.py',150),
  ('operador -> POWER','operador',1,'p_operador','complador.py',151),
  ('operador -> DIVIDE','operador',1,'p_operador','complador.py',152),
  ('operacao -> ID EQUALS ID operador ID SEMICOLON operacao','operacao',7,'p_operacao','complador.py',155),
  ('operacao -> ID EQUALS ID operador INTEGER SEMICOLON operacao','operacao',7,'p_operacao','complador.py',156),
  ('operacao -> ID EQUALS ID operador FLOATN SEMICOLON operacao','operacao',7,'p_operacao','complador.py',157),
  ('operacao -> ID EQUALS INTEGER operador INTEGER SEMICOLON operacao','operacao',7,'p_operacao','complador.py',158),
  ('operacao -> ID EQUALS FLOATN operador INTEGER SEMICOLON operacao','operacao',7,'p_operacao','complador.py',159),
  ('operacao -> ID EQUALS INTEGER operador ID SEMICOLON operacao','operacao',7,'p_operacao','complador.py',160),
  ('operacao -> ID EQUALS FLOATN operador ID SEMICOLON operacao','operacao',7,'p_operacao','complador.py',161),
  ('operacao -> empty','operacao',1,'p_operacao','complador.py',162),
  ('tipo -> INT','tipo',1,'p_tipo','complador.py',165),
  ('tipo -> FLOAT','tipo',1,'p_tipo','complador.py',166),
  ('tipo -> CHAR','tipo',1,'p_tipo','complador.py',167),
]
