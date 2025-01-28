
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ABRE_CHAVE ABRE_COLCHETE ABRE_PARENT AND CARACTERE_ESPECIAL CARDINALIDADE CLASSE COMPARADORES DISJOINTCLASSES DISJOINTWITH EQUIVALENT_TO FECHA_CHAVE FECHA_COLCHETE FECHA_PARENT INDIVIDUALS NAMESPACE NOME_INDIVIDUO ONLY OPERADORES OR PALAVRA_CLASS PALAVRA_RESERVADA PROPRIEDADE SOME SUBCLASSOF TIPO TIPO_NUMERICO VALUEprograma : declaracao_classe programa\n                | declaracao_classe\n    declaracao_classe : PALAVRA_CLASS CLASSE tipo_classe_primaria\n    \n    declaracao_classe : PALAVRA_CLASS error tipo_classe_primaria\n                      | error CLASSE tipo_classe_primaria        \n    \n    tipo_classe_primaria : declaracao_classe_definida\n                         | declaracao_classe_primitiva\n    \n    declaracao_classe_primitiva : SUBCLASSOF continuacao_subclassof caso_disjoint_opcional\n                                | SUBCLASSOF continuacao_subclassof\n                                | SUBCLASSOF caso_disjoint_opcional\n    \n    caso_individuals_opcional : INDIVIDUALS NOME_INDIVIDUO\n                              | INDIVIDUALS NOME_INDIVIDUO CARACTERE_ESPECIAL continuacao_individuals\n    \n    caso_individuals_opcional : INDIVIDUALS error\n                              | INDIVIDUALS error CARACTERE_ESPECIAL continuacao_individuals\n    \n    continuacao_individuals : NOME_INDIVIDUO \n                            | NOME_INDIVIDUO CARACTERE_ESPECIAL continuacao_individuals\n    \n    caso_disjoint_opcional : DISJOINTCLASSES continuacao_disjoint_opcional caso_individuals_opcional\n                           | DISJOINTWITH continuacao_disjoint_opcional caso_individuals_opcional\n    \n    continuacao_disjoint_opcional : CLASSE\n                                  | CLASSE CARACTERE_ESPECIAL continuacao_disjoint_opcional\n    continuacao_subclassof :   CLASSE caso_ands\n                                | declaracao_propriedades\n                                | CLASSE CARACTERE_ESPECIAL continuacao_subclassof\n                                | caso_ands\n                                | ABRE_PARENT declaracao_existencial FECHA_PARENT\n                                | ABRE_PARENT declaracao_existencial FECHA_PARENT AND continuacao_subclassof\n                                | ABRE_PARENT declaracao_existencial FECHA_PARENT CARACTERE_ESPECIAL continuacao_subclassof                     \n    \n    declaracao_propriedades : declaracao_existencial declaracao_propriedades\n                            | declaracao_existencial\n    \n    declaracao_existencial : PROPRIEDADE SOME CLASSE\n                           | PROPRIEDADE ONLY declaracao_classe_axioma_fechamento\n                           \n                           | PROPRIEDADE SOME NAMESPACE TIPO\n                           | PROPRIEDADE COMPARADORES CARDINALIDADE CLASSE\n                           \n                           | PROPRIEDADE COMPARADORES CARDINALIDADE NAMESPACE TIPO\n                           | PROPRIEDADE PROPRIEDADE SOME NAMESPACE TIPO\n                           | PROPRIEDADE SOME CLASSE CARACTERE_ESPECIAL declaracao_existencial\n\n                           | PROPRIEDADE SOME NAMESPACE TIPO ABRE_COLCHETE OPERADORES\n                           | PROPRIEDADE SOME NAMESPACE TIPO CARACTERE_ESPECIAL declaracao_existencial\n                           | PROPRIEDADE PROPRIEDADE SOME CLASSE CARACTERE_ESPECIAL declaracao_existencial\n\n\n                           | PROPRIEDADE PROPRIEDADE SOME NAMESPACE TIPO CARACTERE_ESPECIAL declaracao_existencial\n                           \n                           \n                           | PROPRIEDADE SOME NAMESPACE TIPO_NUMERICO ABRE_COLCHETE OPERADORES CARDINALIDADE FECHA_COLCHETE\n                           | PROPRIEDADE SOME NAMESPACE TIPO CARACTERE_ESPECIAL OPERADORES CARDINALIDADE CARACTERE_ESPECIAL\n\n                                                      \n                           | PROPRIEDADE SOME NAMESPACE TIPO_NUMERICO ABRE_COLCHETE OPERADORES CARDINALIDADE FECHA_COLCHETE CARACTERE_ESPECIAL declaracao_existencial\n\n                           \n                           | PROPRIEDADE COMPARADORES CARDINALIDADE NAMESPACE TIPO_NUMERICO ABRE_COLCHETE OPERADORES CARDINALIDADE FECHA_COLCHETE\n                           \n\n    \n    declaracao_classe_definida : EQUIVALENT_TO continuacao_equivalentto caso_individuals_opcional\n                               | EQUIVALENT_TO continuacao_equivalentto\n                               | EQUIVALENT_TO declaracao_classe_enumerada\n                               | EQUIVALENT_TO continuacao_equivalentto SUBCLASSOF continuacao_subclassof\n                               | continuacao_subclassof EQUIVALENT_TO continuacao_equivalentto\n    \n        continuacao_equivalentto : CLASSE OR declaracao_classe_coberta\n                                 | PALAVRA_RESERVADA CLASSE EQUIVALENT_TO CLASSE declaracao_classe_aninhada \n                                 | CLASSE AND ABRE_PARENT declaracao_existencial casos_parentese FECHA_PARENT\n                                 | CLASSE AND declaracao_existencial casos_parentese \n                                 | CLASSE AND declaracao_existencial classes_or \n                                 | CLASSE AND declaracao_existencial classes_or caso_ands\n                                 | CLASSE AND ABRE_PARENT declaracao_existencial classes_or FECHA_PARENT \n                                 | CLASSE AND ABRE_PARENT declaracao_existencial classes_or FECHA_PARENT caso_ands\n                                 | CLASSE AND ABRE_PARENT casos_parentese declaracao_classe_aninhada FECHA_PARENT\n                                 | CLASSE AND ABRE_PARENT casos_parentese declaracao_classe_aninhada FECHA_PARENT caso_ands\n                                 | CLASSE AND ABRE_PARENT declaracao_existencial FECHA_PARENT \n                                 | CLASSE AND ABRE_PARENT declaracao_existencial FECHA_PARENT continuacao_equivalentto\n    \n    declaracao_classe_aninhada : caso_ands\n    \n    caso_ands : AND casos_parentese caso_ands\n              | AND casos_sem_parentese caso_ands\n              | AND casos_parentese\n              | AND casos_sem_parentese    \n    \n    casos_parentese :  ABRE_PARENT PROPRIEDADE SOME ABRE_PARENT CLASSE classes_or FECHA_PARENT FECHA_PARENT\n                      | ABRE_PARENT declaracao_existencial FECHA_PARENT\n                      | ABRE_PARENT casos_parentese OR casos_parentese FECHA_PARENT\n                      | ABRE_PARENT casos_parentese AND casos_parentese FECHA_PARENT\n                      | ABRE_PARENT casos_parentese FECHA_PARENT\n                      | ABRE_PARENT PROPRIEDADE VALUE CLASSE FECHA_PARENT\n    \n    casos_sem_parentese :  PROPRIEDADE ONLY casos_parentese \n                        |  PROPRIEDADE PALAVRA_RESERVADA CLASSE\n                        |  declaracao_existencial\n    \n    declaracao_classe_axioma_fechamento : ABRE_PARENT classes_or_fechamento FECHA_PARENT\n                                        \n    \n    classes_or_fechamento : CLASSE OR classes_or_fechamento\n                          | CLASSE\n    \n    classes_or : OR CLASSE classes_or\n               | OR CLASSE\n               \n    \n    declaracao_classe_enumerada : ABRE_CHAVE classes_enumeradas FECHA_CHAVE\n    \n    classes_enumeradas : CLASSE CARACTERE_ESPECIAL classes_enumeradas\n                       | CLASSE\n    \n    declaracao_classe_coberta : CLASSE classes_or \n    '
    
