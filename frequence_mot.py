# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 23:35:29 2018

@author: Mai
"""
import os
import nltk
import collections
from nltk.tokenize import word_tokenize
import re
import string
#from collections import 

def frequence_mot_dict(text): #cree la dictionnaire de mots et son fréquence
    text =text[0]
    text=text.replace("’",'  ') # replacer "’ " par l'espace
    text = re.sub("[0-9]+",' ',text)
    for char in string.punctuation: # Replacer ponctuation dans le texte par l'espace
        text=text.replace(char,'  ')
    text=text.lower() # transformer les  mots à la minuscule
    liste_mot = text.split()
    d={}
    for mot in sorted(liste_mot): # trier les mots par l'alphabet
        d[mot]=d.get(mot,0)+1
        
    return d
    
def frequence_Mot(text,mot):
    a=[]
    dict_liste= frequence_mot_dict(text)
    mot=mot.lower() # transformer le mot à la minuscule
    if mot not in dict_liste: # mot exit dans la dictionnaire?
        print("le mot n'exist pas dans le text")
    else:
        for cle,valeur in dict_liste.items():
            if cle == mot:
                a.append(("la fréquence de mot "+ "'" +cle + "'" +":" + str(valeur)+ " fois"))
        return (a)

            


