
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ABRE_CHAVE ABRE_PARENT AND CARACTERE_ESPECIAL CARDINALIDADE CLASSE DISJOINTCLASSES EQUIVALENT_TO FECHA_CHAVE FECHA_PARENT INDIVIDUALS NAMESPACE NOME_INDIVIDUO ONLY OPERADORES OR PALAVRA_RESERVADA PROPRIEDADE SOME SUBCLASSOF TIPOprograma : tipo_classe_primaria programa\n                | tipo_classe_primaria\n    tipo_classe_primaria : declaracao_classe_definida\n                         | declaracao_classe_primitiva\n    \n    tipo_classe_secundaria : declaracao_classe_aninhada\n                          | declaracao_classe_enumerada\n                          | declaracao_classe_coberta\n                          | declaracao_classe_axioma_fechamento\n    \n    declaracao_classe_primitiva : PALAVRA_RESERVADA CLASSE caso_subclassof caso_disjoint_opcional caso_individuals_opcional \n    \n    caso_subclassof : SUBCLASSOF PROPRIEDADE SOME CLASSE\n                   | SUBCLASSOF PROPRIEDADE SOME NAMESPACE TIPO\n                   | SUBCLASSOF PROPRIEDADE SOME CLASSE CARACTERE_ESPECIAL continuacao_subclassof \n                   | SUBCLASSOF PROPRIEDADE SOME NAMESPACE TIPO CARACTERE_ESPECIAL continuacao_subclassof\n                   | SUBCLASSOF declaracao_classe_axioma_fechamento\n    \n    caso_individuals_opcional : NOME_INDIVIDUO CARACTERE_ESPECIAL caso_individuals_opcional\n                              | NOME_INDIVIDUO\n                              | INDIVIDUALS NOME_INDIVIDUO\n                              | INDIVIDUALS NOME_INDIVIDUO CARACTERE_ESPECIAL caso_individuals_opcional\n                              |\n    \n    caso_disjoint_opcional : CLASSE CARACTERE_ESPECIAL caso_disjoint_opcional\n                         |  CLASSE\n                         |  DISJOINTCLASSES CLASSE \n                         |  DISJOINTCLASSES CLASSE CARACTERE_ESPECIAL caso_disjoint_opcional\n                         |\n    continuacao_subclassof : PROPRIEDADE SOME CLASSE\n                   | PROPRIEDADE SOME NAMESPACE TIPO\n                   | PROPRIEDADE SOME CLASSE CARACTERE_ESPECIAL continuacao_subclassof \n                   | PROPRIEDADE SOME NAMESPACE TIPO CARACTERE_ESPECIAL continuacao_subclassof\n    \n    declaracao_classe_definida : PALAVRA_RESERVADA CLASSE EQUIVALENT_TO estrutura_definida\n    \n    estrutura_definida : caso_simples_opcional estrutura_definida\n                       | tipo_classe_secundaria estrutura_definida\n                       | caso_individuals_opcional estrutura_definida\n                       |\n    \n    caso_simples_opcional : CLASSE caso_ands\n    \n    declaracao_classe_aninhada : caso_ands\n    \n    caso_ands : AND restricoes_aninhada caso_ands\n              | AND restricoes_aninhada\n    \n    restricoes_aninhada : ABRE_PARENT PROPRIEDADE SOME CLASSE FECHA_PARENT\n                        | ABRE_PARENT PROPRIEDADE SOME ABRE_PARENT classes_and FECHA_PARENT\n                        | ABRE_PARENT PROPRIEDADE SOME CLASSE restricoes_aninhada\n                        | ABRE_PARENT PROPRIEDADE SOME CARDINALIDADE CLASSE FECHA_PARENT restricoes_aninhada\n                        | ABRE_PARENT PROPRIEDADE SOME NAMESPACE TIPO CARACTERE_ESPECIAL OPERADORES CARDINALIDADE CARACTERE_ESPECIAL FECHA_PARENT\n                        | ABRE_PARENT PROPRIEDADE SOME NAMESPACE TIPO CARACTERE_ESPECIAL OPERADORES CARDINALIDADE CARACTERE_ESPECIAL FECHA_PARENT CARACTERE_ESPECIAL restricoes_aninhada\n                        | ABRE_PARENT restricoes_aninhada FECHA_PARENT\n    classes_and : CLASSE AND classes_and\n                | CLASSE\n    declaracao_classe_axioma_fechamento : CLASSE CARACTERE_ESPECIAL restricoes_axioma_fechamento \n    restricoes_axioma_fechamento : PROPRIEDADE SOME CLASSE\n                                | PROPRIEDADE SOME CLASSE CARACTERE_ESPECIAL restricoes_axioma_fechamento\n                                | PROPRIEDADE ONLY ABRE_PARENT classes_or FECHA_PARENT\n    \n    classes_or : CLASSE OR classes_or\n              | CLASSE \n    \n    declaracao_classe_enumerada : ABRE_CHAVE classes_enumeradas FECHA_CHAVE\n    \n    classes_enumeradas : CLASSE CARACTERE_ESPECIAL classes_enumeradas\n                      | CLASSE\n    \n    declaracao_classe_coberta : classes_or\n    '
    
