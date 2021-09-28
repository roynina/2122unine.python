#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 19:51:32 2021

@author: ninaroy
"""

#programme moyenne.py
nb_entree=int(input('Entrez le nombre d\'entrée'))
list=[]
for i in range (nb_entree) :
    nombre=float(input('entrez les valeurs des entrées'))
    list.append(nombre)
somme=sum(list)
moyenne=somme/nb_entree
print('la moyenne des entrées est ', moyenne)