
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ABRE_CHAVE ABRE_COLCHETE ABRE_PARENT AND CARACTERE_ESPECIAL CARDINALIDADE CLASSE COMPARADORES DISJOINTS EQUIVALENT_TO FECHA_CHAVE FECHA_COLCHETE FECHA_PARENT INDIVIDUALS NAMESPACE NOME_INDIVIDUO ONLY OPERADORES OR PALAVRA_CLASS PALAVRA_RESERVADA PROPRIEDADE SOME SUBCLASSOF TIPO TIPO_NUMERICO VALUEprograma : declaracao_classe programa\n                | declaracao_classe\n    declaracao_classe : PALAVRA_CLASS CLASSE tipo_classe_primaria\n    \n    declaracao_classe : PALAVRA_CLASS error tipo_classe_primaria\n                      | error CLASSE tipo_classe_primaria        \n    \n    tipo_classe_primaria : declaracao_classe_definida\n                         | declaracao_classe_primitiva\n    \n    declaracao_classe_primitiva : SUBCLASSOF continuacao_subclassof\n    \n    continuacao_individuals : NOME_INDIVIDUO \n                            | NOME_INDIVIDUO CARACTERE_ESPECIAL continuacao_individuals\n    \n    caso_disjoint_opcional : DISJOINTS continuacao_disjoint_opcional INDIVIDUALS continuacao_individuals\n                           | DISJOINTS continuacao_disjoint_opcional\n    \n    caso_disjoint_opcional : error continuacao_disjoint_opcional INDIVIDUALS continuacao_individuals\n                           | DISJOINTS continuacao_disjoint_opcional error\n                           | DISJOINTS continuacao_disjoint_opcional INDIVIDUALS error\n    \n    continuacao_disjoint_opcional : CLASSE CARACTERE_ESPECIAL continuacao_disjoint_opcional\n                                  | CLASSE \n    continuacao_subclassof :   CLASSE caso_ands\n                                | CLASSE\n                                | declaracao_propriedades\n                                | declaracao_propriedades caso_disjoint_opcional\n                                | CLASSE CARACTERE_ESPECIAL continuacao_subclassof\n                                | caso_ands\n                                | ABRE_PARENT declaracao_propriedades FECHA_PARENT\n                                | ABRE_PARENT declaracao_propriedades FECHA_PARENT AND continuacao_subclassof\n                                | ABRE_PARENT declaracao_propriedades FECHA_PARENT CARACTERE_ESPECIAL continuacao_subclassof\n                                | CLASSE caso_disjoint_opcional\n                                | caso_disjoint_opcional\n    \n    declaracao_propriedades : declaracao_existencial declaracao_propriedades\n                            | declaracao_existencial\n    \n    declaracao_existencial : PROPRIEDADE SOME NAMESPACE TIPO\n                           | PROPRIEDADE COMPARADORES CARDINALIDADE NAMESPACE TIPO\n                           | PROPRIEDADE SOME NAMESPACE TIPO ABRE_COLCHETE OPERADORES\n                           | PROPRIEDADE SOME NAMESPACE TIPO CARACTERE_ESPECIAL declaracao_existencial\n                           | PROPRIEDADE PROPRIEDADE SOME NAMESPACE TIPO\n                           | PROPRIEDADE PROPRIEDADE SOME NAMESPACE TIPO CARACTERE_ESPECIAL declaracao_existencial\n                           | PROPRIEDADE SOME NAMESPACE TIPO CARACTERE_ESPECIAL OPERADORES CARDINALIDADE CARACTERE_ESPECIAL\n                           | PROPRIEDADE SOME NAMESPACE TIPO_NUMERICO ABRE_COLCHETE OPERADORES CARDINALIDADE FECHA_COLCHETE\n                           | PROPRIEDADE SOME NAMESPACE TIPO_NUMERICO ABRE_COLCHETE OPERADORES CARDINALIDADE FECHA_COLCHETE CARACTERE_ESPECIAL declaracao_existencial\n                           | PROPRIEDADE COMPARADORES CARDINALIDADE NAMESPACE TIPO_NUMERICO ABRE_COLCHETE OPERADORES CARDINALIDADE FECHA_COLCHETE\n                           \n                           \n                           | PROPRIEDADE ONLY CLASSE\n                           | PROPRIEDADE ONLY ABRE_PARENT declaracao_classe_axioma_fechamento FECHA_PARENT\n                           | PROPRIEDADE ONLY CLASSE CARACTERE_ESPECIAL declaracao_existencial\n                           \n                           | PROPRIEDADE SOME CLASSE\n                           \n                           | PROPRIEDADE COMPARADORES CARDINALIDADE CLASSE\n\n                           | PROPRIEDADE PROPRIEDADE COMPARADORES CARDINALIDADE CLASSE\n                           | PROPRIEDADE SOME CLASSE CARACTERE_ESPECIAL declaracao_existencial\n\n                           | PROPRIEDADE COMPARADORES CARDINALIDADE CLASSE CARACTERE_ESPECIAL declaracao_existencial\n                           | PROPRIEDADE PROPRIEDADE SOME CLASSE CARACTERE_ESPECIAL declaracao_existencial\n\n                           | PROPRIEDADE PROPRIEDADE COMPARADORES CARDINALIDADE CLASSE CARACTERE_ESPECIAL declaracao_existencial\n    \n    declaracao_classe_definida : EQUIVALENT_TO continuacao_equivalentto caso_disjoint_opcional\n                               | EQUIVALENT_TO continuacao_equivalentto\n                               | EQUIVALENT_TO declaracao_classe_enumerada\n                               | EQUIVALENT_TO continuacao_equivalentto SUBCLASSOF continuacao_subclassof\n    \n        continuacao_equivalentto : CLASSE OR declaracao_classe_coberta\n                                 | PALAVRA_RESERVADA CLASSE EQUIVALENT_TO CLASSE declaracao_classe_aninhada \n                                 | CLASSE AND ABRE_PARENT declaracao_existencial casos_parentese FECHA_PARENT\n                                 | CLASSE AND declaracao_existencial casos_parentese\n                                 | CLASSE AND declaracao_existencial\n                                 | CLASSE AND declaracao_existencial classes_or\n                                 | CLASSE AND declaracao_existencial caso_ands\n                                 | CLASSE AND declaracao_existencial classes_or caso_ands\n                                 | CLASSE AND ABRE_PARENT declaracao_existencial classes_or FECHA_PARENT \n                                 | CLASSE AND ABRE_PARENT declaracao_existencial classes_or FECHA_PARENT caso_ands\n                                 | CLASSE AND ABRE_PARENT casos_parentese declaracao_classe_aninhada FECHA_PARENT\n                                 | CLASSE AND ABRE_PARENT casos_parentese declaracao_classe_aninhada FECHA_PARENT caso_ands\n                                 | CLASSE AND ABRE_PARENT declaracao_existencial FECHA_PARENT continuacao_equivalentto\n                                 | CLASSE AND ABRE_PARENT declaracao_existencial FECHA_PARENT \n                                 | CLASSE AND ABRE_PARENT declaracao_existencial FECHA_PARENT caso_ands\n    \n    declaracao_classe_aninhada : caso_ands\n    \n    caso_ands : AND casos_parentese caso_ands\n              | AND casos_sem_parentese caso_ands\n              | AND casos_parentese\n              | AND casos_sem_parentese    \n    \n    casos_parentese :  ABRE_PARENT PROPRIEDADE SOME ABRE_PARENT CLASSE classes_or FECHA_PARENT FECHA_PARENT\n                      | ABRE_PARENT declaracao_existencial FECHA_PARENT\n                      | ABRE_PARENT casos_parentese OR casos_parentese FECHA_PARENT\n                      | ABRE_PARENT casos_parentese AND casos_parentese FECHA_PARENT\n                      | ABRE_PARENT casos_parentese FECHA_PARENT\n                      | ABRE_PARENT PROPRIEDADE VALUE CLASSE FECHA_PARENT\n    \n    casos_sem_parentese :  PROPRIEDADE ONLY casos_parentese \n                        |  PROPRIEDADE PALAVRA_RESERVADA CLASSE\n                        |  declaracao_existencial\n    \n    declaracao_classe_axioma_fechamento :  classes_or_fechamento \n                                        \n    \n    classes_or_fechamento : CLASSE OR classes_or_fechamento\n                          | CLASSE\n    \n    classes_or : OR CLASSE classes_or\n               | OR CLASSE\n               \n    \n    declaracao_classe_enumerada : ABRE_CHAVE classes_enumeradas FECHA_CHAVE\n    \n    classes_enumeradas : CLASSE CARACTERE_ESPECIAL classes_enumeradas\n                       | CLASSE\n    \n    declaracao_classe_coberta : CLASSE classes_or \n    '
    