_lr_action_items = {'PALAVRA_CLASS':([0,2,10,11,12,16,17,19,22,23,24,26,27,31,32,37,38,39,42,47,48,56,60,61,62,63,70,72,75,76,77,79,83,85,87,92,94,96,98,102,106,110,114,115,119,120,125,127,131,133,135,136,137,138,140,143,144,145,147,148,149,151,152,153,159,160,161,162,163,165,169,170,171,173,174,176,178,179,],[3,3,-3,-6,-7,-24,-22,-29,-4,-5,-21,-46,-47,-9,-10,-28,-65,-66,-75,-23,-45,-8,-49,-25,-63,-64,-30,-31,-48,-11,-13,-50,-81,-17,-18,-68,-71,-73,-74,-32,-33,-84,-53,-54,-26,-27,-35,-36,-76,-34,-15,-12,-14,-80,-60,-62,-55,-51,-72,-69,-70,-39,-37,-38,-79,-52,-61,-56,-58,-40,-16,-57,-59,-42,-41,-67,-44,-43,]),'error':([0,2,3,10,11,12,16,17,19,22,23,24,26,27,31,32,37,38,39,42,47,48,50,56,60,61,62,63,70,72,75,76,77,79,83,85,87,92,94,96,98,102,106,110,114,115,119,120,125,127,131,133,135,136,137,138,140,143,144,145,147,148,149,151,152,153,159,160,161,162,163,165,169,170,171,173,174,176,178,179,],[4,4,7,-3,-6,-7,-24,-22,-29,-4,-5,-21,-46,-47,-9,-10,-28,-65,-66,-75,-23,-45,77,-8,-49,-25,-63,-64,-30,-31,-48,-11,-13,-50,-81,-17,-18,-68,-71,-73,-74,-32,-33,-84,-53,-54,-26,-27,-35,-36,-76,-34,-15,-12,-14,-80,-60,-62,-55,-51,-72,-69,-70,-39,-37,-38,-79,-52,-61,-56,-58,-40,-16,-57,-59,-42,-41,-67,-44,-43,]),'$end':([1,2,5,10,11,12,16,17,19,22,23,24,26,27,31,32,37,38,39,42,47,48,56,60,61,62,63,70,72,75,76,77,79,83,85,87,92,94,96,98,102,106,110,114,115,119,120,125,127,131,133,135,136,137,138,140,143,144,145,147,148,149,151,152,153,159,160,161,162,163,165,169,170,171,173,174,176,178,179,],[0,-2,-1,-3,-6,-7,-24,-22,-29,-4,-5,-21,-46,-47,-9,-10,-28,-65,-66,-75,-23,-45,-8,-49,-25,-63,-64,-30,-31,-48,-11,-13,-50,-81,-17,-18,-68,-71,-73,-74,-32,-33,-84,-53,-54,-26,-27,-35,-36,-76,-34,-15,-12,-14,-80,-60,-62,-55,-51,-72,-69,-70,-39,-37,-38,-79,-52,-61,-56,-58,-40,-16,-57,-59,-42,-41,-67,-44,-43,]),'CLASSE':([3,4,6,7,8,13,14,25,29,30,33,34,35,44,49,51,68,69,73,74,82,84,86,88,89,90,91,97,111,121,132,140,],[6,8,9,9,9,28,9,9,53,55,58,58,28,70,9,78,98,100,105,106,116,55,58,9,9,70,122,105,138,146,105,28,]),'EQUIVALENT_TO':([6,7,8,15,16,17,19,24,37,38,39,42,47,53,61,62,63,70,72,92,94,96,98,102,106,119,120,125,127,131,133,147,148,149,151,152,153,165,173,174,176,178,179,],[13,13,13,35,-24,-22,-29,-21,-28,-65,-66,-75,-23,82,-25,-63,-64,-30,-31,-68,-71,-73,-74,-32,-33,-26,-27,-35,-36,-76,-34,-72,-69,-70,-39,-37,-38,-40,-42,-41,-67,-44,-43,]),'SUBCLASSOF':([6,7,8,26,38,39,42,62,63,70,72,79,92,94,96,98,102,106,110,114,115,125,127,131,133,138,140,143,144,145,147,148,149,151,152,153,159,160,161,162,163,165,170,171,173,174,176,178,179,],[14,14,14,49,-65,-66,-75,-63,-64,-30,-31,-50,-68,-71,-73,-74,-32,-33,-84,-53,-54,-35,-36,-76,-34,-80,-60,-62,-55,-51,-72,-69,-70,-39,-37,-38,-79,-52,-61,-56,-58,-40,-57,-59,-42,-41,-67,-44,-43,]),'ABRE_PARENT':([6,7,8,14,20,25,40,45,49,52,67,70,72,80,81,88,89,90,93,95,97,102,106,112,125,127,131,133,151,152,153,165,173,174,178,179,],[18,18,18,18,40,18,40,73,18,80,97,-30,-31,40,40,18,18,121,40,40,40,-32,-33,40,-35,-36,-76,-34,-39,-37,-38,-40,-42,-41,-44,-43,]),'AND':([6,7,8,9,14,25,28,38,39,42,49,61,66,70,72,88,89,92,94,96,98,102,106,113,115,116,125,127,131,133,138,147,148,149,151,152,153,159,162,163,165,173,174,176,178,179,],[20,20,20,20,20,20,52,20,20,-75,20,88,95,-30,-31,20,20,-68,-71,-73,-74,-32,-33,20,20,20,-35,-36,-76,-34,-80,-72,-69,-70,-39,-37,-38,-79,20,20,-40,-42,-41,-67,-44,-43,]),'PROPRIEDADE':([6,7,8,14,18,19,20,21,25,40,41,49,52,64,70,72,80,88,89,97,101,102,106,125,126,127,129,131,133,150,151,152,153,165,173,174,177,178,179,],[21,21,21,21,21,21,41,43,21,64,43,21,21,43,-30,-31,21,21,21,64,21,-32,-33,-35,21,-36,21,-76,-34,21,-39,-37,-38,-40,-42,-41,21,-44,-43,]),'CARACTERE_ESPECIAL':([9,55,58,61,70,76,77,100,102,125,135,166,174,],[25,84,86,89,101,108,109,126,129,150,158,173,177,]),'PALAVRA_RESERVADA':([13,35,41,140,],[29,29,68,29,]),'ABRE_CHAVE':([13,],[30,]),'DISJOINTCLASSES':([14,16,17,19,24,31,37,38,39,42,47,61,62,63,70,72,92,94,96,98,102,106,119,120,125,127,131,133,147,148,149,151,152,153,165,173,174,176,178,179,],[33,-24,-22,-29,-21,33,-28,-65,-66,-75,-23,-25,-63,-64,-30,-31,-68,-71,-73,-74,-32,-33,-26,-27,-35,-36,-76,-34,-72,-69,-70,-39,-37,-38,-40,-42,-41,-67,-44,-43,]),'DISJOINTWITH':([14,16,17,19,24,31,37,38,39,42,47,61,62,63,70,72,92,94,96,98,102,106,119,120,125,127,131,133,147,148,149,151,152,153,165,173,174,176,178,179,],[34,-24,-22,-29,-21,34,-28,-65,-66,-75,-23,-25,-63,-64,-30,-31,-68,-71,-73,-74,-32,-33,-26,-27,-35,-36,-76,-34,-72,-69,-70,-39,-37,-38,-40,-42,-41,-67,-44,-43,]),'SOME':([21,41,43,64,],[44,44,69,90,]),'ONLY':([21,41,64,],[45,67,45,]),'COMPARADORES':([21,41,64,],[46,46,46,]),'INDIVIDUALS':([26,38,39,42,57,58,59,62,63,70,72,79,92,94,96,98,102,106,110,114,115,118,125,127,131,133,138,140,143,144,145,147,148,149,151,152,153,159,160,161,162,163,165,170,171,173,174,176,178,179,],[50,-65,-66,-75,50,-19,50,-63,-64,-30,-31,-50,-68,-71,-73,-74,-32,-33,-84,-53,-54,-20,-35,-36,-76,-34,-80,-60,-62,-55,-51,-72,-69,-70,-39,-37,-38,-79,-52,-61,-56,-58,-40,-57,-59,-42,-41,-67,-44,-43,]),'OR':([28,66,70,72,78,81,92,94,102,105,106,112,125,127,131,133,138,146,147,148,149,151,152,153,165,173,174,176,178,179,],[51,93,-30,-31,111,111,-68,-71,-32,132,-33,111,-35,-36,-76,-34,111,111,-72,-69,-70,-39,-37,-38,-40,-42,-41,-67,-44,-43,]),'FECHA_PARENT':([36,38,39,42,62,63,65,66,70,72,92,94,96,98,102,104,105,106,112,122,123,124,125,127,131,133,138,139,141,142,143,147,148,149,151,152,153,156,159,164,165,172,173,174,176,178,179,],[61,-65,-66,-75,-63,-64,92,94,-30,-31,-68,-71,-73,-74,-32,131,-78,-33,140,147,148,149,-35,-36,-76,-34,-80,160,162,163,-62,-72,-69,-70,-39,-37,-38,-77,-79,172,-40,176,-42,-41,-67,-44,-43,]),'NAMESPACE':([44,69,74,90,],[71,99,107,71,]),'CARDINALIDADE':([46,154,155,168,],[74,166,167,175,]),'NOME_INDIVIDUO':([50,108,109,158,],[76,135,135,135,]),'FECHA_CHAVE':([54,55,117,],[83,-83,-82,]),'VALUE':([64,],[91,]),'TIPO':([71,99,107,],[102,125,133,]),'TIPO_NUMERICO':([71,107,],[103,134,]),'ABRE_COLCHETE':([102,103,134,],[128,130,157,]),'OPERADORES':([128,129,130,157,],[152,154,155,168,]),'FECHA_COLCHETE':([167,175,],[174,178,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,2,],[1,5,]),'declaracao_classe':([0,2,],[2,2,]),'tipo_classe_primaria':([6,7,8,],[10,22,23,]),'declaracao_classe_definida':([6,7,8,],[11,11,11,]),'declaracao_classe_primitiva':([6,7,8,],[12,12,12,]),'continuacao_subclassof':([6,7,8,14,25,49,88,89,],[15,15,15,31,47,75,119,120,]),'caso_ands':([6,7,8,9,14,25,38,39,49,88,89,113,115,116,162,163,],[16,16,16,24,16,16,62,63,16,16,16,143,144,143,170,171,]),'declaracao_propriedades':([6,7,8,14,19,25,49,88,89,],[17,17,17,17,37,17,17,17,17,]),'declaracao_existencial':([6,7,8,14,18,19,20,25,40,49,52,80,88,89,97,101,126,129,150,177,],[19,19,19,19,36,19,42,19,65,19,81,112,19,19,65,127,151,153,165,179,]),'continuacao_equivalentto':([13,35,140,],[26,60,161,]),'declaracao_classe_enumerada':([13,],[27,]),'caso_disjoint_opcional':([14,31,],[32,56,]),'casos_parentese':([20,40,67,80,81,93,95,97,112,],[38,66,96,113,114,123,124,66,139,]),'casos_sem_parentese':([20,],[39,]),'caso_individuals_opcional':([26,57,59,],[48,85,87,]),'classes_enumeradas':([30,84,],[54,117,]),'continuacao_disjoint_opcional':([33,34,86,],[57,59,118,]),'declaracao_classe_axioma_fechamento':([45,67,],[72,72,]),'declaracao_classe_coberta':([51,],[79,]),'classes_or_fechamento':([73,97,132,],[104,104,156,]),'classes_or':([78,81,112,138,146,],[110,115,141,159,164,]),'continuacao_individuals':([108,109,158,],[136,137,169,]),'declaracao_classe_aninhada':([113,116,],[142,145,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> declaracao_classe programa','programa',2,'p_programa','analisador_semantico.py',120),
  ('programa -> declaracao_classe','programa',1,'p_programa','analisador_semantico.py',121),
  ('declaracao_classe -> PALAVRA_CLASS CLASSE tipo_classe_primaria','declaracao_classe',3,'p_declaracao_classe','analisador_semantico.py',125),
  ('declaracao_classe -> PALAVRA_CLASS error tipo_classe_primaria','declaracao_classe',3,'p_declaracao_classe_error','analisador_semantico.py',175),
  ('declaracao_classe -> error CLASSE tipo_classe_primaria','declaracao_classe',3,'p_declaracao_classe_error','analisador_semantico.py',176),
  ('tipo_classe_primaria -> declaracao_classe_definida','tipo_classe_primaria',1,'p_tipo_classe_primaria','analisador_semantico.py',187),
  ('tipo_classe_primaria -> declaracao_classe_primitiva','tipo_classe_primaria',1,'p_tipo_classe_primaria','analisador_semantico.py',188),
  ('declaracao_classe_primitiva -> SUBCLASSOF continuacao_subclassof caso_disjoint_opcional','declaracao_classe_primitiva',3,'p_declaracao_classe_primitiva','analisador_semantico.py',195),
  ('declaracao_classe_primitiva -> SUBCLASSOF continuacao_subclassof','declaracao_classe_primitiva',2,'p_declaracao_classe_primitiva','analisador_semantico.py',196),
  ('declaracao_classe_primitiva -> SUBCLASSOF caso_disjoint_opcional','declaracao_classe_primitiva',2,'p_declaracao_classe_primitiva','analisador_semantico.py',197),
  ('caso_individuals_opcional -> INDIVIDUALS NOME_INDIVIDUO','caso_individuals_opcional',2,'p_caso_individuals_opcional','analisador_semantico.py',206),
  ('caso_individuals_opcional -> INDIVIDUALS NOME_INDIVIDUO CARACTERE_ESPECIAL continuacao_individuals','caso_individuals_opcional',4,'p_caso_individuals_opcional','analisador_semantico.py',207),
  ('caso_individuals_opcional -> INDIVIDUALS error','caso_individuals_opcional',2,'p_caso_individuals_opcional_error','analisador_semantico.py',212),
  ('caso_individuals_opcional -> INDIVIDUALS error CARACTERE_ESPECIAL continuacao_individuals','caso_individuals_opcional',4,'p_caso_individuals_opcional_error','analisador_semantico.py',213),
  ('continuacao_individuals -> NOME_INDIVIDUO','continuacao_individuals',1,'p_continuacao_individuals','analisador_semantico.py',221),
  ('continuacao_individuals -> NOME_INDIVIDUO CARACTERE_ESPECIAL continuacao_individuals','continuacao_individuals',3,'p_continuacao_individuals','analisador_semantico.py',222),
  ('caso_disjoint_opcional -> DISJOINTCLASSES continuacao_disjoint_opcional caso_individuals_opcional','caso_disjoint_opcional',3,'p_caso_disjoint_opcional','analisador_semantico.py',229),
  ('caso_disjoint_opcional -> DISJOINTWITH continuacao_disjoint_opcional caso_individuals_opcional','caso_disjoint_opcional',3,'p_caso_disjoint_opcional','analisador_semantico.py',230),
  ('continuacao_disjoint_opcional -> CLASSE','continuacao_disjoint_opcional',1,'p_continuacao_disjoint_opcional','analisador_semantico.py',249),
  ('continuacao_disjoint_opcional -> CLASSE CARACTERE_ESPECIAL continuacao_disjoint_opcional','continuacao_disjoint_opcional',3,'p_continuacao_disjoint_opcional','analisador_semantico.py',250),
  ('continuacao_subclassof -> CLASSE caso_ands','continuacao_subclassof',2,'p_continuacao_subclassof','analisador_semantico.py',263),
  ('continuacao_subclassof -> declaracao_propriedades','continuacao_subclassof',1,'p_continuacao_subclassof','analisador_semantico.py',264),
  ('continuacao_subclassof -> CLASSE CARACTERE_ESPECIAL continuacao_subclassof','continuacao_subclassof',3,'p_continuacao_subclassof','analisador_semantico.py',265),
  ('continuacao_subclassof -> caso_ands','continuacao_subclassof',1,'p_continuacao_subclassof','analisador_semantico.py',266),
  ('continuacao_subclassof -> ABRE_PARENT declaracao_existencial FECHA_PARENT','continuacao_subclassof',3,'p_continuacao_subclassof','analisador_semantico.py',267),
  ('continuacao_subclassof -> ABRE_PARENT declaracao_existencial FECHA_PARENT AND continuacao_subclassof','continuacao_subclassof',5,'p_continuacao_subclassof','analisador_semantico.py',268),
  ('continuacao_subclassof -> ABRE_PARENT declaracao_existencial FECHA_PARENT CARACTERE_ESPECIAL continuacao_subclassof','continuacao_subclassof',5,'p_continuacao_subclassof','analisador_semantico.py',269),
  ('declaracao_propriedades -> declaracao_existencial declaracao_propriedades','declaracao_propriedades',2,'p_declaracao_propriedades','analisador_semantico.py',274),
  ('declaracao_propriedades -> declaracao_existencial','declaracao_propriedades',1,'p_declaracao_propriedades','analisador_semantico.py',275),
  ('declaracao_existencial -> PROPRIEDADE SOME CLASSE','declaracao_existencial',3,'p_declaracao_existencial','analisador_semantico.py',280),
  ('declaracao_existencial -> PROPRIEDADE ONLY declaracao_classe_axioma_fechamento','declaracao_existencial',3,'p_declaracao_existencial','analisador_semantico.py',281),
  ('declaracao_existencial -> PROPRIEDADE SOME NAMESPACE TIPO','declaracao_existencial',4,'p_declaracao_existencial','analisador_semantico.py',283),
  ('declaracao_existencial -> PROPRIEDADE COMPARADORES CARDINALIDADE CLASSE','declaracao_existencial',4,'p_declaracao_existencial','analisador_semantico.py',284),
  ('declaracao_existencial -> PROPRIEDADE COMPARADORES CARDINALIDADE NAMESPACE TIPO','declaracao_existencial',5,'p_declaracao_existencial','analisador_semantico.py',286),
  ('declaracao_existencial -> PROPRIEDADE PROPRIEDADE SOME NAMESPACE TIPO','declaracao_existencial',5,'p_declaracao_existencial','analisador_semantico.py',287),
  ('declaracao_existencial -> PROPRIEDADE SOME CLASSE CARACTERE_ESPECIAL declaracao_existencial','declaracao_existencial',5,'p_declaracao_existencial','analisador_semantico.py',288),
  ('declaracao_existencial -> PROPRIEDADE SOME NAMESPACE TIPO ABRE_COLCHETE OPERADORES','declaracao_existencial',6,'p_declaracao_existencial','analisador_semantico.py',290),
  ('declaracao_existencial -> PROPRIEDADE SOME NAMESPACE TIPO CARACTERE_ESPECIAL declaracao_existencial','declaracao_existencial',6,'p_declaracao_existencial','analisador_semantico.py',291),
  ('declaracao_existencial -> PROPRIEDADE PROPRIEDADE SOME CLASSE CARACTERE_ESPECIAL declaracao_existencial','declaracao_existencial',6,'p_declaracao_existencial','analisador_semantico.py',292),
  ('declaracao_existencial -> PROPRIEDADE PROPRIEDADE SOME NAMESPACE TIPO CARACTERE_ESPECIAL declaracao_existencial','declaracao_existencial',7,'p_declaracao_existencial','analisador_semantico.py',295),
  ('declaracao_existencial -> PROPRIEDADE SOME NAMESPACE TIPO_NUMERICO ABRE_COLCHETE OPERADORES CARDINALIDADE FECHA_COLCHETE','declaracao_existencial',8,'p_declaracao_existencial','analisador_semantico.py',298),
  ('declaracao_existencial -> PROPRIEDADE SOME NAMESPACE TIPO CARACTERE_ESPECIAL OPERADORES CARDINALIDADE CARACTERE_ESPECIAL','declaracao_existencial',8,'p_declaracao_existencial','analisador_semantico.py',299),
  ('declaracao_existencial -> PROPRIEDADE SOME NAMESPACE TIPO_NUMERICO ABRE_COLCHETE OPERADORES CARDINALIDADE FECHA_COLCHETE CARACTERE_ESPECIAL declaracao_existencial','declaracao_existencial',10,'p_declaracao_existencial','analisador_semantico.py',302),
  ('declaracao_existencial -> PROPRIEDADE COMPARADORES CARDINALIDADE NAMESPACE TIPO_NUMERICO ABRE_COLCHETE OPERADORES CARDINALIDADE FECHA_COLCHETE','declaracao_existencial',9,'p_declaracao_existencial','analisador_semantico.py',305),
  ('declaracao_classe_definida -> EQUIVALENT_TO continuacao_equivalentto caso_individuals_opcional','declaracao_classe_definida',3,'p_declaracao_classe_definida','analisador_semantico.py',355),
  ('declaracao_classe_definida -> EQUIVALENT_TO continuacao_equivalentto','declaracao_classe_definida',2,'p_declaracao_classe_definida','analisador_semantico.py',356),
  ('declaracao_classe_definida -> EQUIVALENT_TO declaracao_classe_enumerada','declaracao_classe_definida',2,'p_declaracao_classe_definida','analisador_semantico.py',357),
  ('declaracao_classe_definida -> EQUIVALENT_TO continuacao_equivalentto SUBCLASSOF continuacao_subclassof','declaracao_classe_definida',4,'p_declaracao_classe_definida','analisador_semantico.py',358),
  ('declaracao_classe_definida -> continuacao_subclassof EQUIVALENT_TO continuacao_equivalentto','declaracao_classe_definida',3,'p_declaracao_classe_definida','analisador_semantico.py',359),
  ('continuacao_equivalentto -> CLASSE OR declaracao_classe_coberta','continuacao_equivalentto',3,'p_continuacao_equivalentto','analisador_semantico.py',366),
  ('continuacao_equivalentto -> PALAVRA_RESERVADA CLASSE EQUIVALENT_TO CLASSE declaracao_classe_aninhada','continuacao_equivalentto',5,'p_continuacao_equivalentto','analisador_semantico.py',367),
  ('continuacao_equivalentto -> CLASSE AND ABRE_PARENT declaracao_existencial casos_parentese FECHA_PARENT','continuacao_equivalentto',6,'p_continuacao_equivalentto','analisador_semantico.py',368),
  ('continuacao_equivalentto -> CLASSE AND declaracao_existencial casos_parentese','continuacao_equivalentto',4,'p_continuacao_equivalentto','analisador_semantico.py',369),
  ('continuacao_equivalentto -> CLASSE AND declaracao_existencial classes_or','continuacao_equivalentto',4,'p_continuacao_equivalentto','analisador_semantico.py',370),
  ('continuacao_equivalentto -> CLASSE AND declaracao_existencial classes_or caso_ands','continuacao_equivalentto',5,'p_continuacao_equivalentto','analisador_semantico.py',371),
  ('continuacao_equivalentto -> CLASSE AND ABRE_PARENT declaracao_existencial classes_or FECHA_PARENT','continuacao_equivalentto',6,'p_continuacao_equivalentto','analisador_semantico.py',372),
  ('continuacao_equivalentto -> CLASSE AND ABRE_PARENT declaracao_existencial classes_or FECHA_PARENT caso_ands','continuacao_equivalentto',7,'p_continuacao_equivalentto','analisador_semantico.py',373),
  ('continuacao_equivalentto -> CLASSE AND ABRE_PARENT casos_parentese declaracao_classe_aninhada FECHA_PARENT','continuacao_equivalentto',6,'p_continuacao_equivalentto','analisador_semantico.py',374),
  ('continuacao_equivalentto -> CLASSE AND ABRE_PARENT casos_parentese declaracao_classe_aninhada FECHA_PARENT caso_ands','continuacao_equivalentto',7,'p_continuacao_equivalentto','analisador_semantico.py',375),
  ('continuacao_equivalentto -> CLASSE AND ABRE_PARENT declaracao_existencial FECHA_PARENT','continuacao_equivalentto',5,'p_continuacao_equivalentto','analisador_semantico.py',376),
  ('continuacao_equivalentto -> CLASSE AND ABRE_PARENT declaracao_existencial FECHA_PARENT continuacao_equivalentto','continuacao_equivalentto',6,'p_continuacao_equivalentto','analisador_semantico.py',377),
  ('declaracao_classe_aninhada -> caso_ands','declaracao_classe_aninhada',1,'p_declaracao_classe_aninhada','analisador_semantico.py',382),
  ('caso_ands -> AND casos_parentese caso_ands','caso_ands',3,'p_caso_ands','analisador_semantico.py',387),
  ('caso_ands -> AND casos_sem_parentese caso_ands','caso_ands',3,'p_caso_ands','analisador_semantico.py',388),
  ('caso_ands -> AND casos_parentese','caso_ands',2,'p_caso_ands','analisador_semantico.py',389),
  ('caso_ands -> AND casos_sem_parentese','caso_ands',2,'p_caso_ands','analisador_semantico.py',390),
  ('casos_parentese -> ABRE_PARENT PROPRIEDADE SOME ABRE_PARENT CLASSE classes_or FECHA_PARENT FECHA_PARENT','casos_parentese',8,'p_casos_parentese','analisador_semantico.py',395),
  ('casos_parentese -> ABRE_PARENT declaracao_existencial FECHA_PARENT','casos_parentese',3,'p_casos_parentese','analisador_semantico.py',396),
  ('casos_parentese -> ABRE_PARENT casos_parentese OR casos_parentese FECHA_PARENT','casos_parentese',5,'p_casos_parentese','analisador_semantico.py',397),
  ('casos_parentese -> ABRE_PARENT casos_parentese AND casos_parentese FECHA_PARENT','casos_parentese',5,'p_casos_parentese','analisador_semantico.py',398),
  ('casos_parentese -> ABRE_PARENT casos_parentese FECHA_PARENT','casos_parentese',3,'p_casos_parentese','analisador_semantico.py',399),
  ('casos_parentese -> ABRE_PARENT PROPRIEDADE VALUE CLASSE FECHA_PARENT','casos_parentese',5,'p_casos_parentese','analisador_semantico.py',400),
  ('casos_sem_parentese -> PROPRIEDADE ONLY casos_parentese','casos_sem_parentese',3,'p_casos_sem_parentese','analisador_semantico.py',405),
  ('casos_sem_parentese -> PROPRIEDADE PALAVRA_RESERVADA CLASSE','casos_sem_parentese',3,'p_casos_sem_parentese','analisador_semantico.py',406),
  ('casos_sem_parentese -> declaracao_existencial','casos_sem_parentese',1,'p_casos_sem_parentese','analisador_semantico.py',407),
  ('declaracao_classe_axioma_fechamento -> ABRE_PARENT classes_or_fechamento FECHA_PARENT','declaracao_classe_axioma_fechamento',3,'p_declaracao_classe_axioma_fechamento','analisador_semantico.py',414),
  ('classes_or_fechamento -> CLASSE OR classes_or_fechamento','classes_or_fechamento',3,'p_classes_or_fechamento','analisador_semantico.py',422),
  ('classes_or_fechamento -> CLASSE','classes_or_fechamento',1,'p_classes_or_fechamento','analisador_semantico.py',423),
  ('classes_or -> OR CLASSE classes_or','classes_or',3,'p_classes_or','analisador_semantico.py',433),
  ('classes_or -> OR CLASSE','classes_or',2,'p_classes_or','analisador_semantico.py',434),
  ('declaracao_classe_enumerada -> ABRE_CHAVE classes_enumeradas FECHA_CHAVE','declaracao_classe_enumerada',3,'p_declaracao_classe_enumerada','analisador_semantico.py',441),
  ('classes_enumeradas -> CLASSE CARACTERE_ESPECIAL classes_enumeradas','classes_enumeradas',3,'p_classes_enumeradas','analisador_semantico.py',447),
  ('classes_enumeradas -> CLASSE','classes_enumeradas',1,'p_classes_enumeradas','analisador_semantico.py',448),
  ('declaracao_classe_coberta -> CLASSE classes_or','declaracao_classe_coberta',2,'p_declaracao_classe_coberta','analisador_semantico.py',455),
]
