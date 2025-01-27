
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ABRE_CHAVE ABRE_COLCHETE ABRE_PARENT AND CARACTERE_ESPECIAL CARDINALIDADE CLASSE COMPARADORES DISJOINTCLASSES DISJOINTWITH EQUIVALENT_TO FECHA_CHAVE FECHA_COLCHETE FECHA_PARENT INDIVIDUALS NAMESPACE NOME_INDIVIDUO ONLY OPERADORES OR PALAVRA_CLASS PALAVRA_RESERVADA PROPRIEDADE SOME SUBCLASSOF TIPO TIPO_NUMERICO VALUEprograma : declaracao_classe programa\n                | declaracao_classe\n    programa : error programa\n             | error\n    \n    declaracao_classe : PALAVRA_CLASS CLASSE tipo_classe_primaria\n    \n    tipo_classe_primaria : declaracao_classe_definida\n                         | declaracao_classe_primitiva\n    \n    declaracao_classe_primitiva : SUBCLASSOF continuacao_subclassof caso_disjoint_opcional\n                                | SUBCLASSOF continuacao_subclassof\n                                | SUBCLASSOF caso_disjoint_opcional\n    \n    caso_individuals_opcional : INDIVIDUALS NOME_INDIVIDUO\n                              | INDIVIDUALS NOME_INDIVIDUO CARACTERE_ESPECIAL continuacao_individuals\n    \n    caso_individuals_opcional : INDIVIDUALS error\n                              | INDIVIDUALS error CARACTERE_ESPECIAL continuacao_individuals\n    \n    continuacao_individuals : NOME_INDIVIDUO \n                            | NOME_INDIVIDUO CARACTERE_ESPECIAL continuacao_individuals\n    \n    caso_disjoint_opcional : DISJOINTCLASSES continuacao_disjoint_opcional caso_individuals_opcional\n                           | DISJOINTWITH continuacao_disjoint_opcional caso_individuals_opcional\n    \n    continuacao_disjoint_opcional : CLASSE\n                                  | CLASSE CARACTERE_ESPECIAL continuacao_disjoint_opcional\n    continuacao_subclassof :   CLASSE caso_ands\n                                | declaracao_propriedades\n                                | CLASSE CARACTERE_ESPECIAL continuacao_subclassof\n                                | caso_ands\n                                | ABRE_PARENT declaracao_existencial FECHA_PARENT\n                                | ABRE_PARENT declaracao_existencial FECHA_PARENT AND continuacao_subclassof\n                                | ABRE_PARENT declaracao_existencial FECHA_PARENT CARACTERE_ESPECIAL continuacao_subclassof                     \n    \n    declaracao_propriedades : declaracao_existencial declaracao_propriedades\n                            | declaracao_existencial\n    \n    declaracao_existencial : PROPRIEDADE SOME CLASSE\n                           | PROPRIEDADE ONLY declaracao_classe_axioma_fechamento\n                           \n                           | PROPRIEDADE SOME NAMESPACE TIPO\n                           | PROPRIEDADE COMPARADORES CARDINALIDADE CLASSE\n                           \n                           | PROPRIEDADE COMPARADORES CARDINALIDADE NAMESPACE TIPO\n                           | PROPRIEDADE PROPRIEDADE SOME NAMESPACE TIPO\n                           | PROPRIEDADE SOME CLASSE CARACTERE_ESPECIAL declaracao_existencial\n\n                           | PROPRIEDADE SOME NAMESPACE TIPO ABRE_COLCHETE OPERADORES\n                           | PROPRIEDADE SOME NAMESPACE TIPO CARACTERE_ESPECIAL declaracao_existencial\n                           | PROPRIEDADE PROPRIEDADE SOME CLASSE CARACTERE_ESPECIAL declaracao_existencial\n\n\n                           | PROPRIEDADE PROPRIEDADE SOME NAMESPACE TIPO CARACTERE_ESPECIAL declaracao_existencial\n                           \n                           \n                           | PROPRIEDADE SOME NAMESPACE TIPO_NUMERICO ABRE_COLCHETE OPERADORES CARDINALIDADE FECHA_COLCHETE\n                           | PROPRIEDADE SOME NAMESPACE TIPO CARACTERE_ESPECIAL OPERADORES CARDINALIDADE CARACTERE_ESPECIAL\n\n                                                      \n                           | PROPRIEDADE SOME NAMESPACE TIPO_NUMERICO ABRE_COLCHETE OPERADORES CARDINALIDADE FECHA_COLCHETE CARACTERE_ESPECIAL declaracao_existencial\n\n                           \n                           | PROPRIEDADE COMPARADORES CARDINALIDADE NAMESPACE TIPO_NUMERICO ABRE_COLCHETE OPERADORES CARDINALIDADE FECHA_COLCHETE\n                           \n\n    \n    declaracao_classe_definida : EQUIVALENT_TO continuacao_equivalentto caso_individuals_opcional\n                               | EQUIVALENT_TO continuacao_equivalentto\n                               | EQUIVALENT_TO declaracao_classe_enumerada\n                               | EQUIVALENT_TO continuacao_equivalentto SUBCLASSOF continuacao_subclassof\n                               | continuacao_subclassof EQUIVALENT_TO continuacao_equivalentto\n    \n        continuacao_equivalentto : CLASSE OR declaracao_classe_coberta\n                                 | PALAVRA_RESERVADA CLASSE EQUIVALENT_TO CLASSE declaracao_classe_aninhada \n                                 | CLASSE AND ABRE_PARENT declaracao_existencial casos_parentese FECHA_PARENT\n                                 | CLASSE AND declaracao_existencial casos_parentese \n                                 | CLASSE AND declaracao_existencial classes_or \n                                 | CLASSE AND declaracao_existencial classes_or caso_ands\n                                 | CLASSE AND ABRE_PARENT declaracao_existencial classes_or FECHA_PARENT \n                                 | CLASSE AND ABRE_PARENT declaracao_existencial classes_or FECHA_PARENT caso_ands\n                                 | CLASSE AND ABRE_PARENT casos_parentese declaracao_classe_aninhada FECHA_PARENT\n                                 | CLASSE AND ABRE_PARENT casos_parentese declaracao_classe_aninhada FECHA_PARENT caso_ands\n                                 | CLASSE AND ABRE_PARENT declaracao_existencial FECHA_PARENT \n                                 | CLASSE AND ABRE_PARENT declaracao_existencial FECHA_PARENT continuacao_equivalentto\n    \n    declaracao_classe_aninhada : caso_ands\n    \n    caso_ands : AND casos_parentese caso_ands\n              | AND casos_sem_parentese caso_ands\n              | AND casos_parentese\n              | AND casos_sem_parentese    \n    \n    casos_parentese :  ABRE_PARENT PROPRIEDADE SOME ABRE_PARENT CLASSE classes_or FECHA_PARENT FECHA_PARENT\n                      | ABRE_PARENT declaracao_existencial FECHA_PARENT\n                      | ABRE_PARENT casos_parentese OR casos_parentese FECHA_PARENT\n                      | ABRE_PARENT casos_parentese AND casos_parentese FECHA_PARENT\n                      | ABRE_PARENT casos_parentese FECHA_PARENT\n                      | ABRE_PARENT PROPRIEDADE VALUE CLASSE FECHA_PARENT\n    \n    casos_sem_parentese :  PROPRIEDADE ONLY casos_parentese \n                        |  PROPRIEDADE PALAVRA_RESERVADA CLASSE\n                        |  declaracao_existencial\n    \n    declaracao_classe_axioma_fechamento : ABRE_PARENT classes_or_fechamento FECHA_PARENT\n                                        \n    \n    classes_or_fechamento : CLASSE OR classes_or_fechamento\n                          | CLASSE\n    \n    classes_or : OR CLASSE classes_or\n               | OR CLASSE\n               \n    \n    declaracao_classe_enumerada : ABRE_CHAVE classes_enumeradas FECHA_CHAVE\n    \n    classes_enumeradas : CLASSE CARACTERE_ESPECIAL classes_enumeradas\n                       | CLASSE\n    \n    declaracao_classe_coberta : CLASSE classes_or \n    '
    
