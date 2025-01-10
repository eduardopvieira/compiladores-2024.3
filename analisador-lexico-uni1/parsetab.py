
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'CARACTERE_ESPECIAL CARDINALIDADE CLASSE NAMESPACE NOME_INDIVIDUO PALAVRA_RESERVADA PROPRIEDADE TIPOprograma : declaracao_classedeclaracao_classe : PALAVRA_RESERVADA CLASSE obrigatorio_subclassof caso_disjointclasses caso_individualsobrigatorio_subclassof : PALAVRA_RESERVADA PROPRIEDADE PALAVRA_RESERVADA CLASSE\n                       | PALAVRA_RESERVADA PROPRIEDADE PALAVRA_RESERVADA NAMESPACE TIPO\n                       | PALAVRA_RESERVADA PROPRIEDADE PALAVRA_RESERVADA NAMESPACE TIPO CARACTERE_ESPECIAL outra_propriedade\n                       | PALAVRA_RESERVADA PROPRIEDADE PALAVRA_RESERVADA CLASSE CARACTERE_ESPECIAL outra_propriedadeoutra_propriedade : PROPRIEDADE PALAVRA_RESERVADA CLASSE CARACTERE_ESPECIAL outra_propriedade\n                         | PROPRIEDADE PALAVRA_RESERVADA NAMESPACE TIPO CARACTERE_ESPECIAL outra_propriedade\n                         | PROPRIEDADE PALAVRA_RESERVADA CLASSE\n                         | PROPRIEDADE PALAVRA_RESERVADA NAMESPACE TIPOcaso_disjointclasses : PALAVRA_RESERVADA CLASSE\n                            | PALAVRA_RESERVADA CLASSE CARACTERE_ESPECIAL outra_classe\n                            |outra_classe : CLASSE\n                    | CLASSE CARACTERE_ESPECIAL outra_classecaso_individuals : PALAVRA_RESERVADA NOME_INDIVIDUO\n                        | PALAVRA_RESERVADA NOME_INDIVIDUO CARACTERE_ESPECIAL outro_individuo\n                        |outro_individuo : NOME_INDIVIDUO\n                       | NOME_INDIVIDUO CARACTERE_ESPECIAL outro_individuo'
    
_lr_action_items = {'PALAVRA_RESERVADA':([0,4,6,7,9,11,14,19,20,21,23,24,30,31,33,37,38,40,],[3,5,8,10,12,-11,-3,-4,-14,-12,29,-6,-5,-15,-9,-10,-7,-8,]),'$end':([1,2,6,9,11,13,14,17,19,20,21,24,27,28,30,31,33,35,37,38,40,],[0,-1,-13,-18,-11,-2,-3,-16,-4,-14,-12,-6,-19,-17,-5,-15,-9,-20,-10,-7,-8,]),'CLASSE':([3,8,10,16,26,29,],[4,11,14,20,20,33,]),'PROPRIEDADE':([5,18,25,36,39,],[7,23,23,23,23,]),'NAMESPACE':([10,29,],[15,34,]),'CARACTERE_ESPECIAL':([11,14,17,19,20,27,33,37,],[16,18,22,25,26,32,36,39,]),'NOME_INDIVIDUO':([12,22,32,],[17,27,27,]),'TIPO':([15,34,],[19,37,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'declaracao_classe':([0,],[2,]),'obrigatorio_subclassof':([4,],[6,]),'caso_disjointclasses':([6,],[9,]),'caso_individuals':([9,],[13,]),'outra_classe':([16,26,],[21,31,]),'outra_propriedade':([18,25,36,39,],[24,30,38,40,]),'outro_individuo':([22,32,],[28,35,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> declaracao_classe','programa',1,'p_programa','analisadorLexico.py',39),
  ('declaracao_classe -> PALAVRA_RESERVADA CLASSE obrigatorio_subclassof caso_disjointclasses caso_individuals','declaracao_classe',5,'p_classe_primitiva','analisadorLexico.py',44),
  ('obrigatorio_subclassof -> PALAVRA_RESERVADA PROPRIEDADE PALAVRA_RESERVADA CLASSE','obrigatorio_subclassof',4,'p_obrigatorio_subclassof','analisadorLexico.py',54),
  ('obrigatorio_subclassof -> PALAVRA_RESERVADA PROPRIEDADE PALAVRA_RESERVADA NAMESPACE TIPO','obrigatorio_subclassof',5,'p_obrigatorio_subclassof','analisadorLexico.py',55),
  ('obrigatorio_subclassof -> PALAVRA_RESERVADA PROPRIEDADE PALAVRA_RESERVADA NAMESPACE TIPO CARACTERE_ESPECIAL outra_propriedade','obrigatorio_subclassof',7,'p_obrigatorio_subclassof','analisadorLexico.py',56),
  ('obrigatorio_subclassof -> PALAVRA_RESERVADA PROPRIEDADE PALAVRA_RESERVADA CLASSE CARACTERE_ESPECIAL outra_propriedade','obrigatorio_subclassof',6,'p_obrigatorio_subclassof','analisadorLexico.py',57),
  ('outra_propriedade -> PROPRIEDADE PALAVRA_RESERVADA CLASSE CARACTERE_ESPECIAL outra_propriedade','outra_propriedade',5,'p_outra_propriedade','analisadorLexico.py',67),
  ('outra_propriedade -> PROPRIEDADE PALAVRA_RESERVADA NAMESPACE TIPO CARACTERE_ESPECIAL outra_propriedade','outra_propriedade',6,'p_outra_propriedade','analisadorLexico.py',68),
  ('outra_propriedade -> PROPRIEDADE PALAVRA_RESERVADA CLASSE','outra_propriedade',3,'p_outra_propriedade','analisadorLexico.py',69),
  ('outra_propriedade -> PROPRIEDADE PALAVRA_RESERVADA NAMESPACE TIPO','outra_propriedade',4,'p_outra_propriedade','analisadorLexico.py',70),
  ('caso_disjointclasses -> PALAVRA_RESERVADA CLASSE','caso_disjointclasses',2,'p_caso_disjointclasses','analisadorLexico.py',79),
  ('caso_disjointclasses -> PALAVRA_RESERVADA CLASSE CARACTERE_ESPECIAL outra_classe','caso_disjointclasses',4,'p_caso_disjointclasses','analisadorLexico.py',80),
  ('caso_disjointclasses -> <empty>','caso_disjointclasses',0,'p_caso_disjointclasses','analisadorLexico.py',81),
  ('outra_classe -> CLASSE','outra_classe',1,'p_outra_classe','analisadorLexico.py',88),
  ('outra_classe -> CLASSE CARACTERE_ESPECIAL outra_classe','outra_classe',3,'p_outra_classe','analisadorLexico.py',89),
  ('caso_individuals -> PALAVRA_RESERVADA NOME_INDIVIDUO','caso_individuals',2,'p_caso_individuals','analisadorLexico.py',96),
  ('caso_individuals -> PALAVRA_RESERVADA NOME_INDIVIDUO CARACTERE_ESPECIAL outro_individuo','caso_individuals',4,'p_caso_individuals','analisadorLexico.py',97),
  ('caso_individuals -> <empty>','caso_individuals',0,'p_caso_individuals','analisadorLexico.py',98),
  ('outro_individuo -> NOME_INDIVIDUO','outro_individuo',1,'p_outro_individuo','analisadorLexico.py',105),
  ('outro_individuo -> NOME_INDIVIDUO CARACTERE_ESPECIAL outro_individuo','outro_individuo',3,'p_outro_individuo','analisadorLexico.py',106),
]
