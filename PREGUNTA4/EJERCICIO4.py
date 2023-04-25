# -*- coding: utf-8 -*-
"""

@author: alex
"""

from kanren import run, var, eq, Relation, facts
a = var()
b = var()

padre = Relation()
primo = Relation()
tio = Relation()
facts(padre, ("Maximo R","Alex R"),("Maximo R","Paul H"),("Maximo R","Maya H"),
      ("Otilia P","Enrique H"),("Otilia P","Paul H"),("Otilia P","Maya H"))
facts(primo, ("Paul H","Reyna Pr"),("Paul H","Daniela Pr"),("Paul H","Alison Pr"),
      ("Paul H","Dylan Pr"),("Paul H","Ricaldi Pr"))
facts(tio, ("Paul H","Victor T"),("Paul H","Jesusa T"),("Paul H","Cecilio T"),
      ("Paul H","Rebeca T"),("Paul H","Delia T"),("Paul H","Grover T"))
print(padre.facts)
print(run(1,a,padre(a,"Paul R")))
print(run(1,a,padre(a,"Enrique H")))
print(run(2,b,padre("Otilia P",b)))
print(run(3,b,padre("Maximo R",b)))
#print(run(3,b,padre("Maya H",b)))

print(run(3,a,primo(a,"Ricaldi Pr")))
print(run(3,a,primo(a,"Andrea M")))
print(run(3,a,primo(a,"Josue M")))
print(run(3,a,primo("Alex R",a)))

print(run(3,a,tio(a,"Victor T")))
print(run(3,a,tio(a,"Amelia T")))