
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ABRE_CHAVE ABRE_PARENT AND CARACTERE_ESPECIAL CARDINALIDADE CLASSE COMPARADORES DISJOINTCLASSES DISJOINTWITH EQUIVALENT_TO FECHA_CHAVE FECHA_PARENT INDIVIDUALS NAMESPACE NOME_INDIVIDUO ONLY OPERADORES OR PALAVRA_RESERVADA PROPRIEDADE SOME SUBCLASSOF TIPO VALUEprograma : tipo_classe_primaria programa\n                | tipo_classe_primaria\n    tipo_classe_primaria : declaracao_classe_definida\n                         | declaracao_classe_primitiva\n    \n    declaracao_classe_primitiva : PALAVRA_RESERVADA CLASSE SUBCLASSOF continuacao_subclassof caso_disjoint_opcional caso_individuals_opcional\n                                | PALAVRA_RESERVADA CLASSE SUBCLASSOF continuacao_subclassof caso_individuals_opcional caso_disjoint_opcional\n                                | PALAVRA_RESERVADA CLASSE SUBCLASSOF continuacao_subclassof caso_disjoint_opcional\n                                | PALAVRA_RESERVADA CLASSE SUBCLASSOF continuacao_subclassof caso_individuals_opcional\n                                | PALAVRA_RESERVADA CLASSE SUBCLASSOF continuacao_subclassof\n    \n    caso_individuals_opcional : INDIVIDUALS NOME_INDIVIDUO\n                              | INDIVIDUALS NOME_INDIVIDUO CARACTERE_ESPECIAL continuacao_individuals\n    \n    continuacao_individuals : NOME_INDIVIDUO \n                            | NOME_INDIVIDUO CARACTERE_ESPECIAL continuacao_individuals\n    \n    caso_disjoint_opcional : CLASSE CARACTERE_ESPECIAL caso_disjoint_opcional\n                         |  CLASSE\n                         |  DISJOINTCLASSES CLASSE \n                         |  DISJOINTCLASSES CLASSE CARACTERE_ESPECIAL caso_disjoint_opcional\n                         |  DISJOINTWITH CLASSE \n                         |  DISJOINTWITH CLASSE CARACTERE_ESPECIAL\n                         |  DISJOINTWITH CLASSE CARACTERE_ESPECIAL caso_disjoint_opcional\n    continuacao_subclassof : PROPRIEDADE SOME CLASSE\n                   | CLASSE CARACTERE_ESPECIAL declaracao_classe_axioma_fechamento\n                   | PROPRIEDADE SOME NAMESPACE TIPO\n                   | PROPRIEDADE SOME CLASSE CARACTERE_ESPECIAL continuacao_subclassof \n                   | PROPRIEDADE SOME NAMESPACE TIPO CARACTERE_ESPECIAL continuacao_subclassof\n                   | CLASSE caso_ands\n                   | CLASSE\n    \n    declaracao_classe_definida : PALAVRA_RESERVADA CLASSE EQUIVALENT_TO continuacao_equivalentto caso_individuals_opcional\n                               | PALAVRA_RESERVADA CLASSE EQUIVALENT_TO continuacao_equivalentto\n                               | PALAVRA_RESERVADA CLASSE EQUIVALENT_TO declaracao_classe_enumerada\n                               | PALAVRA_RESERVADA CLASSE EQUIVALENT_TO continuacao_equivalentto SUBCLASSOF continuacao_subclassof\n                               | PALAVRA_RESERVADA CLASSE continuacao_subclassof EQUIVALENT_TO continuacao_equivalentto\n    \n        continuacao_equivalentto : CLASSE OR declaracao_classe_coberta\n                                 | PALAVRA_RESERVADA CLASSE EQUIVALENT_TO CLASSE declaracao_classe_aninhada \n                                 | CLASSE AND PROPRIEDADE SOME_ONLY casos_parentese\n                                 | CLASSE AND PROPRIEDADE SOME_ONLY CLASSE casos_parentese \n                                 | CLASSE AND PROPRIEDADE SOME_ONLY classes_or caso_ands\n                                 | CLASSE AND PROPRIEDADE SOME_ONLY classes_or \n                                 | CLASSE AND ABRE_PARENT PROPRIEDADE SOME_ONLY casos_parentese FECHA_PARENT\n                                 | CLASSE AND ABRE_PARENT PROPRIEDADE SOME_ONLY classes_or FECHA_PARENT \n                                 | CLASSE AND ABRE_PARENT casos_parentese declaracao_classe_aninhada FECHA_PARENT\n                                 | CLASSE AND ABRE_PARENT casos_parentese declaracao_classe_aninhada FECHA_PARENT caso_ands\n                                 | CLASSE AND ABRE_PARENT PROPRIEDADE SOME_ONLY classes_or FECHA_PARENT caso_ands\n                                 | CLASSE AND ABRE_PARENT PROPRIEDADE SOME_ONLY NAMESPACE TIPO CARACTERE_ESPECIAL OPERADORES CARDINALIDADE CARACTERE_ESPECIAL FECHA_PARENT\n                                        \n    \n    declaracao_classe_aninhada : caso_ands\n    \n    caso_ands : AND casos_parentese caso_ands\n              | AND casos_sem_parentese caso_ands\n              | AND casos_parentese\n              | AND casos_sem_parentese    \n    \n    casos_parentese :   ABRE_PARENT PROPRIEDADE SOME_ONLY CLASSE FECHA_PARENT\n                        | ABRE_PARENT PROPRIEDADE SOME_ONLY ABRE_PARENT classes_or FECHA_PARENT FECHA_PARENT\n                        | ABRE_PARENT PROPRIEDADE COMPARADORES CARDINALIDADE CLASSE FECHA_PARENT\n                        | ABRE_PARENT casos_parentese OR casos_parentese FECHA_PARENT\n                        | ABRE_PARENT casos_parentese AND casos_parentese FECHA_PARENT\n                        | ABRE_PARENT casos_parentese FECHA_PARENT\n                        | ABRE_PARENT PROPRIEDADE VALUE CLASSE FECHA_PARENT\n    \n    casos_sem_parentese :  PROPRIEDADE SOME_ONLY CLASSE \n                        |  PROPRIEDADE ONLY casos_parentese \n                        |  PROPRIEDADE PALAVRA_RESERVADA CLASSE \n                        |  PROPRIEDADE COMPARADORES CARDINALIDADE CLASSE \n    \n    declaracao_classe_axioma_fechamento : regras_classe_axioma_fechamento\n    \n    regras_classe_axioma_fechamento : PROPRIEDADE SOME_ONLY CLASSE\n                                    | PROPRIEDADE rec_propriedade SOME_ONLY CLASSE\n                                    | PROPRIEDADE rec_propriedade SOME_ONLY CLASSE CARACTERE_ESPECIAL regras_classe_axioma_fechamento\n                                    | PROPRIEDADE SOME_ONLY CLASSE CARACTERE_ESPECIAL regras_classe_axioma_fechamento\n                                    | ABRE_PARENT PROPRIEDADE SOME_ONLY CLASSE FECHA_PARENT\n                                    | ABRE_PARENT PROPRIEDADE SOME_ONLY CLASSE FECHA_PARENT AND regras_classe_axioma_fechamento\n                                    | ABRE_PARENT PROPRIEDADE SOME_ONLY CLASSE FECHA_PARENT CARACTERE_ESPECIAL regras_classe_axioma_fechamento\n\n                                    | PROPRIEDADE rec_propriedade COMPARADORES CARDINALIDADE CLASSE\n                                    | PROPRIEDADE rec_propriedade COMPARADORES CARDINALIDADE CLASSE CARACTERE_ESPECIAL regras_classe_axioma_fechamento\n                                    | PROPRIEDADE COMPARADORES CARDINALIDADE CLASSE \n                                    | PROPRIEDADE COMPARADORES CARDINALIDADE CLASSE CARACTERE_ESPECIAL regras_classe_axioma_fechamento\n                                    \n                                    | ABRE_PARENT PROPRIEDADE COMPARADORES CARDINALIDADE CLASSE FECHA_PARENT\n                                    | ABRE_PARENT PROPRIEDADE COMPARADORES CARDINALIDADE CLASSE FECHA_PARENT CARACTERE_ESPECIAL regras_classe_axioma_fechamento\n                                    | ABRE_PARENT PROPRIEDADE COMPARADORES CARDINALIDADE CLASSE FECHA_PARENT AND regras_classe_axioma_fechamento\n                                    | ABRE_PARENT PROPRIEDADE COMPARADORES CARDINALIDADE CLASSE CARACTERE_ESPECIAL FECHA_PARENT regras_classe_axioma_fechamento\n                                    | ABRE_PARENT PROPRIEDADE rec_propriedade COMPARADORES CARDINALIDADE CLASSE FECHA_PARENT\n                                    | ABRE_PARENT PROPRIEDADE rec_propriedade COMPARADORES CARDINALIDADE CLASSE CARACTERE_ESPECIAL FECHA_PARENT regras_classe_axioma_fechamento\n                                        \n    \n    rec_propriedade : PROPRIEDADE\n                    | PROPRIEDADE PROPRIEDADE\n    \n    SOME_ONLY : SOME\n              | ONLY\n    \n    classes_or : CLASSE OR classes_or\n               | CLASSE\n               | ABRE_PARENT classes_or FECHA_PARENT\n    \n    declaracao_classe_enumerada : ABRE_CHAVE classes_enumeradas FECHA_CHAVE\n    \n    classes_enumeradas : CLASSE CARACTERE_ESPECIAL classes_enumeradas\n                       | CLASSE\n    \n    declaracao_classe_coberta : classes_or \n    '
    
