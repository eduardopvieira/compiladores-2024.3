
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ABRE_CHAVE ABRE_PARENT AND CARACTERE_ESPECIAL CARDINALIDADE CLASSE COMPARADORES DISJOINTCLASSES DISJOINTWITH EQUIVALENT_TO FECHA_CHAVE FECHA_PARENT INDIVIDUALS NAMESPACE NOME_INDIVIDUO ONLY OPERADORES OR PALAVRA_CLASS PALAVRA_RESERVADA PROPRIEDADE SOME SUBCLASSOF TIPO VALUEprograma : declaracao_classe programa\n                | declaracao_classe\n    programa : error programa\n             | error\n    \n    declaracao_classe : PALAVRA_CLASS CLASSE tipo_classe_primaria\n    \n    tipo_classe_primaria : declaracao_classe_definida\n                         | declaracao_classe_primitiva\n    \n    declaracao_classe_primitiva : SUBCLASSOF continuacao_subclassof caso_disjoint_opcional\n                                | SUBCLASSOF continuacao_subclassof\n                                | SUBCLASSOF caso_disjoint_opcional\n    \n    caso_individuals_opcional : INDIVIDUALS NOME_INDIVIDUO\n                              | INDIVIDUALS NOME_INDIVIDUO CARACTERE_ESPECIAL continuacao_individuals\n    \n    caso_individuals_opcional : INDIVIDUALS error\n                              | INDIVIDUALS error CARACTERE_ESPECIAL continuacao_individuals\n    \n    continuacao_individuals : NOME_INDIVIDUO \n                            | NOME_INDIVIDUO CARACTERE_ESPECIAL continuacao_individuals\n    \n    caso_disjoint_opcional : DISJOINTCLASSES continuacao_disjoint_opcional caso_individuals_opcional\n                           | DISJOINTWITH continuacao_disjoint_opcional caso_individuals_opcional\n    \n    continuacao_disjoint_opcional : CLASSE\n                                  | CLASSE CARACTERE_ESPECIAL continuacao_disjoint_opcional\n    continuacao_subclassof :   CLASSE caso_ands\n                                | declaracao_propriedades\n                                | CLASSE CARACTERE_ESPECIAL continuacao_subclassof\n                                | caso_ands\n                                | ABRE_PARENT declaracao_existencial FECHA_PARENT\n                                | ABRE_PARENT declaracao_existencial FECHA_PARENT AND continuacao_subclassof\n                                | ABRE_PARENT declaracao_existencial FECHA_PARENT CARACTERE_ESPECIAL continuacao_subclassof                     \n    \n    declaracao_propriedades : declaracao_existencial declaracao_propriedades\n                            | declaracao_existencial\n    \n    declaracao_existencial : PROPRIEDADE SOME CLASSE\n                           | PROPRIEDADE ONLY declaracao_classe_axioma_fechamento\n                           \n                           | PROPRIEDADE SOME NAMESPACE TIPO\n                           | PROPRIEDADE COMPARADORES CARDINALIDADE CLASSE\n\n                           | PROPRIEDADE COMPARADORES CARDINALIDADE NAMESPACE TIPO\n                           \n                           | PROPRIEDADE SOME CLASSE CARACTERE_ESPECIAL declaracao_existencial\n                           | PROPRIEDADE PROPRIEDADE SOME NAMESPACE TIPO\n\n                           | PROPRIEDADE PROPRIEDADE SOME CLASSE CARACTERE_ESPECIAL declaracao_existencial\n                           | PROPRIEDADE SOME NAMESPACE TIPO CARACTERE_ESPECIAL declaracao_existencial\n                           | PROPRIEDADE SOME NAMESPACE TIPO CARACTERE_ESPECIAL OPERADORES CARDINALIDADE CARACTERE_ESPECIAL\n                           | PROPRIEDADE PROPRIEDADE SOME NAMESPACE TIPO CARACTERE_ESPECIAL declaracao_existencial\n\n\n    \n    declaracao_classe_definida : EQUIVALENT_TO continuacao_equivalentto caso_individuals_opcional\n                               | EQUIVALENT_TO continuacao_equivalentto\n                               | EQUIVALENT_TO declaracao_classe_enumerada\n                               | EQUIVALENT_TO continuacao_equivalentto SUBCLASSOF continuacao_subclassof\n                               | continuacao_subclassof EQUIVALENT_TO continuacao_equivalentto\n    \n        continuacao_equivalentto : CLASSE OR declaracao_classe_coberta\n                                 | PALAVRA_RESERVADA CLASSE EQUIVALENT_TO CLASSE declaracao_classe_aninhada \n                                 \n                                 | CLASSE AND ABRE_PARENT declaracao_existencial casos_parentese FECHA_PARENT\n                                 | CLASSE AND declaracao_existencial casos_parentese \n                                 | CLASSE AND declaracao_existencial classes_or \n                                 | CLASSE AND declaracao_existencial classes_or caso_ands\n                                 | CLASSE AND ABRE_PARENT declaracao_existencial classes_or FECHA_PARENT \n                                 | CLASSE AND ABRE_PARENT declaracao_existencial classes_or FECHA_PARENT caso_ands\n                                 | CLASSE AND ABRE_PARENT casos_parentese declaracao_classe_aninhada FECHA_PARENT\n                                 | CLASSE AND ABRE_PARENT casos_parentese declaracao_classe_aninhada FECHA_PARENT caso_ands\n                                 \n                                 | CLASSE AND ABRE_PARENT declaracao_existencial FECHA_PARENT \n                                 \n                                 | CLASSE AND ABRE_PARENT declaracao_existencial FECHA_PARENT continuacao_equivalentto\n\n                                                                     \n    \n    declaracao_classe_aninhada : caso_ands\n    \n    caso_ands : AND casos_parentese caso_ands\n              | AND casos_sem_parentese caso_ands\n              | AND casos_parentese\n              | AND casos_sem_parentese    \n    \n    casos_parentese :  ABRE_PARENT PROPRIEDADE SOME ABRE_PARENT CLASSE classes_or FECHA_PARENT FECHA_PARENT\n                      | ABRE_PARENT declaracao_existencial FECHA_PARENT\n                      | ABRE_PARENT casos_parentese OR casos_parentese FECHA_PARENT\n                      | ABRE_PARENT casos_parentese AND casos_parentese FECHA_PARENT\n                      | ABRE_PARENT casos_parentese FECHA_PARENT\n                      | ABRE_PARENT PROPRIEDADE VALUE CLASSE FECHA_PARENT\n    \n    casos_sem_parentese :  PROPRIEDADE ONLY casos_parentese \n                        |  PROPRIEDADE PALAVRA_RESERVADA CLASSE\n                        |  declaracao_existencial\n    \n    declaracao_classe_axioma_fechamento : ABRE_PARENT classes_or_fechamento FECHA_PARENT\n                                        \n    \n    classes_or_fechamento : CLASSE OR classes_or_fechamento\n                          | CLASSE\n    \n    classes_or : OR CLASSE classes_or\n               | OR CLASSE\n               \n    \n    declaracao_classe_enumerada : ABRE_CHAVE classes_enumeradas FECHA_CHAVE\n    \n    classes_enumeradas : CLASSE CARACTERE_ESPECIAL classes_enumeradas\n                       | CLASSE\n    \n    declaracao_classe_coberta : CLASSE classes_or \n    '
    