_lr_action_items = {'PALAVRA_CLASS':([0,2,9,10,11,14,15,16,17,21,22,23,24,25,28,32,39,41,42,44,45,48,49,50,51,57,59,61,63,65,66,67,68,75,81,83,85,89,90,91,98,100,102,104,105,106,107,108,109,113,117,122,124,127,128,129,130,131,137,139,143,144,147,148,150,151,152,153,154,155,157,158,159,160,162,164,165,169,171,172,174,175,180,181,183,185,186,],[3,3,-3,-6,-7,-4,-5,-52,-53,-8,-19,-23,-20,-28,-30,-51,-18,-27,-21,-73,-74,-83,-29,-12,-17,-54,-55,-59,-89,-22,-24,-71,-72,-14,-44,-41,-92,-58,-60,-61,-76,-79,-81,-82,-11,-15,-9,-16,-13,-31,-45,-88,-68,-70,-62,-56,-25,-26,-35,-46,-47,-32,-43,-42,-87,-57,-67,-69,-63,-65,-80,-77,-78,-10,-49,-33,-34,-48,-64,-66,-36,-50,-37,-38,-75,-40,-39,]),'error':([0,2,3,9,10,11,13,14,15,16,17,21,22,23,24,25,28,32,33,39,40,41,42,44,45,48,49,50,51,57,59,61,63,65,66,67,68,74,75,81,83,85,89,90,91,94,95,98,100,102,104,105,106,107,108,109,113,117,122,124,127,128,129,130,131,137,139,143,144,147,148,150,151,152,153,154,155,157,158,159,160,162,164,165,169,171,172,174,175,180,181,183,185,186,],[4,4,7,-3,-6,-7,30,-4,-5,30,-53,-8,30,-23,30,-28,-30,-51,30,-18,30,-27,-21,-73,-74,-83,-29,75,-17,-54,-55,-59,-89,-22,-24,-71,-72,106,-14,-44,-41,-92,-58,-60,-61,30,30,-76,-79,-81,-82,-11,-15,-9,-16,-13,-31,-45,-88,-68,-70,-62,-56,-25,-26,-35,-46,-47,-32,-43,-42,-87,-57,-67,-69,-63,-65,-80,-77,-78,-10,-49,-33,-34,-48,-64,-66,-36,-50,-37,-38,-75,-40,-39,]),'$end':([1,2,5,9,10,11,14,15,16,17,21,22,23,24,25,28,32,39,41,42,44,45,48,49,50,51,57,59,61,63,65,66,67,68,75,81,83,85,89,90,91,98,100,102,104,105,106,107,108,109,113,117,122,124,127,128,129,130,131,137,139,143,144,147,148,150,151,152,153,154,155,157,158,159,160,162,164,165,169,171,172,174,175,180,181,183,185,186,],[0,-2,-1,-3,-6,-7,-4,-5,-52,-53,-8,-19,-23,-20,-28,-30,-51,-18,-27,-21,-73,-74,-83,-29,-12,-17,-54,-55,-59,-89,-22,-24,-71,-72,-14,-44,-41,-92,-58,-60,-61,-76,-79,-81,-82,-11,-15,-9,-16,-13,-31,-45,-88,-68,-70,-62,-56,-25,-26,-35,-46,-47,-32,-43,-42,-87,-57,-67,-69,-63,-65,-80,-77,-78,-10,-49,-33,-34,-48,-64,-66,-36,-50,-37,-38,-75,-40,-39,]),'CLASSE':([3,4,12,13,19,20,29,30,33,34,40,54,56,62,64,72,73,76,78,82,84,86,94,95,96,97,103,112,124,132,149,],[6,8,18,22,36,38,51,51,22,58,22,81,83,92,38,83,104,51,111,117,121,122,22,22,81,133,121,139,18,156,121,]),'EQUIVALENT_TO':([6,7,8,36,],[12,12,12,62,]),'SUBCLASSOF':([6,7,8,16,44,45,48,59,61,67,68,81,83,85,89,90,91,98,100,102,104,113,117,122,124,127,128,129,137,139,143,144,147,148,150,151,152,153,154,155,157,158,159,162,164,165,169,171,172,174,175,180,181,183,185,186,],[13,13,13,33,-73,-74,-83,-55,-59,-71,-72,-44,-41,-92,-58,-60,-61,-76,-79,-81,-82,-31,-45,-88,-68,-70,-62,-56,-35,-46,-47,-32,-43,-42,-87,-57,-67,-69,-63,-65,-80,-77,-78,-49,-33,-34,-48,-64,-66,-36,-50,-37,-38,-75,-40,-39,]),'PALAVRA_RESERVADA':([12,47,124,],[19,73,19,]),'ABRE_CHAVE':([12,],[20,]),'ABRE_PARENT':([13,27,33,35,40,46,56,60,61,72,81,83,87,94,95,96,99,101,103,113,117,137,139,143,144,147,148,162,164,165,169,174,175,180,181,185,186,],[26,46,26,60,26,46,84,46,46,103,-44,-41,46,26,26,132,46,46,46,-31,-45,-35,-46,-47,-32,-43,-42,-49,-33,-34,-48,-36,-50,-37,-38,-40,-39,]),'AND':([13,18,22,33,40,44,45,48,61,66,71,81,83,88,90,92,94,95,98,100,102,104,113,117,122,124,137,139,143,144,147,148,150,154,155,157,158,159,162,164,165,169,174,175,180,181,183,185,186,],[27,35,27,27,27,27,27,-83,27,94,101,-44,-41,27,27,27,27,27,-76,-79,-81,-82,-31,-45,-88,27,-35,-46,-47,-32,-43,-42,-87,27,27,-80,-77,-78,-49,-33,-34,-48,-36,-50,-37,-38,-75,-40,-39,]),'DISJOINTS':([13,16,22,24,28,33,40,44,45,48,49,59,61,67,68,81,83,85,89,90,91,94,95,98,100,102,104,113,117,122,124,127,128,129,137,139,143,144,147,148,150,151,152,153,154,155,157,158,159,162,164,165,169,171,172,174,175,180,181,183,185,186,],[29,29,29,29,-30,29,29,-73,-74,-83,-29,-55,-59,-71,-72,-44,-41,-92,-58,-60,-61,29,29,-76,-79,-81,-82,-31,-45,-88,-68,-70,-62,-56,-35,-46,-47,-32,-43,-42,-87,-57,-67,-69,-63,-65,-80,-77,-78,-49,-33,-34,-48,-64,-66,-36,-50,-37,-38,-75,-40,-39,]),'PROPRIEDADE':([13,26,27,28,31,33,35,40,46,47,60,69,81,83,94,95,103,113,115,117,118,137,138,139,141,143,144,146,147,148,161,162,163,164,165,169,174,175,180,181,184,185,186,],[31,31,47,31,53,31,31,31,69,53,31,53,-44,-41,31,31,69,-31,31,-45,31,-35,31,-46,31,-47,-32,31,-43,-42,31,-49,31,-33,-34,-48,-36,-50,-37,-38,31,-40,-39,]),'OR':([18,58,61,71,81,83,87,98,100,113,117,121,122,137,139,143,144,147,148,156,157,158,159,162,164,165,169,174,175,180,181,183,185,186,],[34,86,86,99,-44,-41,86,-76,-79,-31,-45,149,86,-35,-46,-47,-32,-43,-42,86,-80,-77,-78,-49,-33,-34,-48,-36,-50,-37,-38,-75,-40,-39,]),'CARACTERE_ESPECIAL':([22,38,51,66,81,83,107,111,113,117,137,139,176,181,],[40,64,76,95,115,118,136,138,141,146,161,163,180,184,]),'FECHA_PARENT':([28,43,44,45,48,49,67,68,70,71,81,83,87,98,100,102,104,113,117,119,120,121,122,123,125,126,127,133,134,135,137,139,143,144,147,148,150,157,158,159,162,164,165,169,170,173,174,175,179,180,181,183,185,186,],[-30,66,-73,-74,-83,-29,-71,-72,98,100,-44,-41,124,-76,-79,-81,-82,-31,-45,148,-84,-86,-88,151,154,155,-70,157,158,159,-35,-46,-47,-32,-43,-42,-87,-80,-77,-78,-49,-33,-34,-48,-85,179,-36,-50,183,-37,-38,-75,-40,-39,]),'SOME':([31,47,53,69,],[54,54,78,96,]),'COMPARADORES':([31,47,53,69,],[55,55,79,55,]),'ONLY':([31,47,69,],[56,72,56,]),'FECHA_CHAVE':([37,38,93,],[63,-91,-90,]),'INDIVIDUALS':([50,51,52,108,],[74,-17,77,-16,]),'NAMESPACE':([54,78,82,96,],[80,110,116,80,]),'CARDINALIDADE':([55,79,166,167,178,],[82,112,176,177,182,]),'VALUE':([69,],[97,]),'NOME_INDIVIDUO':([74,77,136,],[107,107,107,]),'TIPO':([80,110,116,],[113,137,144,]),'TIPO_NUMERICO':([80,116,],[114,145,]),'ABRE_COLCHETE':([113,114,145,],[140,142,168,]),'OPERADORES':([140,141,142,168,],[164,166,167,178,]),'FECHA_COLCHETE':([177,182,],[181,185,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,2,],[1,5,]),'declaracao_classe':([0,2,],[2,2,]),'tipo_classe_primaria':([6,7,8,],[9,14,15,]),'declaracao_classe_definida':([6,7,8,],[10,10,10,]),'declaracao_classe_primitiva':([6,7,8,],[11,11,11,]),'continuacao_equivalentto':([12,124,],[16,152,]),'declaracao_classe_enumerada':([12,],[17,]),'continuacao_subclassof':([13,33,40,94,95,],[21,57,65,130,131,]),'caso_ands':([13,22,33,40,44,45,61,88,90,92,94,95,124,154,155,],[23,39,23,23,67,68,91,127,128,127,23,23,153,171,172,]),'declaracao_propriedades':([13,26,28,33,40,94,95,],[24,43,49,24,24,24,24,]),'caso_disjoint_opcional':([13,16,22,24,33,40,94,95,],[25,32,41,42,25,25,25,25,]),'declaracao_existencial':([13,26,27,28,33,35,40,46,60,94,95,103,115,118,138,141,146,161,163,184,],[28,28,48,28,28,61,28,70,87,28,28,70,143,147,162,165,169,174,175,186,]),'classes_enumeradas':([20,64,],[37,93,]),'casos_parentese':([27,46,60,61,72,87,99,101,103,],[44,71,88,89,102,123,134,135,71,]),'casos_sem_parentese':([27,],[45,]),'continuacao_disjoint_opcional':([29,30,76,],[50,52,108,]),'declaracao_classe_coberta':([34,],[59,]),'classes_or':([58,61,87,122,156,],[85,90,125,150,173,]),'continuacao_individuals':([74,77,136,],[105,109,160,]),'declaracao_classe_axioma_fechamento':([84,103,],[119,119,]),'classes_or_fechamento':([84,103,149,],[120,120,170,]),'declaracao_classe_aninhada':([88,92,],[126,129,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> declaracao_classe programa','programa',2,'p_programa','analisador_semantico.py',113),
  ('programa -> declaracao_classe','programa',1,'p_programa','analisador_semantico.py',114),
  ('declaracao_classe -> PALAVRA_CLASS CLASSE tipo_classe_primaria','declaracao_classe',3,'p_declaracao_classe','analisador_semantico.py',118),
  ('declaracao_classe -> PALAVRA_CLASS error tipo_classe_primaria','declaracao_classe',3,'p_declaracao_classe_error','analisador_semantico.py',172),
  ('declaracao_classe -> error CLASSE tipo_classe_primaria','declaracao_classe',3,'p_declaracao_classe_error','analisador_semantico.py',173),
  ('tipo_classe_primaria -> declaracao_classe_definida','tipo_classe_primaria',1,'p_tipo_classe_primaria','analisador_semantico.py',184),
  ('tipo_classe_primaria -> declaracao_classe_primitiva','tipo_classe_primaria',1,'p_tipo_classe_primaria','analisador_semantico.py',185),
  ('declaracao_classe_primitiva -> SUBCLASSOF continuacao_subclassof','declaracao_classe_primitiva',2,'p_declaracao_classe_primitiva','analisador_semantico.py',193),
  ('continuacao_individuals -> NOME_INDIVIDUO','continuacao_individuals',1,'p_continuacao_individuals','analisador_semantico.py',205),
  ('continuacao_individuals -> NOME_INDIVIDUO CARACTERE_ESPECIAL continuacao_individuals','continuacao_individuals',3,'p_continuacao_individuals','analisador_semantico.py',206),
  ('caso_disjoint_opcional -> DISJOINTS continuacao_disjoint_opcional INDIVIDUALS continuacao_individuals','caso_disjoint_opcional',4,'p_caso_disjoint_opcional','analisador_semantico.py',213),
  ('caso_disjoint_opcional -> DISJOINTS continuacao_disjoint_opcional','caso_disjoint_opcional',2,'p_caso_disjoint_opcional','analisador_semantico.py',214),
  ('caso_disjoint_opcional -> error continuacao_disjoint_opcional INDIVIDUALS continuacao_individuals','caso_disjoint_opcional',4,'p_caso_disjoint_opcional_error','analisador_semantico.py',222),
  ('caso_disjoint_opcional -> DISJOINTS continuacao_disjoint_opcional error','caso_disjoint_opcional',3,'p_caso_disjoint_opcional_error','analisador_semantico.py',223),
  ('caso_disjoint_opcional -> DISJOINTS continuacao_disjoint_opcional INDIVIDUALS error','caso_disjoint_opcional',4,'p_caso_disjoint_opcional_error','analisador_semantico.py',224),
  ('continuacao_disjoint_opcional -> CLASSE CARACTERE_ESPECIAL continuacao_disjoint_opcional','continuacao_disjoint_opcional',3,'p_continuacao_disjoint_opcional','analisador_semantico.py',236),
  ('continuacao_disjoint_opcional -> CLASSE','continuacao_disjoint_opcional',1,'p_continuacao_disjoint_opcional','analisador_semantico.py',237),
  ('continuacao_subclassof -> CLASSE caso_ands','continuacao_subclassof',2,'p_continuacao_subclassof','analisador_semantico.py',243),
  ('continuacao_subclassof -> CLASSE','continuacao_subclassof',1,'p_continuacao_subclassof','analisador_semantico.py',244),
  ('continuacao_subclassof -> declaracao_propriedades','continuacao_subclassof',1,'p_continuacao_subclassof','analisador_semantico.py',245),
  ('continuacao_subclassof -> declaracao_propriedades caso_disjoint_opcional','continuacao_subclassof',2,'p_continuacao_subclassof','analisador_semantico.py',246),
  ('continuacao_subclassof -> CLASSE CARACTERE_ESPECIAL continuacao_subclassof','continuacao_subclassof',3,'p_continuacao_subclassof','analisador_semantico.py',247),
  ('continuacao_subclassof -> caso_ands','continuacao_subclassof',1,'p_continuacao_subclassof','analisador_semantico.py',248),
  ('continuacao_subclassof -> ABRE_PARENT declaracao_propriedades FECHA_PARENT','continuacao_subclassof',3,'p_continuacao_subclassof','analisador_semantico.py',249),
  ('continuacao_subclassof -> ABRE_PARENT declaracao_propriedades FECHA_PARENT AND continuacao_subclassof','continuacao_subclassof',5,'p_continuacao_subclassof','analisador_semantico.py',250),
  ('continuacao_subclassof -> ABRE_PARENT declaracao_propriedades FECHA_PARENT CARACTERE_ESPECIAL continuacao_subclassof','continuacao_subclassof',5,'p_continuacao_subclassof','analisador_semantico.py',251),
  ('continuacao_subclassof -> CLASSE caso_disjoint_opcional','continuacao_subclassof',2,'p_continuacao_subclassof','analisador_semantico.py',252),
  ('continuacao_subclassof -> caso_disjoint_opcional','continuacao_subclassof',1,'p_continuacao_subclassof','analisador_semantico.py',253),
  ('declaracao_propriedades -> declaracao_existencial declaracao_propriedades','declaracao_propriedades',2,'p_declaracao_propriedades','analisador_semantico.py',259),
  ('declaracao_propriedades -> declaracao_existencial','declaracao_propriedades',1,'p_declaracao_propriedades','analisador_semantico.py',260),
  ('declaracao_existencial -> PROPRIEDADE SOME NAMESPACE TIPO','declaracao_existencial',4,'p_declaracao_existencial','analisador_semantico.py',265),
  ('declaracao_existencial -> PROPRIEDADE COMPARADORES CARDINALIDADE NAMESPACE TIPO','declaracao_existencial',5,'p_declaracao_existencial','analisador_semantico.py',266),
  ('declaracao_existencial -> PROPRIEDADE SOME NAMESPACE TIPO ABRE_COLCHETE OPERADORES','declaracao_existencial',6,'p_declaracao_existencial','analisador_semantico.py',267),
  ('declaracao_existencial -> PROPRIEDADE SOME NAMESPACE TIPO CARACTERE_ESPECIAL declaracao_existencial','declaracao_existencial',6,'p_declaracao_existencial','analisador_semantico.py',268),
  ('declaracao_existencial -> PROPRIEDADE PROPRIEDADE SOME NAMESPACE TIPO','declaracao_existencial',5,'p_declaracao_existencial','analisador_semantico.py',269),
  ('declaracao_existencial -> PROPRIEDADE PROPRIEDADE SOME NAMESPACE TIPO CARACTERE_ESPECIAL declaracao_existencial','declaracao_existencial',7,'p_declaracao_existencial','analisador_semantico.py',270),
  ('declaracao_existencial -> PROPRIEDADE SOME NAMESPACE TIPO CARACTERE_ESPECIAL OPERADORES CARDINALIDADE CARACTERE_ESPECIAL','declaracao_existencial',8,'p_declaracao_existencial','analisador_semantico.py',271),
  ('declaracao_existencial -> PROPRIEDADE SOME NAMESPACE TIPO_NUMERICO ABRE_COLCHETE OPERADORES CARDINALIDADE FECHA_COLCHETE','declaracao_existencial',8,'p_declaracao_existencial','analisador_semantico.py',272),
  ('declaracao_existencial -> PROPRIEDADE SOME NAMESPACE TIPO_NUMERICO ABRE_COLCHETE OPERADORES CARDINALIDADE FECHA_COLCHETE CARACTERE_ESPECIAL declaracao_existencial','declaracao_existencial',10,'p_declaracao_existencial','analisador_semantico.py',273),
  ('declaracao_existencial -> PROPRIEDADE COMPARADORES CARDINALIDADE NAMESPACE TIPO_NUMERICO ABRE_COLCHETE OPERADORES CARDINALIDADE FECHA_COLCHETE','declaracao_existencial',9,'p_declaracao_existencial','analisador_semantico.py',274),
  ('declaracao_existencial -> PROPRIEDADE ONLY CLASSE','declaracao_existencial',3,'p_declaracao_existencial','analisador_semantico.py',277),
  ('declaracao_existencial -> PROPRIEDADE ONLY ABRE_PARENT declaracao_classe_axioma_fechamento FECHA_PARENT','declaracao_existencial',5,'p_declaracao_existencial','analisador_semantico.py',278),
  ('declaracao_existencial -> PROPRIEDADE ONLY CLASSE CARACTERE_ESPECIAL declaracao_existencial','declaracao_existencial',5,'p_declaracao_existencial','analisador_semantico.py',279),
  ('declaracao_existencial -> PROPRIEDADE SOME CLASSE','declaracao_existencial',3,'p_declaracao_existencial','analisador_semantico.py',281),
  ('declaracao_existencial -> PROPRIEDADE COMPARADORES CARDINALIDADE CLASSE','declaracao_existencial',4,'p_declaracao_existencial','analisador_semantico.py',283),
  ('declaracao_existencial -> PROPRIEDADE PROPRIEDADE COMPARADORES CARDINALIDADE CLASSE','declaracao_existencial',5,'p_declaracao_existencial','analisador_semantico.py',285),
  ('declaracao_existencial -> PROPRIEDADE SOME CLASSE CARACTERE_ESPECIAL declaracao_existencial','declaracao_existencial',5,'p_declaracao_existencial','analisador_semantico.py',286),
  ('declaracao_existencial -> PROPRIEDADE COMPARADORES CARDINALIDADE CLASSE CARACTERE_ESPECIAL declaracao_existencial','declaracao_existencial',6,'p_declaracao_existencial','analisador_semantico.py',288),
  ('declaracao_existencial -> PROPRIEDADE PROPRIEDADE SOME CLASSE CARACTERE_ESPECIAL declaracao_existencial','declaracao_existencial',6,'p_declaracao_existencial','analisador_semantico.py',289),
  ('declaracao_existencial -> PROPRIEDADE PROPRIEDADE COMPARADORES CARDINALIDADE CLASSE CARACTERE_ESPECIAL declaracao_existencial','declaracao_existencial',7,'p_declaracao_existencial','analisador_semantico.py',291),
  ('declaracao_classe_definida -> EQUIVALENT_TO continuacao_equivalentto caso_disjoint_opcional','declaracao_classe_definida',3,'p_declaracao_classe_definida','analisador_semantico.py',360),
  ('declaracao_classe_definida -> EQUIVALENT_TO continuacao_equivalentto','declaracao_classe_definida',2,'p_declaracao_classe_definida','analisador_semantico.py',361),
  ('declaracao_classe_definida -> EQUIVALENT_TO declaracao_classe_enumerada','declaracao_classe_definida',2,'p_declaracao_classe_definida','analisador_semantico.py',362),
  ('declaracao_classe_definida -> EQUIVALENT_TO continuacao_equivalentto SUBCLASSOF continuacao_subclassof','declaracao_classe_definida',4,'p_declaracao_classe_definida','analisador_semantico.py',363),
  ('continuacao_equivalentto -> CLASSE OR declaracao_classe_coberta','continuacao_equivalentto',3,'p_continuacao_equivalentto','analisador_semantico.py',370),
  ('continuacao_equivalentto -> PALAVRA_RESERVADA CLASSE EQUIVALENT_TO CLASSE declaracao_classe_aninhada','continuacao_equivalentto',5,'p_continuacao_equivalentto','analisador_semantico.py',371),
  ('continuacao_equivalentto -> CLASSE AND ABRE_PARENT declaracao_existencial casos_parentese FECHA_PARENT','continuacao_equivalentto',6,'p_continuacao_equivalentto','analisador_semantico.py',372),
  ('continuacao_equivalentto -> CLASSE AND declaracao_existencial casos_parentese','continuacao_equivalentto',4,'p_continuacao_equivalentto','analisador_semantico.py',373),
  ('continuacao_equivalentto -> CLASSE AND declaracao_existencial','continuacao_equivalentto',3,'p_continuacao_equivalentto','analisador_semantico.py',374),
  ('continuacao_equivalentto -> CLASSE AND declaracao_existencial classes_or','continuacao_equivalentto',4,'p_continuacao_equivalentto','analisador_semantico.py',375),
  ('continuacao_equivalentto -> CLASSE AND declaracao_existencial caso_ands','continuacao_equivalentto',4,'p_continuacao_equivalentto','analisador_semantico.py',376),
  ('continuacao_equivalentto -> CLASSE AND declaracao_existencial classes_or caso_ands','continuacao_equivalentto',5,'p_continuacao_equivalentto','analisador_semantico.py',377),
  ('continuacao_equivalentto -> CLASSE AND ABRE_PARENT declaracao_existencial classes_or FECHA_PARENT','continuacao_equivalentto',6,'p_continuacao_equivalentto','analisador_semantico.py',378),
  ('continuacao_equivalentto -> CLASSE AND ABRE_PARENT declaracao_existencial classes_or FECHA_PARENT caso_ands','continuacao_equivalentto',7,'p_continuacao_equivalentto','analisador_semantico.py',379),
  ('continuacao_equivalentto -> CLASSE AND ABRE_PARENT casos_parentese declaracao_classe_aninhada FECHA_PARENT','continuacao_equivalentto',6,'p_continuacao_equivalentto','analisador_semantico.py',380),
  ('continuacao_equivalentto -> CLASSE AND ABRE_PARENT casos_parentese declaracao_classe_aninhada FECHA_PARENT caso_ands','continuacao_equivalentto',7,'p_continuacao_equivalentto','analisador_semantico.py',381),
  ('continuacao_equivalentto -> CLASSE AND ABRE_PARENT declaracao_existencial FECHA_PARENT continuacao_equivalentto','continuacao_equivalentto',6,'p_continuacao_equivalentto','analisador_semantico.py',382),
  ('continuacao_equivalentto -> CLASSE AND ABRE_PARENT declaracao_existencial FECHA_PARENT','continuacao_equivalentto',5,'p_continuacao_equivalentto','analisador_semantico.py',383),
  ('continuacao_equivalentto -> CLASSE AND ABRE_PARENT declaracao_existencial FECHA_PARENT caso_ands','continuacao_equivalentto',6,'p_continuacao_equivalentto','analisador_semantico.py',384),
  ('declaracao_classe_aninhada -> caso_ands','declaracao_classe_aninhada',1,'p_declaracao_classe_aninhada','analisador_semantico.py',389),
  ('caso_ands -> AND casos_parentese caso_ands','caso_ands',3,'p_caso_ands','analisador_semantico.py',394),
  ('caso_ands -> AND casos_sem_parentese caso_ands','caso_ands',3,'p_caso_ands','analisador_semantico.py',395),
  ('caso_ands -> AND casos_parentese','caso_ands',2,'p_caso_ands','analisador_semantico.py',396),
  ('caso_ands -> AND casos_sem_parentese','caso_ands',2,'p_caso_ands','analisador_semantico.py',397),
  ('casos_parentese -> ABRE_PARENT PROPRIEDADE SOME ABRE_PARENT CLASSE classes_or FECHA_PARENT FECHA_PARENT','casos_parentese',8,'p_casos_parentese','analisador_semantico.py',402),
  ('casos_parentese -> ABRE_PARENT declaracao_existencial FECHA_PARENT','casos_parentese',3,'p_casos_parentese','analisador_semantico.py',403),
  ('casos_parentese -> ABRE_PARENT casos_parentese OR casos_parentese FECHA_PARENT','casos_parentese',5,'p_casos_parentese','analisador_semantico.py',404),
  ('casos_parentese -> ABRE_PARENT casos_parentese AND casos_parentese FECHA_PARENT','casos_parentese',5,'p_casos_parentese','analisador_semantico.py',405),
  ('casos_parentese -> ABRE_PARENT casos_parentese FECHA_PARENT','casos_parentese',3,'p_casos_parentese','analisador_semantico.py',406),
  ('casos_parentese -> ABRE_PARENT PROPRIEDADE VALUE CLASSE FECHA_PARENT','casos_parentese',5,'p_casos_parentese','analisador_semantico.py',407),
  ('casos_sem_parentese -> PROPRIEDADE ONLY casos_parentese','casos_sem_parentese',3,'p_casos_sem_parentese','analisador_semantico.py',412),
  ('casos_sem_parentese -> PROPRIEDADE PALAVRA_RESERVADA CLASSE','casos_sem_parentese',3,'p_casos_sem_parentese','analisador_semantico.py',413),
  ('casos_sem_parentese -> declaracao_existencial','casos_sem_parentese',1,'p_casos_sem_parentese','analisador_semantico.py',414),
  ('declaracao_classe_axioma_fechamento -> classes_or_fechamento','declaracao_classe_axioma_fechamento',1,'p_declaracao_classe_axioma_fechamento','analisador_semantico.py',421),
  ('classes_or_fechamento -> CLASSE OR classes_or_fechamento','classes_or_fechamento',3,'p_classes_or_fechamento','analisador_semantico.py',429),
  ('classes_or_fechamento -> CLASSE','classes_or_fechamento',1,'p_classes_or_fechamento','analisador_semantico.py',430),
  ('classes_or -> OR CLASSE classes_or','classes_or',3,'p_classes_or','analisador_semantico.py',442),
  ('classes_or -> OR CLASSE','classes_or',2,'p_classes_or','analisador_semantico.py',443),
  ('declaracao_classe_enumerada -> ABRE_CHAVE classes_enumeradas FECHA_CHAVE','declaracao_classe_enumerada',3,'p_declaracao_classe_enumerada','analisador_semantico.py',450),
  ('classes_enumeradas -> CLASSE CARACTERE_ESPECIAL classes_enumeradas','classes_enumeradas',3,'p_classes_enumeradas','analisador_semantico.py',456),
  ('classes_enumeradas -> CLASSE','classes_enumeradas',1,'p_classes_enumeradas','analisador_semantico.py',457),
  ('declaracao_classe_coberta -> CLASSE classes_or','declaracao_classe_coberta',2,'p_declaracao_classe_coberta','analisador_semantico.py',464),
]