_lr_action_items = {'PALAVRA_RESERVADA':([0,2,3,4,8,9,14,18,19,21,22,24,25,28,29,31,35,40,41,42,45,46,55,56,64,65,66,70,71,72,75,76,77,78,80,82,93,95,96,97,107,109,110,113,115,125,126,127,128,129,130,131,132,136,137,138,139,140,141,143,145,149,151,152,153,154,155,159,161,163,166,170,171,172,174,175,176,177,178,182,184,185,187,188,189,192,195,],[5,5,-3,-4,-27,16,-26,-29,-30,-9,16,-22,-61,-48,-49,61,-28,-15,-7,-8,-32,-21,-46,-47,-84,-33,-89,-31,-10,-86,-5,-6,-16,-18,-23,-62,-55,-57,-58,-59,-14,-19,-24,-63,-71,-60,-34,-45,-83,-85,-84,-35,-38,-12,-11,-17,-20,-25,-65,-69,-66,-50,-56,-53,-54,-36,-37,-41,-64,-72,-73,-52,-39,-40,-42,-13,-70,-67,-68,-77,-51,-43,-74,-75,-76,-78,-44,]),'$end':([1,2,3,4,6,8,14,18,19,21,24,25,28,29,35,40,41,42,45,46,55,56,64,65,66,70,71,72,75,76,77,78,80,82,93,95,96,97,107,109,110,113,115,125,126,127,128,129,130,131,132,136,137,138,139,140,141,143,145,149,151,152,153,154,155,159,161,163,166,170,171,172,174,175,176,177,178,182,184,185,187,188,189,192,195,],[0,-2,-3,-4,-1,-27,-26,-29,-30,-9,-22,-61,-48,-49,-28,-15,-7,-8,-32,-21,-46,-47,-84,-33,-89,-31,-10,-86,-5,-6,-16,-18,-23,-62,-55,-57,-58,-59,-14,-19,-24,-63,-71,-60,-34,-45,-83,-85,-84,-35,-38,-12,-11,-17,-20,-25,-65,-69,-66,-50,-56,-53,-54,-36,-37,-41,-64,-72,-73,-52,-39,-40,-42,-13,-70,-67,-68,-77,-51,-43,-74,-75,-76,-78,-44,]),'CLASSE':([5,7,8,9,10,14,16,20,21,22,23,24,25,28,29,33,36,42,43,44,46,49,52,53,55,56,59,60,61,63,67,71,73,74,79,80,82,83,85,86,89,91,93,95,96,97,98,100,102,108,109,110,111,113,114,115,117,119,121,125,133,134,136,137,140,141,143,145,147,149,151,152,153,161,163,166,170,175,176,177,178,182,184,187,188,189,192,],[7,8,-27,17,8,-26,32,39,40,17,46,-22,-61,-48,-49,64,8,40,77,78,-21,82,-81,-82,-46,-47,95,-82,97,99,64,-10,39,40,8,-23,-62,113,115,116,120,122,-55,-57,-58,-59,125,64,130,40,40,-24,8,-63,143,-71,146,64,150,-60,64,64,-12,-11,-25,-65,-69,-66,168,-50,-56,-53,-54,-64,-72,-73,-52,-13,-70,-67,-68,-77,-51,-74,-75,-76,-78,]),'EQUIVALENT_TO':([7,8,11,14,24,25,28,29,32,46,55,56,80,82,93,95,96,97,110,113,115,125,140,141,143,145,149,151,152,153,161,163,166,170,176,177,178,182,184,187,188,189,192,],[9,-27,22,-26,-22,-61,-48,-49,63,-21,-46,-47,-23,-62,-55,-57,-58,-59,-24,-63,-71,-60,-25,-65,-69,-66,-50,-56,-53,-54,-64,-72,-73,-52,-70,-67,-68,-77,-51,-74,-75,-76,-78,]),'SUBCLASSOF':([7,18,28,29,55,56,64,65,66,93,95,96,97,125,126,127,128,129,130,131,132,149,151,152,153,154,155,159,170,171,172,174,184,185,195,],[10,36,-48,-49,-46,-47,-84,-33,-89,-55,-57,-58,-59,-60,-34,-45,-83,-85,-84,-35,-38,-50,-56,-53,-54,-36,-37,-41,-52,-39,-40,-42,-51,-43,-44,]),'PROPRIEDADE':([7,10,13,15,26,27,30,34,36,48,54,69,79,111,112,133,142,144,162,164,165,179,180,181,190,],[12,12,26,31,48,54,57,68,12,81,48,103,12,12,26,57,26,26,26,26,26,26,26,26,26,]),'CARACTERE_ESPECIAL':([8,39,40,46,71,77,78,80,82,113,115,136,143,145,146,166,168,173,193,],[13,73,74,79,105,108,109,111,112,142,144,160,162,165,167,179,183,186,194,]),'DISJOINTCLASSES':([8,14,21,24,25,28,29,42,46,55,56,71,74,80,82,93,95,96,97,108,109,110,113,115,125,136,137,140,141,143,145,149,151,152,153,161,163,166,170,175,176,177,178,182,184,187,188,189,192,],[-27,-26,43,-22,-61,-48,-49,43,-21,-46,-47,-10,43,-23,-62,-55,-57,-58,-59,43,43,-24,-63,-71,-60,-12,-11,-25,-65,-69,-66,-50,-56,-53,-54,-64,-72,-73,-52,-13,-70,-67,-68,-77,-51,-74,-75,-76,-78,]),'DISJOINTWITH':([8,14,21,24,25,28,29,42,46,55,56,71,74,80,82,93,95,96,97,108,109,110,113,115,125,136,137,140,141,143,145,149,151,152,153,161,163,166,170,175,176,177,178,182,184,187,188,189,192,],[-27,-26,44,-22,-61,-48,-49,44,-21,-46,-47,-10,44,-23,-62,-55,-57,-58,-59,44,44,-24,-63,-71,-60,-12,-11,-25,-65,-69,-66,-50,-56,-53,-54,-64,-72,-73,-52,-13,-70,-67,-68,-77,-51,-74,-75,-76,-78,]),'INDIVIDUALS':([8,14,18,21,24,25,28,29,40,41,46,55,56,64,65,66,77,78,80,82,93,95,96,97,107,109,110,113,115,125,126,127,128,129,130,131,132,138,139,140,141,143,145,149,151,152,153,154,155,159,161,163,166,170,171,172,174,176,177,178,182,184,185,187,188,189,192,195,],[-27,-26,37,37,-22,-61,-48,-49,-15,37,-21,-46,-47,-84,-33,-89,-16,-18,-23,-62,-55,-57,-58,-59,-14,-19,-24,-63,-71,-60,-34,-45,-83,-85,-84,-35,-38,-17,-20,-25,-65,-69,-66,-50,-56,-53,-54,-36,-37,-41,-64,-72,-73,-52,-39,-40,-42,-70,-67,-68,-77,-51,-43,-74,-75,-76,-78,-44,]),'AND':([8,17,28,29,58,64,93,95,96,97,99,104,125,128,129,130,132,145,149,151,152,153,159,166,170,172,184,],[15,34,15,15,94,-84,-55,-57,-58,-59,15,15,-60,-83,-85,-84,15,164,-50,-56,-53,-54,15,180,-52,15,-51,]),'ABRE_CHAVE':([9,],[20,]),'SOME':([12,26,31,48,50,54,57,68,81,103,],[23,52,52,-79,52,52,52,52,-80,52,]),'ABRE_PARENT':([13,15,30,33,34,52,53,60,67,69,89,92,94,100,102,112,119,130,133,134,142,144,162,164,165,179,180,181,190,],[27,30,30,67,69,-81,-82,30,67,30,119,30,30,67,133,27,67,30,133,133,27,27,27,27,27,27,27,27,27,]),'OR':([17,58,64,93,130,149,151,152,153,170,184,],[33,92,100,-55,100,-50,-56,-53,-54,-52,-51,]),'NAMESPACE':([23,52,53,134,],[47,-81,-82,158,]),'COMPARADORES':([26,31,48,50,54,57,81,88,],[51,62,-79,84,87,90,-80,118,]),'ONLY':([26,31,48,50,54,57,68,81,103,],[53,60,-79,53,53,53,53,-80,53,]),'FECHA_PARENT':([28,29,55,56,58,64,93,95,96,97,101,116,120,122,123,124,125,127,128,129,135,146,148,149,150,151,152,153,156,157,167,168,169,170,183,184,194,],[-48,-49,-46,-47,93,-84,-55,-57,-58,-59,129,145,149,151,152,153,-60,-45,-83,-85,159,166,169,-50,170,-56,-53,-54,171,172,181,182,184,-52,190,-51,195,]),'NOME_INDIVIDUO':([37,105,160,],[71,136,136,]),'FECHA_CHAVE':([38,39,106,],[72,-88,-87,]),'TIPO':([47,158,],[80,173,]),'CARDINALIDADE':([51,62,84,87,90,118,191,],[85,98,114,117,121,147,193,]),'VALUE':([57,],[91,]),'OPERADORES':([186,],[191,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,2,],[1,6,]),'tipo_classe_primaria':([0,2,],[2,2,]),'declaracao_classe_definida':([0,2,],[3,3,]),'declaracao_classe_primitiva':([0,2,],[4,4,]),'continuacao_subclassof':([7,10,36,79,111,],[11,21,70,110,140,]),'caso_ands':([8,28,29,99,104,132,159,172,],[14,55,56,127,127,155,174,185,]),'continuacao_equivalentto':([9,22,],[18,45,]),'declaracao_classe_enumerada':([9,],[19,]),'declaracao_classe_axioma_fechamento':([13,],[24,]),'regras_classe_axioma_fechamento':([13,112,142,144,162,164,165,179,180,181,190,],[25,141,161,163,176,177,178,187,188,189,192,]),'casos_parentese':([15,30,60,69,92,94,102,130,133,134,],[28,58,96,104,123,124,131,154,58,156,]),'casos_sem_parentese':([15,],[29,]),'caso_individuals_opcional':([18,21,41,],[35,42,75,]),'classes_enumeradas':([20,73,],[38,106,]),'caso_disjoint_opcional':([21,42,74,108,109,],[41,76,107,138,139,]),'SOME_ONLY':([26,31,50,54,57,68,103,],[49,59,83,86,89,102,134,]),'rec_propriedade':([26,54,],[50,88,]),'declaracao_classe_coberta':([33,],[65,]),'classes_or':([33,67,100,102,119,133,134,],[66,101,128,132,148,101,157,]),'declaracao_classe_aninhada':([99,104,],[126,135,]),'continuacao_individuals':([105,160,],[137,175,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> tipo_classe_primaria programa','programa',2,'p_programa','analisador_sintatico.py',95),
  ('programa -> tipo_classe_primaria','programa',1,'p_programa','analisador_sintatico.py',96),
  ('tipo_classe_primaria -> declaracao_classe_definida','tipo_classe_primaria',1,'p_tipo_classe_primaria','analisador_sintatico.py',100),
  ('tipo_classe_primaria -> declaracao_classe_primitiva','tipo_classe_primaria',1,'p_tipo_classe_primaria','analisador_sintatico.py',101),
  ('declaracao_classe_primitiva -> PALAVRA_RESERVADA CLASSE SUBCLASSOF continuacao_subclassof caso_disjoint_opcional caso_individuals_opcional','declaracao_classe_primitiva',6,'p_declaracao_classe_primitiva','analisador_sintatico.py',109),
  ('declaracao_classe_primitiva -> PALAVRA_RESERVADA CLASSE SUBCLASSOF continuacao_subclassof caso_individuals_opcional caso_disjoint_opcional','declaracao_classe_primitiva',6,'p_declaracao_classe_primitiva','analisador_sintatico.py',110),
  ('declaracao_classe_primitiva -> PALAVRA_RESERVADA CLASSE SUBCLASSOF continuacao_subclassof caso_disjoint_opcional','declaracao_classe_primitiva',5,'p_declaracao_classe_primitiva','analisador_sintatico.py',111),
  ('declaracao_classe_primitiva -> PALAVRA_RESERVADA CLASSE SUBCLASSOF continuacao_subclassof caso_individuals_opcional','declaracao_classe_primitiva',5,'p_declaracao_classe_primitiva','analisador_sintatico.py',112),
  ('declaracao_classe_primitiva -> PALAVRA_RESERVADA CLASSE SUBCLASSOF continuacao_subclassof','declaracao_classe_primitiva',4,'p_declaracao_classe_primitiva','analisador_sintatico.py',113),
  ('caso_individuals_opcional -> INDIVIDUALS NOME_INDIVIDUO','caso_individuals_opcional',2,'p_caso_individuals_opcional','analisador_sintatico.py',122),
  ('caso_individuals_opcional -> INDIVIDUALS NOME_INDIVIDUO CARACTERE_ESPECIAL continuacao_individuals','caso_individuals_opcional',4,'p_caso_individuals_opcional','analisador_sintatico.py',123),
  ('continuacao_individuals -> NOME_INDIVIDUO','continuacao_individuals',1,'p_continuacao_individuals','analisador_sintatico.py',128),
  ('continuacao_individuals -> NOME_INDIVIDUO CARACTERE_ESPECIAL continuacao_individuals','continuacao_individuals',3,'p_continuacao_individuals','analisador_sintatico.py',129),
  ('caso_disjoint_opcional -> CLASSE CARACTERE_ESPECIAL caso_disjoint_opcional','caso_disjoint_opcional',3,'p_caso_disjoint_opcional','analisador_sintatico.py',134),
  ('caso_disjoint_opcional -> CLASSE','caso_disjoint_opcional',1,'p_caso_disjoint_opcional','analisador_sintatico.py',135),
  ('caso_disjoint_opcional -> DISJOINTCLASSES CLASSE','caso_disjoint_opcional',2,'p_caso_disjoint_opcional','analisador_sintatico.py',136),
  ('caso_disjoint_opcional -> DISJOINTCLASSES CLASSE CARACTERE_ESPECIAL caso_disjoint_opcional','caso_disjoint_opcional',4,'p_caso_disjoint_opcional','analisador_sintatico.py',137),
  ('caso_disjoint_opcional -> DISJOINTWITH CLASSE','caso_disjoint_opcional',2,'p_caso_disjoint_opcional','analisador_sintatico.py',138),
  ('caso_disjoint_opcional -> DISJOINTWITH CLASSE CARACTERE_ESPECIAL','caso_disjoint_opcional',3,'p_caso_disjoint_opcional','analisador_sintatico.py',139),
  ('caso_disjoint_opcional -> DISJOINTWITH CLASSE CARACTERE_ESPECIAL caso_disjoint_opcional','caso_disjoint_opcional',4,'p_caso_disjoint_opcional','analisador_sintatico.py',140),
  ('continuacao_subclassof -> PROPRIEDADE SOME CLASSE','continuacao_subclassof',3,'p_continuacao_subclassof','analisador_sintatico.py',144),
  ('continuacao_subclassof -> CLASSE CARACTERE_ESPECIAL declaracao_classe_axioma_fechamento','continuacao_subclassof',3,'p_continuacao_subclassof','analisador_sintatico.py',145),
  ('continuacao_subclassof -> PROPRIEDADE SOME NAMESPACE TIPO','continuacao_subclassof',4,'p_continuacao_subclassof','analisador_sintatico.py',146),
  ('continuacao_subclassof -> PROPRIEDADE SOME CLASSE CARACTERE_ESPECIAL continuacao_subclassof','continuacao_subclassof',5,'p_continuacao_subclassof','analisador_sintatico.py',147),
  ('continuacao_subclassof -> PROPRIEDADE SOME NAMESPACE TIPO CARACTERE_ESPECIAL continuacao_subclassof','continuacao_subclassof',6,'p_continuacao_subclassof','analisador_sintatico.py',148),
  ('continuacao_subclassof -> CLASSE caso_ands','continuacao_subclassof',2,'p_continuacao_subclassof','analisador_sintatico.py',149),
  ('continuacao_subclassof -> CLASSE','continuacao_subclassof',1,'p_continuacao_subclassof','analisador_sintatico.py',150),
  ('declaracao_classe_definida -> PALAVRA_RESERVADA CLASSE EQUIVALENT_TO continuacao_equivalentto caso_individuals_opcional','declaracao_classe_definida',5,'p_declaracao_classe_definida','analisador_sintatico.py',159),
  ('declaracao_classe_definida -> PALAVRA_RESERVADA CLASSE EQUIVALENT_TO continuacao_equivalentto','declaracao_classe_definida',4,'p_declaracao_classe_definida','analisador_sintatico.py',160),
  ('declaracao_classe_definida -> PALAVRA_RESERVADA CLASSE EQUIVALENT_TO declaracao_classe_enumerada','declaracao_classe_definida',4,'p_declaracao_classe_definida','analisador_sintatico.py',161),
  ('declaracao_classe_definida -> PALAVRA_RESERVADA CLASSE EQUIVALENT_TO continuacao_equivalentto SUBCLASSOF continuacao_subclassof','declaracao_classe_definida',6,'p_declaracao_classe_definida','analisador_sintatico.py',162),
  ('declaracao_classe_definida -> PALAVRA_RESERVADA CLASSE continuacao_subclassof EQUIVALENT_TO continuacao_equivalentto','declaracao_classe_definida',5,'p_declaracao_classe_definida','analisador_sintatico.py',163),
  ('continuacao_equivalentto -> CLASSE OR declaracao_classe_coberta','continuacao_equivalentto',3,'p_continuacao_equivalentto','analisador_sintatico.py',179),
  ('continuacao_equivalentto -> PALAVRA_RESERVADA CLASSE EQUIVALENT_TO CLASSE declaracao_classe_aninhada','continuacao_equivalentto',5,'p_continuacao_equivalentto','analisador_sintatico.py',180),
  ('continuacao_equivalentto -> CLASSE AND PROPRIEDADE SOME_ONLY casos_parentese','continuacao_equivalentto',5,'p_continuacao_equivalentto','analisador_sintatico.py',181),
  ('continuacao_equivalentto -> CLASSE AND PROPRIEDADE SOME_ONLY CLASSE casos_parentese','continuacao_equivalentto',6,'p_continuacao_equivalentto','analisador_sintatico.py',182),
  ('continuacao_equivalentto -> CLASSE AND PROPRIEDADE SOME_ONLY classes_or caso_ands','continuacao_equivalentto',6,'p_continuacao_equivalentto','analisador_sintatico.py',183),
  ('continuacao_equivalentto -> CLASSE AND PROPRIEDADE SOME_ONLY classes_or','continuacao_equivalentto',5,'p_continuacao_equivalentto','analisador_sintatico.py',184),
  ('continuacao_equivalentto -> CLASSE AND ABRE_PARENT PROPRIEDADE SOME_ONLY casos_parentese FECHA_PARENT','continuacao_equivalentto',7,'p_continuacao_equivalentto','analisador_sintatico.py',185),
  ('continuacao_equivalentto -> CLASSE AND ABRE_PARENT PROPRIEDADE SOME_ONLY classes_or FECHA_PARENT','continuacao_equivalentto',7,'p_continuacao_equivalentto','analisador_sintatico.py',186),
  ('continuacao_equivalentto -> CLASSE AND ABRE_PARENT casos_parentese declaracao_classe_aninhada FECHA_PARENT','continuacao_equivalentto',6,'p_continuacao_equivalentto','analisador_sintatico.py',187),
  ('continuacao_equivalentto -> CLASSE AND ABRE_PARENT casos_parentese declaracao_classe_aninhada FECHA_PARENT caso_ands','continuacao_equivalentto',7,'p_continuacao_equivalentto','analisador_sintatico.py',188),
  ('continuacao_equivalentto -> CLASSE AND ABRE_PARENT PROPRIEDADE SOME_ONLY classes_or FECHA_PARENT caso_ands','continuacao_equivalentto',8,'p_continuacao_equivalentto','analisador_sintatico.py',189),
  ('continuacao_equivalentto -> CLASSE AND ABRE_PARENT PROPRIEDADE SOME_ONLY NAMESPACE TIPO CARACTERE_ESPECIAL OPERADORES CARDINALIDADE CARACTERE_ESPECIAL FECHA_PARENT','continuacao_equivalentto',12,'p_continuacao_equivalentto','analisador_sintatico.py',190),
  ('declaracao_classe_aninhada -> caso_ands','declaracao_classe_aninhada',1,'p_declaracao_classe_aninhada','analisador_sintatico.py',196),
  ('caso_ands -> AND casos_parentese caso_ands','caso_ands',3,'p_caso_ands','analisador_sintatico.py',203),
  ('caso_ands -> AND casos_sem_parentese caso_ands','caso_ands',3,'p_caso_ands','analisador_sintatico.py',204),
  ('caso_ands -> AND casos_parentese','caso_ands',2,'p_caso_ands','analisador_sintatico.py',205),
  ('caso_ands -> AND casos_sem_parentese','caso_ands',2,'p_caso_ands','analisador_sintatico.py',206),
  ('casos_parentese -> ABRE_PARENT PROPRIEDADE SOME_ONLY CLASSE FECHA_PARENT','casos_parentese',5,'p_casos_parentese','analisador_sintatico.py',211),
  ('casos_parentese -> ABRE_PARENT PROPRIEDADE SOME_ONLY ABRE_PARENT classes_or FECHA_PARENT FECHA_PARENT','casos_parentese',7,'p_casos_parentese','analisador_sintatico.py',212),
  ('casos_parentese -> ABRE_PARENT PROPRIEDADE COMPARADORES CARDINALIDADE CLASSE FECHA_PARENT','casos_parentese',6,'p_casos_parentese','analisador_sintatico.py',213),
  ('casos_parentese -> ABRE_PARENT casos_parentese OR casos_parentese FECHA_PARENT','casos_parentese',5,'p_casos_parentese','analisador_sintatico.py',214),
  ('casos_parentese -> ABRE_PARENT casos_parentese AND casos_parentese FECHA_PARENT','casos_parentese',5,'p_casos_parentese','analisador_sintatico.py',215),
  ('casos_parentese -> ABRE_PARENT casos_parentese FECHA_PARENT','casos_parentese',3,'p_casos_parentese','analisador_sintatico.py',216),
  ('casos_parentese -> ABRE_PARENT PROPRIEDADE VALUE CLASSE FECHA_PARENT','casos_parentese',5,'p_casos_parentese','analisador_sintatico.py',217),
  ('casos_sem_parentese -> PROPRIEDADE SOME_ONLY CLASSE','casos_sem_parentese',3,'p_casos_sem_parentese','analisador_sintatico.py',222),
  ('casos_sem_parentese -> PROPRIEDADE ONLY casos_parentese','casos_sem_parentese',3,'p_casos_sem_parentese','analisador_sintatico.py',223),
  ('casos_sem_parentese -> PROPRIEDADE PALAVRA_RESERVADA CLASSE','casos_sem_parentese',3,'p_casos_sem_parentese','analisador_sintatico.py',224),
  ('casos_sem_parentese -> PROPRIEDADE COMPARADORES CARDINALIDADE CLASSE','casos_sem_parentese',4,'p_casos_sem_parentese','analisador_sintatico.py',225),
  ('declaracao_classe_axioma_fechamento -> regras_classe_axioma_fechamento','declaracao_classe_axioma_fechamento',1,'p_declaracao_classe_axioma_fechamento','analisador_sintatico.py',232),
  ('regras_classe_axioma_fechamento -> PROPRIEDADE SOME_ONLY CLASSE','regras_classe_axioma_fechamento',3,'p_regras_classe_axioma_fechamento','analisador_sintatico.py',240),
  ('regras_classe_axioma_fechamento -> PROPRIEDADE rec_propriedade SOME_ONLY CLASSE','regras_classe_axioma_fechamento',4,'p_regras_classe_axioma_fechamento','analisador_sintatico.py',241),
  ('regras_classe_axioma_fechamento -> PROPRIEDADE rec_propriedade SOME_ONLY CLASSE CARACTERE_ESPECIAL regras_classe_axioma_fechamento','regras_classe_axioma_fechamento',6,'p_regras_classe_axioma_fechamento','analisador_sintatico.py',242),
  ('regras_classe_axioma_fechamento -> PROPRIEDADE SOME_ONLY CLASSE CARACTERE_ESPECIAL regras_classe_axioma_fechamento','regras_classe_axioma_fechamento',5,'p_regras_classe_axioma_fechamento','analisador_sintatico.py',243),
  ('regras_classe_axioma_fechamento -> ABRE_PARENT PROPRIEDADE SOME_ONLY CLASSE FECHA_PARENT','regras_classe_axioma_fechamento',5,'p_regras_classe_axioma_fechamento','analisador_sintatico.py',244),
  ('regras_classe_axioma_fechamento -> ABRE_PARENT PROPRIEDADE SOME_ONLY CLASSE FECHA_PARENT AND regras_classe_axioma_fechamento','regras_classe_axioma_fechamento',7,'p_regras_classe_axioma_fechamento','analisador_sintatico.py',245),
  ('regras_classe_axioma_fechamento -> ABRE_PARENT PROPRIEDADE SOME_ONLY CLASSE FECHA_PARENT CARACTERE_ESPECIAL regras_classe_axioma_fechamento','regras_classe_axioma_fechamento',7,'p_regras_classe_axioma_fechamento','analisador_sintatico.py',246),
  ('regras_classe_axioma_fechamento -> PROPRIEDADE rec_propriedade COMPARADORES CARDINALIDADE CLASSE','regras_classe_axioma_fechamento',5,'p_regras_classe_axioma_fechamento','analisador_sintatico.py',248),
  ('regras_classe_axioma_fechamento -> PROPRIEDADE rec_propriedade COMPARADORES CARDINALIDADE CLASSE CARACTERE_ESPECIAL regras_classe_axioma_fechamento','regras_classe_axioma_fechamento',7,'p_regras_classe_axioma_fechamento','analisador_sintatico.py',249),
  ('regras_classe_axioma_fechamento -> PROPRIEDADE COMPARADORES CARDINALIDADE CLASSE','regras_classe_axioma_fechamento',4,'p_regras_classe_axioma_fechamento','analisador_sintatico.py',250),
  ('regras_classe_axioma_fechamento -> PROPRIEDADE COMPARADORES CARDINALIDADE CLASSE CARACTERE_ESPECIAL regras_classe_axioma_fechamento','regras_classe_axioma_fechamento',6,'p_regras_classe_axioma_fechamento','analisador_sintatico.py',251),
  ('regras_classe_axioma_fechamento -> ABRE_PARENT PROPRIEDADE COMPARADORES CARDINALIDADE CLASSE FECHA_PARENT','regras_classe_axioma_fechamento',6,'p_regras_classe_axioma_fechamento','analisador_sintatico.py',253),
  ('regras_classe_axioma_fechamento -> ABRE_PARENT PROPRIEDADE COMPARADORES CARDINALIDADE CLASSE FECHA_PARENT CARACTERE_ESPECIAL regras_classe_axioma_fechamento','regras_classe_axioma_fechamento',8,'p_regras_classe_axioma_fechamento','analisador_sintatico.py',254),
  ('regras_classe_axioma_fechamento -> ABRE_PARENT PROPRIEDADE COMPARADORES CARDINALIDADE CLASSE FECHA_PARENT AND regras_classe_axioma_fechamento','regras_classe_axioma_fechamento',8,'p_regras_classe_axioma_fechamento','analisador_sintatico.py',255),
  ('regras_classe_axioma_fechamento -> ABRE_PARENT PROPRIEDADE COMPARADORES CARDINALIDADE CLASSE CARACTERE_ESPECIAL FECHA_PARENT regras_classe_axioma_fechamento','regras_classe_axioma_fechamento',8,'p_regras_classe_axioma_fechamento','analisador_sintatico.py',256),
  ('regras_classe_axioma_fechamento -> ABRE_PARENT PROPRIEDADE rec_propriedade COMPARADORES CARDINALIDADE CLASSE FECHA_PARENT','regras_classe_axioma_fechamento',7,'p_regras_classe_axioma_fechamento','analisador_sintatico.py',257),
  ('regras_classe_axioma_fechamento -> ABRE_PARENT PROPRIEDADE rec_propriedade COMPARADORES CARDINALIDADE CLASSE CARACTERE_ESPECIAL FECHA_PARENT regras_classe_axioma_fechamento','regras_classe_axioma_fechamento',9,'p_regras_classe_axioma_fechamento','analisador_sintatico.py',258),
  ('rec_propriedade -> PROPRIEDADE','rec_propriedade',1,'p_rec_propriedade','analisador_sintatico.py',264),
  ('rec_propriedade -> PROPRIEDADE PROPRIEDADE','rec_propriedade',2,'p_rec_propriedade','analisador_sintatico.py',265),
  ('SOME_ONLY -> SOME','SOME_ONLY',1,'p_SOME_ONLY','analisador_sintatico.py',270),
  ('SOME_ONLY -> ONLY','SOME_ONLY',1,'p_SOME_ONLY','analisador_sintatico.py',271),
  ('classes_or -> CLASSE OR classes_or','classes_or',3,'p_classes_or','analisador_sintatico.py',276),
  ('classes_or -> CLASSE','classes_or',1,'p_classes_or','analisador_sintatico.py',277),
  ('classes_or -> ABRE_PARENT classes_or FECHA_PARENT','classes_or',3,'p_classes_or','analisador_sintatico.py',278),
  ('declaracao_classe_enumerada -> ABRE_CHAVE classes_enumeradas FECHA_CHAVE','declaracao_classe_enumerada',3,'p_declaracao_classe_enumerada','analisador_sintatico.py',284),
  ('classes_enumeradas -> CLASSE CARACTERE_ESPECIAL classes_enumeradas','classes_enumeradas',3,'p_classes_enumeradas','analisador_sintatico.py',291),
  ('classes_enumeradas -> CLASSE','classes_enumeradas',1,'p_classes_enumeradas','analisador_sintatico.py',292),
  ('declaracao_classe_coberta -> classes_or','declaracao_classe_coberta',1,'p_declaracao_classe_coberta','analisador_sintatico.py',299),
]