_lr_action_items = {'error':([0,2,3,9,10,11,15,16,18,21,23,24,28,29,34,35,36,39,44,45,47,53,57,58,59,60,67,69,72,73,74,76,80,82,84,89,91,93,95,99,103,107,111,112,116,117,122,124,128,130,132,133,134,135,137,140,141,142,144,145,146,148,149,150,156,157,158,159,160,162,166,167,168,170,171,173,175,176,],[3,3,3,-5,-6,-7,-24,-22,-29,-21,-46,-47,-9,-10,-28,-65,-66,-75,-23,-45,74,-8,-49,-25,-63,-64,-30,-31,-48,-11,-13,-50,-81,-17,-18,-68,-71,-73,-74,-32,-33,-84,-53,-54,-26,-27,-35,-36,-76,-34,-15,-12,-14,-80,-60,-62,-55,-51,-72,-69,-70,-39,-37,-38,-79,-52,-61,-56,-58,-40,-16,-57,-59,-42,-41,-67,-44,-43,]),'PALAVRA_CLASS':([0,2,3,9,10,11,15,16,18,21,23,24,28,29,34,35,36,39,44,45,53,57,58,59,60,67,69,72,73,74,76,80,82,84,89,91,93,95,99,103,107,111,112,116,117,122,124,128,130,132,133,134,135,137,140,141,142,144,145,146,148,149,150,156,157,158,159,160,162,166,167,168,170,171,173,175,176,],[4,4,4,-5,-6,-7,-24,-22,-29,-21,-46,-47,-9,-10,-28,-65,-66,-75,-23,-45,-8,-49,-25,-63,-64,-30,-31,-48,-11,-13,-50,-81,-17,-18,-68,-71,-73,-74,-32,-33,-84,-53,-54,-26,-27,-35,-36,-76,-34,-15,-12,-14,-80,-60,-62,-55,-51,-72,-69,-70,-39,-37,-38,-79,-52,-61,-56,-58,-40,-16,-57,-59,-42,-41,-67,-44,-43,]),'$end':([1,2,3,5,6,9,10,11,15,16,18,21,23,24,28,29,34,35,36,39,44,45,53,57,58,59,60,67,69,72,73,74,76,80,82,84,89,91,93,95,99,103,107,111,112,116,117,122,124,128,130,132,133,134,135,137,140,141,142,144,145,146,148,149,150,156,157,158,159,160,162,166,167,168,170,171,173,175,176,],[0,-2,-4,-1,-3,-5,-6,-7,-24,-22,-29,-21,-46,-47,-9,-10,-28,-65,-66,-75,-23,-45,-8,-49,-25,-63,-64,-30,-31,-48,-11,-13,-50,-81,-17,-18,-68,-71,-73,-74,-32,-33,-84,-53,-54,-26,-27,-35,-36,-76,-34,-15,-12,-14,-80,-60,-62,-55,-51,-72,-69,-70,-39,-37,-38,-79,-52,-61,-56,-58,-40,-16,-57,-59,-42,-41,-67,-44,-43,]),'CLASSE':([4,7,12,13,22,26,27,30,31,32,41,46,48,65,66,70,71,79,81,83,85,86,87,88,94,108,118,129,137,],[7,8,25,8,8,50,52,55,55,25,67,8,75,95,97,102,103,113,52,55,8,8,67,119,102,135,143,102,25,]),'EQUIVALENT_TO':([7,14,15,16,18,21,34,35,36,39,44,50,58,59,60,67,69,89,91,93,95,99,103,116,117,122,124,128,130,144,145,146,148,149,150,162,170,171,173,175,176,],[12,32,-24,-22,-29,-21,-28,-65,-66,-75,-23,79,-25,-63,-64,-30,-31,-68,-71,-73,-74,-32,-33,-26,-27,-35,-36,-76,-34,-72,-69,-70,-39,-37,-38,-40,-42,-41,-67,-44,-43,]),'SUBCLASSOF':([7,23,35,36,39,59,60,67,69,76,89,91,93,95,99,103,107,111,112,122,124,128,130,135,137,140,141,142,144,145,146,148,149,150,156,157,158,159,160,162,167,168,170,171,173,175,176,],[13,46,-65,-66,-75,-63,-64,-30,-31,-50,-68,-71,-73,-74,-32,-33,-84,-53,-54,-35,-36,-76,-34,-80,-60,-62,-55,-51,-72,-69,-70,-39,-37,-38,-79,-52,-61,-56,-58,-40,-57,-59,-42,-41,-67,-44,-43,]),'ABRE_PARENT':([7,13,19,22,37,42,46,49,64,67,69,77,78,85,86,87,90,92,94,99,103,109,122,124,128,130,148,149,150,162,170,171,175,176,],[17,17,37,17,37,70,17,77,94,-30,-31,37,37,17,17,118,37,37,37,-32,-33,37,-35,-36,-76,-34,-39,-37,-38,-40,-42,-41,-44,-43,]),'AND':([7,8,13,22,25,35,36,39,46,58,63,67,69,85,86,89,91,93,95,99,103,110,112,113,122,124,128,130,135,144,145,146,148,149,150,156,159,160,162,170,171,173,175,176,],[19,19,19,19,49,19,19,-75,19,85,92,-30,-31,19,19,-68,-71,-73,-74,-32,-33,19,19,19,-35,-36,-76,-34,-80,-72,-69,-70,-39,-37,-38,-79,19,19,-40,-42,-41,-67,-44,-43,]),'PROPRIEDADE':([7,13,17,18,19,20,22,37,38,46,49,61,67,69,77,85,86,94,98,99,103,122,123,124,126,128,130,147,148,149,150,162,170,171,174,175,176,],[20,20,20,20,38,40,20,61,40,20,20,40,-30,-31,20,20,20,61,20,-32,-33,-35,20,-36,20,-76,-34,20,-39,-37,-38,-40,-42,-41,20,-44,-43,]),'CARACTERE_ESPECIAL':([8,52,55,58,67,73,74,97,99,122,132,163,171,],[22,81,83,86,98,105,106,123,126,147,155,170,174,]),'PALAVRA_RESERVADA':([12,32,38,137,],[26,26,65,26,]),'ABRE_CHAVE':([12,],[27,]),'DISJOINTCLASSES':([13,15,16,18,21,28,34,35,36,39,44,58,59,60,67,69,89,91,93,95,99,103,116,117,122,124,128,130,144,145,146,148,149,150,162,170,171,173,175,176,],[30,-24,-22,-29,-21,30,-28,-65,-66,-75,-23,-25,-63,-64,-30,-31,-68,-71,-73,-74,-32,-33,-26,-27,-35,-36,-76,-34,-72,-69,-70,-39,-37,-38,-40,-42,-41,-67,-44,-43,]),'DISJOINTWITH':([13,15,16,18,21,28,34,35,36,39,44,58,59,60,67,69,89,91,93,95,99,103,116,117,122,124,128,130,144,145,146,148,149,150,162,170,171,173,175,176,],[31,-24,-22,-29,-21,31,-28,-65,-66,-75,-23,-25,-63,-64,-30,-31,-68,-71,-73,-74,-32,-33,-26,-27,-35,-36,-76,-34,-72,-69,-70,-39,-37,-38,-40,-42,-41,-67,-44,-43,]),'SOME':([20,38,40,61,],[41,41,66,87,]),'ONLY':([20,38,61,],[42,64,42,]),'COMPARADORES':([20,38,61,],[43,43,43,]),'INDIVIDUALS':([23,35,36,39,54,55,56,59,60,67,69,76,89,91,93,95,99,103,107,111,112,115,122,124,128,130,135,137,140,141,142,144,145,146,148,149,150,156,157,158,159,160,162,167,168,170,171,173,175,176,],[47,-65,-66,-75,47,-19,47,-63,-64,-30,-31,-50,-68,-71,-73,-74,-32,-33,-84,-53,-54,-20,-35,-36,-76,-34,-80,-60,-62,-55,-51,-72,-69,-70,-39,-37,-38,-79,-52,-61,-56,-58,-40,-57,-59,-42,-41,-67,-44,-43,]),'OR':([25,63,67,69,75,78,89,91,99,102,103,109,122,124,128,130,135,143,144,145,146,148,149,150,162,170,171,173,175,176,],[48,90,-30,-31,108,108,-68,-71,-32,129,-33,108,-35,-36,-76,-34,108,108,-72,-69,-70,-39,-37,-38,-40,-42,-41,-67,-44,-43,]),'FECHA_PARENT':([33,35,36,39,59,60,62,63,67,69,89,91,93,95,99,101,102,103,109,119,120,121,122,124,128,130,135,136,138,139,140,144,145,146,148,149,150,153,156,161,162,169,170,171,173,175,176,],[58,-65,-66,-75,-63,-64,89,91,-30,-31,-68,-71,-73,-74,-32,128,-78,-33,137,144,145,146,-35,-36,-76,-34,-80,157,159,160,-62,-72,-69,-70,-39,-37,-38,-77,-79,169,-40,173,-42,-41,-67,-44,-43,]),'NAMESPACE':([41,66,71,87,],[68,96,104,68,]),'CARDINALIDADE':([43,151,152,165,],[71,163,164,172,]),'NOME_INDIVIDUO':([47,105,106,155,],[73,132,132,132,]),'FECHA_CHAVE':([51,52,114,],[80,-83,-82,]),'VALUE':([61,],[88,]),'TIPO':([68,96,104,],[99,122,130,]),'TIPO_NUMERICO':([68,104,],[100,131,]),'ABRE_COLCHETE':([99,100,131,],[125,127,154,]),'OPERADORES':([125,126,127,154,],[149,151,152,165,]),'FECHA_COLCHETE':([164,172,],[171,175,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,2,3,],[1,5,6,]),'declaracao_classe':([0,2,3,],[2,2,2,]),'tipo_classe_primaria':([7,],[9,]),'declaracao_classe_definida':([7,],[10,]),'declaracao_classe_primitiva':([7,],[11,]),'continuacao_subclassof':([7,13,22,46,85,86,],[14,28,44,72,116,117,]),'caso_ands':([7,8,13,22,35,36,46,85,86,110,112,113,159,160,],[15,21,15,15,59,60,15,15,15,140,141,140,167,168,]),'declaracao_propriedades':([7,13,18,22,46,85,86,],[16,16,34,16,16,16,16,]),'declaracao_existencial':([7,13,17,18,19,22,37,46,49,77,85,86,94,98,123,126,147,174,],[18,18,33,18,39,18,62,18,78,109,18,18,62,124,148,150,162,176,]),'continuacao_equivalentto':([12,32,137,],[23,57,158,]),'declaracao_classe_enumerada':([12,],[24,]),'caso_disjoint_opcional':([13,28,],[29,53,]),'casos_parentese':([19,37,64,77,78,90,92,94,109,],[35,63,93,110,111,120,121,63,136,]),'casos_sem_parentese':([19,],[36,]),'caso_individuals_opcional':([23,54,56,],[45,82,84,]),'classes_enumeradas':([27,81,],[51,114,]),'continuacao_disjoint_opcional':([30,31,83,],[54,56,115,]),'declaracao_classe_axioma_fechamento':([42,64,],[69,69,]),'declaracao_classe_coberta':([48,],[76,]),'classes_or_fechamento':([70,94,129,],[101,101,153,]),'classes_or':([75,78,109,135,143,],[107,112,138,156,161,]),'continuacao_individuals':([105,106,155,],[133,134,166,]),'declaracao_classe_aninhada':([110,113,],[139,142,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> declaracao_classe programa','programa',2,'p_programa','analisador_semantico.py',122),
  ('programa -> declaracao_classe','programa',1,'p_programa','analisador_semantico.py',123),
  ('programa -> error programa','programa',2,'p_programa_error','analisador_semantico.py',147),
  ('programa -> error','programa',1,'p_programa_error','analisador_semantico.py',148),
  ('declaracao_classe -> PALAVRA_CLASS CLASSE tipo_classe_primaria','declaracao_classe',3,'p_declaracao_classe','analisador_semantico.py',154),
  ('tipo_classe_primaria -> declaracao_classe_definida','tipo_classe_primaria',1,'p_tipo_classe_primaria','analisador_semantico.py',198),
  ('tipo_classe_primaria -> declaracao_classe_primitiva','tipo_classe_primaria',1,'p_tipo_classe_primaria','analisador_semantico.py',199),
  ('declaracao_classe_primitiva -> SUBCLASSOF continuacao_subclassof caso_disjoint_opcional','declaracao_classe_primitiva',3,'p_declaracao_classe_primitiva','analisador_semantico.py',208),
  ('declaracao_classe_primitiva -> SUBCLASSOF continuacao_subclassof','declaracao_classe_primitiva',2,'p_declaracao_classe_primitiva','analisador_semantico.py',209),
  ('declaracao_classe_primitiva -> SUBCLASSOF caso_disjoint_opcional','declaracao_classe_primitiva',2,'p_declaracao_classe_primitiva','analisador_semantico.py',210),
  ('caso_individuals_opcional -> INDIVIDUALS NOME_INDIVIDUO','caso_individuals_opcional',2,'p_caso_individuals_opcional','analisador_semantico.py',220),
  ('caso_individuals_opcional -> INDIVIDUALS NOME_INDIVIDUO CARACTERE_ESPECIAL continuacao_individuals','caso_individuals_opcional',4,'p_caso_individuals_opcional','analisador_semantico.py',221),
  ('caso_individuals_opcional -> INDIVIDUALS error','caso_individuals_opcional',2,'p_caso_individuals_opcional_error','analisador_semantico.py',226),
  ('caso_individuals_opcional -> INDIVIDUALS error CARACTERE_ESPECIAL continuacao_individuals','caso_individuals_opcional',4,'p_caso_individuals_opcional_error','analisador_semantico.py',227),
  ('continuacao_individuals -> NOME_INDIVIDUO','continuacao_individuals',1,'p_continuacao_individuals','analisador_semantico.py',236),
  ('continuacao_individuals -> NOME_INDIVIDUO CARACTERE_ESPECIAL continuacao_individuals','continuacao_individuals',3,'p_continuacao_individuals','analisador_semantico.py',237),
  ('caso_disjoint_opcional -> DISJOINTCLASSES continuacao_disjoint_opcional caso_individuals_opcional','caso_disjoint_opcional',3,'p_caso_disjoint_opcional','analisador_semantico.py',244),
  ('caso_disjoint_opcional -> DISJOINTWITH continuacao_disjoint_opcional caso_individuals_opcional','caso_disjoint_opcional',3,'p_caso_disjoint_opcional','analisador_semantico.py',245),
  ('continuacao_disjoint_opcional -> CLASSE','continuacao_disjoint_opcional',1,'p_continuacao_disjoint_opcional','analisador_semantico.py',264),
  ('continuacao_disjoint_opcional -> CLASSE CARACTERE_ESPECIAL continuacao_disjoint_opcional','continuacao_disjoint_opcional',3,'p_continuacao_disjoint_opcional','analisador_semantico.py',265),
  ('continuacao_subclassof -> CLASSE caso_ands','continuacao_subclassof',2,'p_continuacao_subclassof','analisador_semantico.py',278),
  ('continuacao_subclassof -> declaracao_propriedades','continuacao_subclassof',1,'p_continuacao_subclassof','analisador_semantico.py',279),
  ('continuacao_subclassof -> CLASSE CARACTERE_ESPECIAL continuacao_subclassof','continuacao_subclassof',3,'p_continuacao_subclassof','analisador_semantico.py',280),
  ('continuacao_subclassof -> caso_ands','continuacao_subclassof',1,'p_continuacao_subclassof','analisador_semantico.py',281),
  ('continuacao_subclassof -> ABRE_PARENT declaracao_existencial FECHA_PARENT','continuacao_subclassof',3,'p_continuacao_subclassof','analisador_semantico.py',282),
  ('continuacao_subclassof -> ABRE_PARENT declaracao_existencial FECHA_PARENT AND continuacao_subclassof','continuacao_subclassof',5,'p_continuacao_subclassof','analisador_semantico.py',283),
  ('continuacao_subclassof -> ABRE_PARENT declaracao_existencial FECHA_PARENT CARACTERE_ESPECIAL continuacao_subclassof','continuacao_subclassof',5,'p_continuacao_subclassof','analisador_semantico.py',284),
  ('declaracao_propriedades -> declaracao_existencial declaracao_propriedades','declaracao_propriedades',2,'p_declaracao_propriedades','analisador_semantico.py',290),
  ('declaracao_propriedades -> declaracao_existencial','declaracao_propriedades',1,'p_declaracao_propriedades','analisador_semantico.py',291),
  ('declaracao_existencial -> PROPRIEDADE SOME CLASSE','declaracao_existencial',3,'p_declaracao_existencial','analisador_semantico.py',296),
  ('declaracao_existencial -> PROPRIEDADE ONLY declaracao_classe_axioma_fechamento','declaracao_existencial',3,'p_declaracao_existencial','analisador_semantico.py',297),
  ('declaracao_existencial -> PROPRIEDADE SOME NAMESPACE TIPO','declaracao_existencial',4,'p_declaracao_existencial','analisador_semantico.py',299),
  ('declaracao_existencial -> PROPRIEDADE COMPARADORES CARDINALIDADE CLASSE','declaracao_existencial',4,'p_declaracao_existencial','analisador_semantico.py',300),
  ('declaracao_existencial -> PROPRIEDADE COMPARADORES CARDINALIDADE NAMESPACE TIPO','declaracao_existencial',5,'p_declaracao_existencial','analisador_semantico.py',302),
  ('declaracao_existencial -> PROPRIEDADE PROPRIEDADE SOME NAMESPACE TIPO','declaracao_existencial',5,'p_declaracao_existencial','analisador_semantico.py',303),
  ('declaracao_existencial -> PROPRIEDADE SOME CLASSE CARACTERE_ESPECIAL declaracao_existencial','declaracao_existencial',5,'p_declaracao_existencial','analisador_semantico.py',304),
  ('declaracao_existencial -> PROPRIEDADE SOME NAMESPACE TIPO ABRE_COLCHETE OPERADORES','declaracao_existencial',6,'p_declaracao_existencial','analisador_semantico.py',306),
  ('declaracao_existencial -> PROPRIEDADE SOME NAMESPACE TIPO CARACTERE_ESPECIAL declaracao_existencial','declaracao_existencial',6,'p_declaracao_existencial','analisador_semantico.py',307),
  ('declaracao_existencial -> PROPRIEDADE PROPRIEDADE SOME CLASSE CARACTERE_ESPECIAL declaracao_existencial','declaracao_existencial',6,'p_declaracao_existencial','analisador_semantico.py',308),
  ('declaracao_existencial -> PROPRIEDADE PROPRIEDADE SOME NAMESPACE TIPO CARACTERE_ESPECIAL declaracao_existencial','declaracao_existencial',7,'p_declaracao_existencial','analisador_semantico.py',311),
  ('declaracao_existencial -> PROPRIEDADE SOME NAMESPACE TIPO_NUMERICO ABRE_COLCHETE OPERADORES CARDINALIDADE FECHA_COLCHETE','declaracao_existencial',8,'p_declaracao_existencial','analisador_semantico.py',314),
  ('declaracao_existencial -> PROPRIEDADE SOME NAMESPACE TIPO CARACTERE_ESPECIAL OPERADORES CARDINALIDADE CARACTERE_ESPECIAL','declaracao_existencial',8,'p_declaracao_existencial','analisador_semantico.py',315),
  ('declaracao_existencial -> PROPRIEDADE SOME NAMESPACE TIPO_NUMERICO ABRE_COLCHETE OPERADORES CARDINALIDADE FECHA_COLCHETE CARACTERE_ESPECIAL declaracao_existencial','declaracao_existencial',10,'p_declaracao_existencial','analisador_semantico.py',318),
  ('declaracao_existencial -> PROPRIEDADE COMPARADORES CARDINALIDADE NAMESPACE TIPO_NUMERICO ABRE_COLCHETE OPERADORES CARDINALIDADE FECHA_COLCHETE','declaracao_existencial',9,'p_declaracao_existencial','analisador_semantico.py',321),
  ('declaracao_classe_definida -> EQUIVALENT_TO continuacao_equivalentto caso_individuals_opcional','declaracao_classe_definida',3,'p_declaracao_classe_definida','analisador_semantico.py',397),
  ('declaracao_classe_definida -> EQUIVALENT_TO continuacao_equivalentto','declaracao_classe_definida',2,'p_declaracao_classe_definida','analisador_semantico.py',398),
  ('declaracao_classe_definida -> EQUIVALENT_TO declaracao_classe_enumerada','declaracao_classe_definida',2,'p_declaracao_classe_definida','analisador_semantico.py',399),
  ('declaracao_classe_definida -> EQUIVALENT_TO continuacao_equivalentto SUBCLASSOF continuacao_subclassof','declaracao_classe_definida',4,'p_declaracao_classe_definida','analisador_semantico.py',400),
  ('declaracao_classe_definida -> continuacao_subclassof EQUIVALENT_TO continuacao_equivalentto','declaracao_classe_definida',3,'p_declaracao_classe_definida','analisador_semantico.py',401),
  ('continuacao_equivalentto -> CLASSE OR declaracao_classe_coberta','continuacao_equivalentto',3,'p_continuacao_equivalentto','analisador_semantico.py',412),
  ('continuacao_equivalentto -> PALAVRA_RESERVADA CLASSE EQUIVALENT_TO CLASSE declaracao_classe_aninhada','continuacao_equivalentto',5,'p_continuacao_equivalentto','analisador_semantico.py',413),
  ('continuacao_equivalentto -> CLASSE AND ABRE_PARENT declaracao_existencial casos_parentese FECHA_PARENT','continuacao_equivalentto',6,'p_continuacao_equivalentto','analisador_semantico.py',414),
  ('continuacao_equivalentto -> CLASSE AND declaracao_existencial casos_parentese','continuacao_equivalentto',4,'p_continuacao_equivalentto','analisador_semantico.py',415),
  ('continuacao_equivalentto -> CLASSE AND declaracao_existencial classes_or','continuacao_equivalentto',4,'p_continuacao_equivalentto','analisador_semantico.py',416),
  ('continuacao_equivalentto -> CLASSE AND declaracao_existencial classes_or caso_ands','continuacao_equivalentto',5,'p_continuacao_equivalentto','analisador_semantico.py',417),
  ('continuacao_equivalentto -> CLASSE AND ABRE_PARENT declaracao_existencial classes_or FECHA_PARENT','continuacao_equivalentto',6,'p_continuacao_equivalentto','analisador_semantico.py',418),
  ('continuacao_equivalentto -> CLASSE AND ABRE_PARENT declaracao_existencial classes_or FECHA_PARENT caso_ands','continuacao_equivalentto',7,'p_continuacao_equivalentto','analisador_semantico.py',419),
  ('continuacao_equivalentto -> CLASSE AND ABRE_PARENT casos_parentese declaracao_classe_aninhada FECHA_PARENT','continuacao_equivalentto',6,'p_continuacao_equivalentto','analisador_semantico.py',420),
  ('continuacao_equivalentto -> CLASSE AND ABRE_PARENT casos_parentese declaracao_classe_aninhada FECHA_PARENT caso_ands','continuacao_equivalentto',7,'p_continuacao_equivalentto','analisador_semantico.py',421),
  ('continuacao_equivalentto -> CLASSE AND ABRE_PARENT declaracao_existencial FECHA_PARENT','continuacao_equivalentto',5,'p_continuacao_equivalentto','analisador_semantico.py',422),
  ('continuacao_equivalentto -> CLASSE AND ABRE_PARENT declaracao_existencial FECHA_PARENT continuacao_equivalentto','continuacao_equivalentto',6,'p_continuacao_equivalentto','analisador_semantico.py',423),
  ('declaracao_classe_aninhada -> caso_ands','declaracao_classe_aninhada',1,'p_declaracao_classe_aninhada','analisador_semantico.py',428),
  ('caso_ands -> AND casos_parentese caso_ands','caso_ands',3,'p_caso_ands','analisador_semantico.py',433),
  ('caso_ands -> AND casos_sem_parentese caso_ands','caso_ands',3,'p_caso_ands','analisador_semantico.py',434),
  ('caso_ands -> AND casos_parentese','caso_ands',2,'p_caso_ands','analisador_semantico.py',435),
  ('caso_ands -> AND casos_sem_parentese','caso_ands',2,'p_caso_ands','analisador_semantico.py',436),
  ('casos_parentese -> ABRE_PARENT PROPRIEDADE SOME ABRE_PARENT CLASSE classes_or FECHA_PARENT FECHA_PARENT','casos_parentese',8,'p_casos_parentese','analisador_semantico.py',441),
  ('casos_parentese -> ABRE_PARENT declaracao_existencial FECHA_PARENT','casos_parentese',3,'p_casos_parentese','analisador_semantico.py',442),
  ('casos_parentese -> ABRE_PARENT casos_parentese OR casos_parentese FECHA_PARENT','casos_parentese',5,'p_casos_parentese','analisador_semantico.py',443),
  ('casos_parentese -> ABRE_PARENT casos_parentese AND casos_parentese FECHA_PARENT','casos_parentese',5,'p_casos_parentese','analisador_semantico.py',444),
  ('casos_parentese -> ABRE_PARENT casos_parentese FECHA_PARENT','casos_parentese',3,'p_casos_parentese','analisador_semantico.py',445),
  ('casos_parentese -> ABRE_PARENT PROPRIEDADE VALUE CLASSE FECHA_PARENT','casos_parentese',5,'p_casos_parentese','analisador_semantico.py',446),
  ('casos_sem_parentese -> PROPRIEDADE ONLY casos_parentese','casos_sem_parentese',3,'p_casos_sem_parentese','analisador_semantico.py',451),
  ('casos_sem_parentese -> PROPRIEDADE PALAVRA_RESERVADA CLASSE','casos_sem_parentese',3,'p_casos_sem_parentese','analisador_semantico.py',452),
  ('casos_sem_parentese -> declaracao_existencial','casos_sem_parentese',1,'p_casos_sem_parentese','analisador_semantico.py',453),
  ('declaracao_classe_axioma_fechamento -> ABRE_PARENT classes_or_fechamento FECHA_PARENT','declaracao_classe_axioma_fechamento',3,'p_declaracao_classe_axioma_fechamento','analisador_semantico.py',460),
  ('classes_or_fechamento -> CLASSE OR classes_or_fechamento','classes_or_fechamento',3,'p_classes_or_fechamento','analisador_semantico.py',468),
  ('classes_or_fechamento -> CLASSE','classes_or_fechamento',1,'p_classes_or_fechamento','analisador_semantico.py',469),
  ('classes_or -> OR CLASSE classes_or','classes_or',3,'p_classes_or','analisador_semantico.py',479),
  ('classes_or -> OR CLASSE','classes_or',2,'p_classes_or','analisador_semantico.py',480),
  ('declaracao_classe_enumerada -> ABRE_CHAVE classes_enumeradas FECHA_CHAVE','declaracao_classe_enumerada',3,'p_declaracao_classe_enumerada','analisador_semantico.py',487),
  ('classes_enumeradas -> CLASSE CARACTERE_ESPECIAL classes_enumeradas','classes_enumeradas',3,'p_classes_enumeradas','analisador_semantico.py',493),
  ('classes_enumeradas -> CLASSE','classes_enumeradas',1,'p_classes_enumeradas','analisador_semantico.py',494),
  ('declaracao_classe_coberta -> CLASSE classes_or','declaracao_classe_coberta',2,'p_declaracao_classe_coberta','analisador_semantico.py',501),
]