_lr_action_items = {'error':([0,2,3,9,10,11,15,16,18,21,23,24,28,29,34,35,36,39,44,45,47,53,57,58,59,60,67,69,72,73,74,76,80,82,84,89,91,93,95,99,102,106,110,111,115,116,121,123,125,127,128,129,130,131,133,136,137,138,140,141,142,144,145,149,150,151,152,153,155,157,158,159,161,162,],[3,3,3,-5,-6,-7,-24,-22,-29,-21,-42,-43,-9,-10,-28,-61,-62,-71,-23,-41,74,-8,-45,-25,-59,-60,-30,-31,-44,-11,-13,-46,-77,-17,-18,-64,-67,-69,-70,-32,-33,-80,-49,-50,-26,-27,-36,-35,-72,-34,-15,-12,-14,-76,-56,-58,-51,-47,-68,-65,-66,-37,-38,-75,-48,-57,-52,-54,-40,-16,-53,-55,-39,-63,]),'PALAVRA_CLASS':([0,2,3,9,10,11,15,16,18,21,23,24,28,29,34,35,36,39,44,45,53,57,58,59,60,67,69,72,73,74,76,80,82,84,89,91,93,95,99,102,106,110,111,115,116,121,123,125,127,128,129,130,131,133,136,137,138,140,141,142,144,145,149,150,151,152,153,155,157,158,159,161,162,],[4,4,4,-5,-6,-7,-24,-22,-29,-21,-42,-43,-9,-10,-28,-61,-62,-71,-23,-41,-8,-45,-25,-59,-60,-30,-31,-44,-11,-13,-46,-77,-17,-18,-64,-67,-69,-70,-32,-33,-80,-49,-50,-26,-27,-36,-35,-72,-34,-15,-12,-14,-76,-56,-58,-51,-47,-68,-65,-66,-37,-38,-75,-48,-57,-52,-54,-40,-16,-53,-55,-39,-63,]),'$end':([1,2,3,5,6,9,10,11,15,16,18,21,23,24,28,29,34,35,36,39,44,45,53,57,58,59,60,67,69,72,73,74,76,80,82,84,89,91,93,95,99,102,106,110,111,115,116,121,123,125,127,128,129,130,131,133,136,137,138,140,141,142,144,145,149,150,151,152,153,155,157,158,159,161,162,],[0,-2,-4,-1,-3,-5,-6,-7,-24,-22,-29,-21,-42,-43,-9,-10,-28,-61,-62,-71,-23,-41,-8,-45,-25,-59,-60,-30,-31,-44,-11,-13,-46,-77,-17,-18,-64,-67,-69,-70,-32,-33,-80,-49,-50,-26,-27,-36,-35,-72,-34,-15,-12,-14,-76,-56,-58,-51,-47,-68,-65,-66,-37,-38,-75,-48,-57,-52,-54,-40,-16,-53,-55,-39,-63,]),'CLASSE':([4,7,12,13,22,26,27,30,31,32,41,46,48,65,66,70,71,79,81,83,85,86,87,88,94,107,117,126,133,],[7,8,25,8,8,50,52,55,55,25,67,8,75,95,97,101,102,112,52,55,8,8,67,118,101,131,139,101,25,]),'EQUIVALENT_TO':([7,14,15,16,18,21,34,35,36,39,44,50,58,59,60,67,69,89,91,93,95,99,102,115,116,121,123,125,127,140,141,142,144,145,155,161,162,],[12,32,-24,-22,-29,-21,-28,-61,-62,-71,-23,79,-25,-59,-60,-30,-31,-64,-67,-69,-70,-32,-33,-26,-27,-36,-35,-72,-34,-68,-65,-66,-37,-38,-40,-39,-63,]),'SUBCLASSOF':([7,23,35,36,39,59,60,67,69,76,89,91,93,95,99,102,106,110,111,121,123,125,127,131,133,136,137,138,140,141,142,144,145,149,150,151,152,153,155,158,159,161,162,],[13,46,-61,-62,-71,-59,-60,-30,-31,-46,-64,-67,-69,-70,-32,-33,-80,-49,-50,-36,-35,-72,-34,-76,-56,-58,-51,-47,-68,-65,-66,-37,-38,-75,-48,-57,-52,-54,-40,-53,-55,-39,-63,]),'ABRE_PARENT':([7,13,19,22,37,42,46,49,64,67,69,77,78,85,86,87,90,92,94,99,102,108,121,123,125,127,144,145,155,161,],[17,17,37,17,37,70,17,77,94,-30,-31,37,37,17,17,117,37,37,37,-32,-33,37,-36,-35,-72,-34,-37,-38,-40,-39,]),'AND':([7,8,13,22,25,35,36,39,46,58,63,67,69,85,86,89,91,93,95,99,102,109,111,112,121,123,125,127,131,140,141,142,144,145,149,152,153,155,161,162,],[19,19,19,19,49,19,19,-71,19,85,92,-30,-31,19,19,-64,-67,-69,-70,-32,-33,19,19,19,-36,-35,-72,-34,-76,-68,-65,-66,-37,-38,-75,19,19,-40,-39,-63,]),'PROPRIEDADE':([7,13,17,18,19,20,22,37,38,46,49,61,67,69,77,85,86,94,98,99,102,121,122,123,124,125,127,143,144,145,155,161,],[20,20,20,20,38,40,20,61,40,20,20,40,-30,-31,20,20,20,61,20,-32,-33,-36,20,-35,20,-72,-34,20,-37,-38,-40,-39,]),'CARACTERE_ESPECIAL':([8,52,55,58,67,73,74,97,99,121,128,156,],[22,81,83,86,98,104,105,122,124,143,148,161,]),'PALAVRA_RESERVADA':([12,32,38,133,],[26,26,65,26,]),'ABRE_CHAVE':([12,],[27,]),'DISJOINTCLASSES':([13,15,16,18,21,28,34,35,36,39,44,58,59,60,67,69,89,91,93,95,99,102,115,116,121,123,125,127,140,141,142,144,145,155,161,162,],[30,-24,-22,-29,-21,30,-28,-61,-62,-71,-23,-25,-59,-60,-30,-31,-64,-67,-69,-70,-32,-33,-26,-27,-36,-35,-72,-34,-68,-65,-66,-37,-38,-40,-39,-63,]),'DISJOINTWITH':([13,15,16,18,21,28,34,35,36,39,44,58,59,60,67,69,89,91,93,95,99,102,115,116,121,123,125,127,140,141,142,144,145,155,161,162,],[31,-24,-22,-29,-21,31,-28,-61,-62,-71,-23,-25,-59,-60,-30,-31,-64,-67,-69,-70,-32,-33,-26,-27,-36,-35,-72,-34,-68,-65,-66,-37,-38,-40,-39,-63,]),'SOME':([20,38,40,61,],[41,41,66,87,]),'ONLY':([20,38,61,],[42,64,42,]),'COMPARADORES':([20,38,61,],[43,43,43,]),'INDIVIDUALS':([23,35,36,39,54,55,56,59,60,67,69,76,89,91,93,95,99,102,106,110,111,114,121,123,125,127,131,133,136,137,138,140,141,142,144,145,149,150,151,152,153,155,158,159,161,162,],[47,-61,-62,-71,47,-19,47,-59,-60,-30,-31,-46,-64,-67,-69,-70,-32,-33,-80,-49,-50,-20,-36,-35,-72,-34,-76,-56,-58,-51,-47,-68,-65,-66,-37,-38,-75,-48,-57,-52,-54,-40,-53,-55,-39,-63,]),'OR':([25,63,67,69,75,78,89,91,99,101,102,108,121,123,125,127,131,139,140,141,142,144,145,155,161,162,],[48,90,-30,-31,107,107,-64,-67,-32,126,-33,107,-36,-35,-72,-34,107,107,-68,-65,-66,-37,-38,-40,-39,-63,]),'FECHA_PARENT':([33,35,36,39,59,60,62,63,67,69,89,91,93,95,99,100,101,102,108,118,119,120,121,123,125,127,131,132,134,135,136,140,141,142,144,145,147,149,154,155,160,161,162,],[58,-61,-62,-71,-59,-60,89,91,-30,-31,-64,-67,-69,-70,-32,125,-74,-33,133,140,141,142,-36,-35,-72,-34,-76,150,152,153,-58,-68,-65,-66,-37,-38,-73,-75,160,-40,162,-39,-63,]),'NAMESPACE':([41,66,71,87,],[68,96,103,68,]),'CARDINALIDADE':([43,146,],[71,156,]),'NOME_INDIVIDUO':([47,104,105,148,],[73,128,128,128,]),'FECHA_CHAVE':([51,52,113,],[80,-79,-78,]),'VALUE':([61,],[88,]),'TIPO':([68,96,103,],[99,121,127,]),'OPERADORES':([124,],[146,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,2,3,],[1,5,6,]),'declaracao_classe':([0,2,3,],[2,2,2,]),'tipo_classe_primaria':([7,],[9,]),'declaracao_classe_definida':([7,],[10,]),'declaracao_classe_primitiva':([7,],[11,]),'continuacao_subclassof':([7,13,22,46,85,86,],[14,28,44,72,115,116,]),'caso_ands':([7,8,13,22,35,36,46,85,86,109,111,112,152,153,],[15,21,15,15,59,60,15,15,15,136,137,136,158,159,]),'declaracao_propriedades':([7,13,18,22,46,85,86,],[16,16,34,16,16,16,16,]),'declaracao_existencial':([7,13,17,18,19,22,37,46,49,77,85,86,94,98,122,124,143,],[18,18,33,18,39,18,62,18,78,108,18,18,62,123,144,145,155,]),'continuacao_equivalentto':([12,32,133,],[23,57,151,]),'declaracao_classe_enumerada':([12,],[24,]),'caso_disjoint_opcional':([13,28,],[29,53,]),'casos_parentese':([19,37,64,77,78,90,92,94,108,],[35,63,93,109,110,119,120,63,132,]),'casos_sem_parentese':([19,],[36,]),'caso_individuals_opcional':([23,54,56,],[45,82,84,]),'classes_enumeradas':([27,81,],[51,113,]),'continuacao_disjoint_opcional':([30,31,83,],[54,56,114,]),'declaracao_classe_axioma_fechamento':([42,64,],[69,69,]),'declaracao_classe_coberta':([48,],[76,]),'classes_or_fechamento':([70,94,126,],[100,100,147,]),'classes_or':([75,78,108,131,139,],[106,111,134,149,154,]),'continuacao_individuals':([104,105,148,],[129,130,157,]),'declaracao_classe_aninhada':([109,112,],[135,138,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> declaracao_classe programa','programa',2,'p_programa','analisador_sintatico.py',116),
  ('programa -> declaracao_classe','programa',1,'p_programa','analisador_sintatico.py',117),
  ('programa -> error programa','programa',2,'p_programa_error','analisador_sintatico.py',121),
  ('programa -> error','programa',1,'p_programa_error','analisador_sintatico.py',122),
  ('declaracao_classe -> PALAVRA_CLASS CLASSE tipo_classe_primaria','declaracao_classe',3,'p_declaracao_classe','analisador_sintatico.py',128),
  ('tipo_classe_primaria -> declaracao_classe_definida','tipo_classe_primaria',1,'p_tipo_classe_primaria','analisador_sintatico.py',151),
  ('tipo_classe_primaria -> declaracao_classe_primitiva','tipo_classe_primaria',1,'p_tipo_classe_primaria','analisador_sintatico.py',152),
  ('declaracao_classe_primitiva -> SUBCLASSOF continuacao_subclassof caso_disjoint_opcional','declaracao_classe_primitiva',3,'p_declaracao_classe_primitiva','analisador_sintatico.py',161),
  ('declaracao_classe_primitiva -> SUBCLASSOF continuacao_subclassof','declaracao_classe_primitiva',2,'p_declaracao_classe_primitiva','analisador_sintatico.py',162),
  ('declaracao_classe_primitiva -> SUBCLASSOF caso_disjoint_opcional','declaracao_classe_primitiva',2,'p_declaracao_classe_primitiva','analisador_sintatico.py',163),
  ('caso_individuals_opcional -> INDIVIDUALS NOME_INDIVIDUO','caso_individuals_opcional',2,'p_caso_individuals_opcional','analisador_sintatico.py',196),
  ('caso_individuals_opcional -> INDIVIDUALS NOME_INDIVIDUO CARACTERE_ESPECIAL continuacao_individuals','caso_individuals_opcional',4,'p_caso_individuals_opcional','analisador_sintatico.py',197),
  ('caso_individuals_opcional -> INDIVIDUALS error','caso_individuals_opcional',2,'p_caso_individuals_opcional_error','analisador_sintatico.py',207),
  ('caso_individuals_opcional -> INDIVIDUALS error CARACTERE_ESPECIAL continuacao_individuals','caso_individuals_opcional',4,'p_caso_individuals_opcional_error','analisador_sintatico.py',208),
  ('continuacao_individuals -> NOME_INDIVIDUO','continuacao_individuals',1,'p_continuacao_individuals','analisador_sintatico.py',217),
  ('continuacao_individuals -> NOME_INDIVIDUO CARACTERE_ESPECIAL continuacao_individuals','continuacao_individuals',3,'p_continuacao_individuals','analisador_sintatico.py',218),
  ('caso_disjoint_opcional -> DISJOINTCLASSES continuacao_disjoint_opcional caso_individuals_opcional','caso_disjoint_opcional',3,'p_caso_disjoint_opcional','analisador_sintatico.py',235),
  ('caso_disjoint_opcional -> DISJOINTWITH continuacao_disjoint_opcional caso_individuals_opcional','caso_disjoint_opcional',3,'p_caso_disjoint_opcional','analisador_sintatico.py',236),
  ('continuacao_disjoint_opcional -> CLASSE','continuacao_disjoint_opcional',1,'p_continuacao_disjoint_opcional','analisador_sintatico.py',255),
  ('continuacao_disjoint_opcional -> CLASSE CARACTERE_ESPECIAL continuacao_disjoint_opcional','continuacao_disjoint_opcional',3,'p_continuacao_disjoint_opcional','analisador_sintatico.py',256),
  ('continuacao_subclassof -> CLASSE caso_ands','continuacao_subclassof',2,'p_continuacao_subclassof','analisador_sintatico.py',269),
  ('continuacao_subclassof -> declaracao_propriedades','continuacao_subclassof',1,'p_continuacao_subclassof','analisador_sintatico.py',270),
  ('continuacao_subclassof -> CLASSE CARACTERE_ESPECIAL continuacao_subclassof','continuacao_subclassof',3,'p_continuacao_subclassof','analisador_sintatico.py',271),
  ('continuacao_subclassof -> caso_ands','continuacao_subclassof',1,'p_continuacao_subclassof','analisador_sintatico.py',272),
  ('continuacao_subclassof -> ABRE_PARENT declaracao_existencial FECHA_PARENT','continuacao_subclassof',3,'p_continuacao_subclassof','analisador_sintatico.py',273),
  ('continuacao_subclassof -> ABRE_PARENT declaracao_existencial FECHA_PARENT AND continuacao_subclassof','continuacao_subclassof',5,'p_continuacao_subclassof','analisador_sintatico.py',274),
  ('continuacao_subclassof -> ABRE_PARENT declaracao_existencial FECHA_PARENT CARACTERE_ESPECIAL continuacao_subclassof','continuacao_subclassof',5,'p_continuacao_subclassof','analisador_sintatico.py',275),
  ('declaracao_propriedades -> declaracao_existencial declaracao_propriedades','declaracao_propriedades',2,'p_declaracao_propriedades','analisador_sintatico.py',281),
  ('declaracao_propriedades -> declaracao_existencial','declaracao_propriedades',1,'p_declaracao_propriedades','analisador_sintatico.py',282),
  ('declaracao_existencial -> PROPRIEDADE SOME CLASSE','declaracao_existencial',3,'p_declaracao_existencial','analisador_sintatico.py',287),
  ('declaracao_existencial -> PROPRIEDADE ONLY declaracao_classe_axioma_fechamento','declaracao_existencial',3,'p_declaracao_existencial','analisador_sintatico.py',288),
  ('declaracao_existencial -> PROPRIEDADE SOME NAMESPACE TIPO','declaracao_existencial',4,'p_declaracao_existencial','analisador_sintatico.py',290),
  ('declaracao_existencial -> PROPRIEDADE COMPARADORES CARDINALIDADE CLASSE','declaracao_existencial',4,'p_declaracao_existencial','analisador_sintatico.py',291),
  ('declaracao_existencial -> PROPRIEDADE COMPARADORES CARDINALIDADE NAMESPACE TIPO','declaracao_existencial',5,'p_declaracao_existencial','analisador_sintatico.py',293),
  ('declaracao_existencial -> PROPRIEDADE SOME CLASSE CARACTERE_ESPECIAL declaracao_existencial','declaracao_existencial',5,'p_declaracao_existencial','analisador_sintatico.py',295),
  ('declaracao_existencial -> PROPRIEDADE PROPRIEDADE SOME NAMESPACE TIPO','declaracao_existencial',5,'p_declaracao_existencial','analisador_sintatico.py',296),
  ('declaracao_existencial -> PROPRIEDADE PROPRIEDADE SOME CLASSE CARACTERE_ESPECIAL declaracao_existencial','declaracao_existencial',6,'p_declaracao_existencial','analisador_sintatico.py',298),
  ('declaracao_existencial -> PROPRIEDADE SOME NAMESPACE TIPO CARACTERE_ESPECIAL declaracao_existencial','declaracao_existencial',6,'p_declaracao_existencial','analisador_sintatico.py',299),
  ('declaracao_existencial -> PROPRIEDADE SOME NAMESPACE TIPO CARACTERE_ESPECIAL OPERADORES CARDINALIDADE CARACTERE_ESPECIAL','declaracao_existencial',8,'p_declaracao_existencial','analisador_sintatico.py',300),
  ('declaracao_existencial -> PROPRIEDADE PROPRIEDADE SOME NAMESPACE TIPO CARACTERE_ESPECIAL declaracao_existencial','declaracao_existencial',7,'p_declaracao_existencial','analisador_sintatico.py',301),
  ('declaracao_classe_definida -> EQUIVALENT_TO continuacao_equivalentto caso_individuals_opcional','declaracao_classe_definida',3,'p_declaracao_classe_definida','analisador_sintatico.py',368),
  ('declaracao_classe_definida -> EQUIVALENT_TO continuacao_equivalentto','declaracao_classe_definida',2,'p_declaracao_classe_definida','analisador_sintatico.py',369),
  ('declaracao_classe_definida -> EQUIVALENT_TO declaracao_classe_enumerada','declaracao_classe_definida',2,'p_declaracao_classe_definida','analisador_sintatico.py',370),
  ('declaracao_classe_definida -> EQUIVALENT_TO continuacao_equivalentto SUBCLASSOF continuacao_subclassof','declaracao_classe_definida',4,'p_declaracao_classe_definida','analisador_sintatico.py',371),
  ('declaracao_classe_definida -> continuacao_subclassof EQUIVALENT_TO continuacao_equivalentto','declaracao_classe_definida',3,'p_declaracao_classe_definida','analisador_sintatico.py',372),
  ('continuacao_equivalentto -> CLASSE OR declaracao_classe_coberta','continuacao_equivalentto',3,'p_continuacao_equivalentto','analisador_sintatico.py',382),
  ('continuacao_equivalentto -> PALAVRA_RESERVADA CLASSE EQUIVALENT_TO CLASSE declaracao_classe_aninhada','continuacao_equivalentto',5,'p_continuacao_equivalentto','analisador_sintatico.py',383),
  ('continuacao_equivalentto -> CLASSE AND ABRE_PARENT declaracao_existencial casos_parentese FECHA_PARENT','continuacao_equivalentto',6,'p_continuacao_equivalentto','analisador_sintatico.py',385),
  ('continuacao_equivalentto -> CLASSE AND declaracao_existencial casos_parentese','continuacao_equivalentto',4,'p_continuacao_equivalentto','analisador_sintatico.py',386),
  ('continuacao_equivalentto -> CLASSE AND declaracao_existencial classes_or','continuacao_equivalentto',4,'p_continuacao_equivalentto','analisador_sintatico.py',387),
  ('continuacao_equivalentto -> CLASSE AND declaracao_existencial classes_or caso_ands','continuacao_equivalentto',5,'p_continuacao_equivalentto','analisador_sintatico.py',388),
  ('continuacao_equivalentto -> CLASSE AND ABRE_PARENT declaracao_existencial classes_or FECHA_PARENT','continuacao_equivalentto',6,'p_continuacao_equivalentto','analisador_sintatico.py',389),
  ('continuacao_equivalentto -> CLASSE AND ABRE_PARENT declaracao_existencial classes_or FECHA_PARENT caso_ands','continuacao_equivalentto',7,'p_continuacao_equivalentto','analisador_sintatico.py',390),
  ('continuacao_equivalentto -> CLASSE AND ABRE_PARENT casos_parentese declaracao_classe_aninhada FECHA_PARENT','continuacao_equivalentto',6,'p_continuacao_equivalentto','analisador_sintatico.py',391),
  ('continuacao_equivalentto -> CLASSE AND ABRE_PARENT casos_parentese declaracao_classe_aninhada FECHA_PARENT caso_ands','continuacao_equivalentto',7,'p_continuacao_equivalentto','analisador_sintatico.py',392),
  ('continuacao_equivalentto -> CLASSE AND ABRE_PARENT declaracao_existencial FECHA_PARENT','continuacao_equivalentto',5,'p_continuacao_equivalentto','analisador_sintatico.py',394),
  ('continuacao_equivalentto -> CLASSE AND ABRE_PARENT declaracao_existencial FECHA_PARENT continuacao_equivalentto','continuacao_equivalentto',6,'p_continuacao_equivalentto','analisador_sintatico.py',396),
  ('declaracao_classe_aninhada -> caso_ands','declaracao_classe_aninhada',1,'p_declaracao_classe_aninhada','analisador_sintatico.py',404),
  ('caso_ands -> AND casos_parentese caso_ands','caso_ands',3,'p_caso_ands','analisador_sintatico.py',411),
  ('caso_ands -> AND casos_sem_parentese caso_ands','caso_ands',3,'p_caso_ands','analisador_sintatico.py',412),
  ('caso_ands -> AND casos_parentese','caso_ands',2,'p_caso_ands','analisador_sintatico.py',413),
  ('caso_ands -> AND casos_sem_parentese','caso_ands',2,'p_caso_ands','analisador_sintatico.py',414),
  ('casos_parentese -> ABRE_PARENT PROPRIEDADE SOME ABRE_PARENT CLASSE classes_or FECHA_PARENT FECHA_PARENT','casos_parentese',8,'p_casos_parentese','analisador_sintatico.py',421),
  ('casos_parentese -> ABRE_PARENT declaracao_existencial FECHA_PARENT','casos_parentese',3,'p_casos_parentese','analisador_sintatico.py',422),
  ('casos_parentese -> ABRE_PARENT casos_parentese OR casos_parentese FECHA_PARENT','casos_parentese',5,'p_casos_parentese','analisador_sintatico.py',423),
  ('casos_parentese -> ABRE_PARENT casos_parentese AND casos_parentese FECHA_PARENT','casos_parentese',5,'p_casos_parentese','analisador_sintatico.py',424),
  ('casos_parentese -> ABRE_PARENT casos_parentese FECHA_PARENT','casos_parentese',3,'p_casos_parentese','analisador_sintatico.py',425),
  ('casos_parentese -> ABRE_PARENT PROPRIEDADE VALUE CLASSE FECHA_PARENT','casos_parentese',5,'p_casos_parentese','analisador_sintatico.py',426),
  ('casos_sem_parentese -> PROPRIEDADE ONLY casos_parentese','casos_sem_parentese',3,'p_casos_sem_parentese','analisador_sintatico.py',431),
  ('casos_sem_parentese -> PROPRIEDADE PALAVRA_RESERVADA CLASSE','casos_sem_parentese',3,'p_casos_sem_parentese','analisador_sintatico.py',432),
  ('casos_sem_parentese -> declaracao_existencial','casos_sem_parentese',1,'p_casos_sem_parentese','analisador_sintatico.py',433),
  ('declaracao_classe_axioma_fechamento -> ABRE_PARENT classes_or_fechamento FECHA_PARENT','declaracao_classe_axioma_fechamento',3,'p_declaracao_classe_axioma_fechamento','analisador_sintatico.py',440),
  ('classes_or_fechamento -> CLASSE OR classes_or_fechamento','classes_or_fechamento',3,'p_classes_or_fechamento','analisador_sintatico.py',448),
  ('classes_or_fechamento -> CLASSE','classes_or_fechamento',1,'p_classes_or_fechamento','analisador_sintatico.py',449),
  ('classes_or -> OR CLASSE classes_or','classes_or',3,'p_classes_or','analisador_sintatico.py',459),
  ('classes_or -> OR CLASSE','classes_or',2,'p_classes_or','analisador_sintatico.py',460),
  ('declaracao_classe_enumerada -> ABRE_CHAVE classes_enumeradas FECHA_CHAVE','declaracao_classe_enumerada',3,'p_declaracao_classe_enumerada','analisador_sintatico.py',467),
  ('classes_enumeradas -> CLASSE CARACTERE_ESPECIAL classes_enumeradas','classes_enumeradas',3,'p_classes_enumeradas','analisador_sintatico.py',474),
  ('classes_enumeradas -> CLASSE','classes_enumeradas',1,'p_classes_enumeradas','analisador_sintatico.py',475),
  ('declaracao_classe_coberta -> CLASSE classes_or','declaracao_classe_coberta',2,'p_declaracao_classe_coberta','analisador_sintatico.py',482),
]