_lr_action_items = {'PALAVRA_RESERVADA':([0,2,3,4,8,9,11,12,13,14,15,16,17,18,19,20,21,24,26,27,31,32,35,36,37,38,39,42,44,45,46,48,50,51,52,53,54,56,59,60,61,65,68,69,71,72,79,85,86,90,91,92,93,97,100,103,105,108,109,111,],[5,5,-3,-4,-19,-24,-52,-29,-19,-19,-19,-35,-5,-6,-7,-8,-16,-56,-21,-19,-14,-34,-30,-31,-32,-19,-17,-37,-24,-9,-22,-47,-52,-51,-15,-19,-53,-36,-20,-24,-10,-18,-44,-23,-11,-48,-12,-38,-40,-13,-49,-50,-39,-25,-41,-26,-27,-28,-42,-43,]),'$end':([1,2,3,4,6,8,9,11,12,13,14,15,16,17,18,19,20,21,24,26,27,31,32,35,36,37,38,39,42,44,45,46,48,50,51,52,53,54,56,59,60,61,65,68,69,71,72,79,85,86,90,91,92,93,97,100,103,105,108,109,111,],[0,-2,-3,-4,-1,-19,-24,-52,-29,-19,-19,-19,-35,-5,-6,-7,-8,-16,-56,-21,-19,-14,-34,-30,-31,-32,-19,-17,-37,-24,-9,-22,-47,-52,-51,-15,-19,-53,-36,-20,-24,-10,-18,-44,-23,-11,-48,-12,-38,-40,-13,-49,-50,-39,-25,-41,-26,-27,-28,-42,-43,]),'CLASSE':([5,8,9,10,11,13,14,15,16,17,18,19,20,21,23,24,28,31,32,34,38,39,42,44,47,48,50,51,52,53,54,55,56,60,61,63,65,67,68,71,72,73,74,76,79,85,86,89,90,91,92,93,94,97,100,103,105,108,109,111,],[7,11,26,30,-52,11,11,11,-35,-5,-6,-7,-8,-16,41,-56,46,-14,-34,50,-19,-17,-37,26,61,-47,-52,-51,-15,-19,-53,41,-36,26,-10,72,-18,75,-44,-11,-48,50,84,87,-12,-38,-40,97,-13,-49,-50,-39,84,-25,-41,-26,-27,-28,-42,-43,]),'EQUIVALENT_TO':([7,],[8,]),'SUBCLASSOF':([7,],[10,]),'NOME_INDIVIDUO':([8,9,11,13,14,15,16,17,18,19,20,21,22,24,26,27,31,32,38,39,42,44,46,48,50,51,52,53,54,56,59,60,61,65,68,69,71,72,79,85,86,90,91,92,93,97,100,103,105,108,109,111,],[21,-24,-52,21,21,21,-35,-5,-6,-7,-8,-16,39,-56,-21,21,-14,-34,21,-17,-37,-24,-22,-47,-52,-51,-15,21,-53,-36,-20,-24,-10,-18,-44,-23,-11,-48,-12,-38,-40,-13,-49,-50,-39,-25,-41,-26,-27,-28,-42,-43,]),'INDIVIDUALS':([8,9,11,13,14,15,16,17,18,19,20,21,24,26,27,31,32,38,39,42,44,46,48,50,51,52,53,54,56,59,60,61,65,68,69,71,72,79,85,86,90,91,92,93,97,100,103,105,108,109,111,],[22,-24,-52,22,22,22,-35,-5,-6,-7,-8,-16,-56,-21,22,-14,-34,22,-17,-37,-24,-22,-47,-52,-51,-15,22,-53,-36,-20,-24,-10,-18,-44,-23,-11,-48,-12,-38,-40,-13,-49,-50,-39,-25,-41,-26,-27,-28,-42,-43,]),'ABRE_CHAVE':([8,11,13,14,15,16,17,18,19,20,21,24,32,38,39,42,48,50,51,52,53,54,56,65,68,72,85,86,91,92,93,100,109,111,],[23,-52,23,23,23,-35,-5,-6,-7,-8,-16,-56,-34,-19,-17,-37,-47,-52,-51,-15,-19,-53,-36,-18,-44,-48,-38,-40,-49,-50,-39,-41,-42,-43,]),'AND':([8,11,13,14,15,16,17,18,19,20,21,24,32,38,39,42,48,50,51,52,53,54,56,65,68,72,84,85,86,91,92,93,100,109,111,],[25,25,25,25,25,-35,-5,-6,-7,-8,-16,-56,-34,-19,-17,25,-47,-52,-51,-15,-19,-53,-36,-18,-44,-48,94,-38,-40,-49,-50,-39,-41,-42,-43,]),'DISJOINTCLASSES':([9,31,44,48,60,61,71,72,79,90,91,92,97,103,105,108,],[28,-14,28,-47,28,-10,-11,-48,-12,-13,-49,-50,-25,-26,-27,-28,]),'PROPRIEDADE':([10,33,43,70,80,81,102,106,],[29,49,57,78,78,49,78,78,]),'CARACTERE_ESPECIAL':([11,21,26,30,39,41,46,61,71,72,88,97,103,104,109,],[33,38,44,33,53,55,60,70,80,81,96,102,106,107,110,]),'OR':([11,50,],[34,34,]),'ABRE_PARENT':([25,43,64,67,75,95,110,],[43,43,73,74,43,43,43,]),'SOME':([29,49,57,78,],[47,63,67,89,]),'FECHA_CHAVE':([40,41,66,],[54,-55,-54,]),'NAMESPACE':([47,67,89,],[62,77,98,]),'ONLY':([49,],[64,]),'FECHA_PARENT':([50,51,58,68,75,82,83,84,85,86,87,93,99,100,107,109,111,],[-52,-51,68,-44,85,92,93,-46,-38,-40,95,-39,-45,-41,109,-42,-43,]),'TIPO':([62,77,98,],[71,88,103,]),'CARDINALIDADE':([67,101,],[76,104,]),'OPERADORES':([96,],[101,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,2,],[1,6,]),'tipo_classe_primaria':([0,2,],[2,2,]),'declaracao_classe_definida':([0,2,],[3,3,]),'declaracao_classe_primitiva':([0,2,],[4,4,]),'caso_subclassof':([7,],[9,]),'estrutura_definida':([8,13,14,15,],[12,35,36,37,]),'caso_simples_opcional':([8,13,14,15,],[13,13,13,13,]),'tipo_classe_secundaria':([8,13,14,15,],[14,14,14,14,]),'caso_individuals_opcional':([8,13,14,15,27,38,53,],[15,15,15,15,45,52,65,]),'caso_ands':([8,11,13,14,15,42,],[16,32,16,16,16,56,]),'declaracao_classe_aninhada':([8,13,14,15,],[17,17,17,17,]),'declaracao_classe_enumerada':([8,13,14,15,],[18,18,18,18,]),'declaracao_classe_coberta':([8,13,14,15,],[19,19,19,19,]),'declaracao_classe_axioma_fechamento':([8,10,13,14,15,],[20,31,20,20,20,]),'classes_or':([8,13,14,15,34,73,],[24,24,24,24,51,82,]),'caso_disjoint_opcional':([9,44,60,],[27,59,69,]),'classes_enumeradas':([23,55,],[40,66,]),'restricoes_aninhada':([25,43,75,95,110,],[42,58,86,100,111,]),'restricoes_axioma_fechamento':([33,81,],[48,91,]),'continuacao_subclassof':([70,80,102,106,],[79,90,105,108,]),'classes_and':([74,94,],[83,99,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> tipo_classe_primaria programa','programa',2,'p_programa','analisadorLexico.py',113),
  ('programa -> tipo_classe_primaria','programa',1,'p_programa','analisadorLexico.py',114),
  ('tipo_classe_primaria -> declaracao_classe_definida','tipo_classe_primaria',1,'p_tipo_classe_primaria','analisadorLexico.py',120),
  ('tipo_classe_primaria -> declaracao_classe_primitiva','tipo_classe_primaria',1,'p_tipo_classe_primaria','analisadorLexico.py',121),
  ('tipo_classe_secundaria -> declaracao_classe_aninhada','tipo_classe_secundaria',1,'p_tipo_classe_secundaria','analisadorLexico.py',127),
  ('tipo_classe_secundaria -> declaracao_classe_enumerada','tipo_classe_secundaria',1,'p_tipo_classe_secundaria','analisadorLexico.py',128),
  ('tipo_classe_secundaria -> declaracao_classe_coberta','tipo_classe_secundaria',1,'p_tipo_classe_secundaria','analisadorLexico.py',129),
  ('tipo_classe_secundaria -> declaracao_classe_axioma_fechamento','tipo_classe_secundaria',1,'p_tipo_classe_secundaria','analisadorLexico.py',130),
  ('declaracao_classe_primitiva -> PALAVRA_RESERVADA CLASSE caso_subclassof caso_disjoint_opcional caso_individuals_opcional','declaracao_classe_primitiva',5,'p_declaracao_classe_primitiva','analisadorLexico.py',138),
  ('caso_subclassof -> SUBCLASSOF PROPRIEDADE SOME CLASSE','caso_subclassof',4,'p_caso_subclassof','analisadorLexico.py',144),
  ('caso_subclassof -> SUBCLASSOF PROPRIEDADE SOME NAMESPACE TIPO','caso_subclassof',5,'p_caso_subclassof','analisadorLexico.py',145),
  ('caso_subclassof -> SUBCLASSOF PROPRIEDADE SOME CLASSE CARACTERE_ESPECIAL continuacao_subclassof','caso_subclassof',6,'p_caso_subclassof','analisadorLexico.py',146),
  ('caso_subclassof -> SUBCLASSOF PROPRIEDADE SOME NAMESPACE TIPO CARACTERE_ESPECIAL continuacao_subclassof','caso_subclassof',7,'p_caso_subclassof','analisadorLexico.py',147),
  ('caso_subclassof -> SUBCLASSOF declaracao_classe_axioma_fechamento','caso_subclassof',2,'p_caso_subclassof','analisadorLexico.py',148),
  ('caso_individuals_opcional -> NOME_INDIVIDUO CARACTERE_ESPECIAL caso_individuals_opcional','caso_individuals_opcional',3,'p_caso_individuals_opcional','analisadorLexico.py',162),
  ('caso_individuals_opcional -> NOME_INDIVIDUO','caso_individuals_opcional',1,'p_caso_individuals_opcional','analisadorLexico.py',163),
  ('caso_individuals_opcional -> INDIVIDUALS NOME_INDIVIDUO','caso_individuals_opcional',2,'p_caso_individuals_opcional','analisadorLexico.py',164),
  ('caso_individuals_opcional -> INDIVIDUALS NOME_INDIVIDUO CARACTERE_ESPECIAL caso_individuals_opcional','caso_individuals_opcional',4,'p_caso_individuals_opcional','analisadorLexico.py',165),
  ('caso_individuals_opcional -> <empty>','caso_individuals_opcional',0,'p_caso_individuals_opcional','analisadorLexico.py',166),
  ('caso_disjoint_opcional -> CLASSE CARACTERE_ESPECIAL caso_disjoint_opcional','caso_disjoint_opcional',3,'p_caso_disjoint_opcional','analisadorLexico.py',172),
  ('caso_disjoint_opcional -> CLASSE','caso_disjoint_opcional',1,'p_caso_disjoint_opcional','analisadorLexico.py',173),
  ('caso_disjoint_opcional -> DISJOINTCLASSES CLASSE','caso_disjoint_opcional',2,'p_caso_disjoint_opcional','analisadorLexico.py',174),
  ('caso_disjoint_opcional -> DISJOINTCLASSES CLASSE CARACTERE_ESPECIAL caso_disjoint_opcional','caso_disjoint_opcional',4,'p_caso_disjoint_opcional','analisadorLexico.py',175),
  ('caso_disjoint_opcional -> <empty>','caso_disjoint_opcional',0,'p_caso_disjoint_opcional','analisadorLexico.py',176),
  ('continuacao_subclassof -> PROPRIEDADE SOME CLASSE','continuacao_subclassof',3,'p_continuacao_subclassof','analisadorLexico.py',181),
  ('continuacao_subclassof -> PROPRIEDADE SOME NAMESPACE TIPO','continuacao_subclassof',4,'p_continuacao_subclassof','analisadorLexico.py',182),
  ('continuacao_subclassof -> PROPRIEDADE SOME CLASSE CARACTERE_ESPECIAL continuacao_subclassof','continuacao_subclassof',5,'p_continuacao_subclassof','analisadorLexico.py',183),
  ('continuacao_subclassof -> PROPRIEDADE SOME NAMESPACE TIPO CARACTERE_ESPECIAL continuacao_subclassof','continuacao_subclassof',6,'p_continuacao_subclassof','analisadorLexico.py',184),
  ('declaracao_classe_definida -> PALAVRA_RESERVADA CLASSE EQUIVALENT_TO estrutura_definida','declaracao_classe_definida',4,'p_declaracao_classe_definida','analisadorLexico.py',192),
  ('estrutura_definida -> caso_simples_opcional estrutura_definida','estrutura_definida',2,'p_estrutura_definida','analisadorLexico.py',198),
  ('estrutura_definida -> tipo_classe_secundaria estrutura_definida','estrutura_definida',2,'p_estrutura_definida','analisadorLexico.py',199),
  ('estrutura_definida -> caso_individuals_opcional estrutura_definida','estrutura_definida',2,'p_estrutura_definida','analisadorLexico.py',200),
  ('estrutura_definida -> <empty>','estrutura_definida',0,'p_estrutura_definida','analisadorLexico.py',201),
  ('caso_simples_opcional -> CLASSE caso_ands','caso_simples_opcional',2,'p_caso_simples_opcional','analisadorLexico.py',207),
  ('declaracao_classe_aninhada -> caso_ands','declaracao_classe_aninhada',1,'p_declaracao_classe_aninhada','analisadorLexico.py',213),
  ('caso_ands -> AND restricoes_aninhada caso_ands','caso_ands',3,'p_caso_ands','analisadorLexico.py',219),
  ('caso_ands -> AND restricoes_aninhada','caso_ands',2,'p_caso_ands','analisadorLexico.py',220),
  ('restricoes_aninhada -> ABRE_PARENT PROPRIEDADE SOME CLASSE FECHA_PARENT','restricoes_aninhada',5,'p_restricoes_aninhada','analisadorLexico.py',226),
  ('restricoes_aninhada -> ABRE_PARENT PROPRIEDADE SOME ABRE_PARENT classes_and FECHA_PARENT','restricoes_aninhada',6,'p_restricoes_aninhada','analisadorLexico.py',227),
  ('restricoes_aninhada -> ABRE_PARENT PROPRIEDADE SOME CLASSE restricoes_aninhada','restricoes_aninhada',5,'p_restricoes_aninhada','analisadorLexico.py',228),
  ('restricoes_aninhada -> ABRE_PARENT PROPRIEDADE SOME CARDINALIDADE CLASSE FECHA_PARENT restricoes_aninhada','restricoes_aninhada',7,'p_restricoes_aninhada','analisadorLexico.py',229),
  ('restricoes_aninhada -> ABRE_PARENT PROPRIEDADE SOME NAMESPACE TIPO CARACTERE_ESPECIAL OPERADORES CARDINALIDADE CARACTERE_ESPECIAL FECHA_PARENT','restricoes_aninhada',10,'p_restricoes_aninhada','analisadorLexico.py',230),
  ('restricoes_aninhada -> ABRE_PARENT PROPRIEDADE SOME NAMESPACE TIPO CARACTERE_ESPECIAL OPERADORES CARDINALIDADE CARACTERE_ESPECIAL FECHA_PARENT CARACTERE_ESPECIAL restricoes_aninhada','restricoes_aninhada',12,'p_restricoes_aninhada','analisadorLexico.py',231),
  ('restricoes_aninhada -> ABRE_PARENT restricoes_aninhada FECHA_PARENT','restricoes_aninhada',3,'p_restricoes_aninhada','analisadorLexico.py',232),
  ('classes_and -> CLASSE AND classes_and','classes_and',3,'p_classes_and','analisadorLexico.py',237),
  ('classes_and -> CLASSE','classes_and',1,'p_classes_and','analisadorLexico.py',238),
  ('declaracao_classe_axioma_fechamento -> CLASSE CARACTERE_ESPECIAL restricoes_axioma_fechamento','declaracao_classe_axioma_fechamento',3,'p_declaracao_classe_axioma_fechamento','analisadorLexico.py',243),
  ('restricoes_axioma_fechamento -> PROPRIEDADE SOME CLASSE','restricoes_axioma_fechamento',3,'p_restricoes_axioma_fechamento','analisadorLexico.py',248),
  ('restricoes_axioma_fechamento -> PROPRIEDADE SOME CLASSE CARACTERE_ESPECIAL restricoes_axioma_fechamento','restricoes_axioma_fechamento',5,'p_restricoes_axioma_fechamento','analisadorLexico.py',249),
  ('restricoes_axioma_fechamento -> PROPRIEDADE ONLY ABRE_PARENT classes_or FECHA_PARENT','restricoes_axioma_fechamento',5,'p_restricoes_axioma_fechamento','analisadorLexico.py',250),
  ('classes_or -> CLASSE OR classes_or','classes_or',3,'p_classes_or','analisadorLexico.py',256),
  ('classes_or -> CLASSE','classes_or',1,'p_classes_or','analisadorLexico.py',257),
  ('declaracao_classe_enumerada -> ABRE_CHAVE classes_enumeradas FECHA_CHAVE','declaracao_classe_enumerada',3,'p_declaracao_classe_enumerada','analisadorLexico.py',264),
  ('classes_enumeradas -> CLASSE CARACTERE_ESPECIAL classes_enumeradas','classes_enumeradas',3,'p_classes_enumeradas','analisadorLexico.py',270),
  ('classes_enumeradas -> CLASSE','classes_enumeradas',1,'p_classes_enumeradas','analisadorLexico.py',271),
  ('declaracao_classe_coberta -> classes_or','declaracao_classe_coberta',1,'p_declaracao_classe_coberta','analisadorLexico.py',278),
]
