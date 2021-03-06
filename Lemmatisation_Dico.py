# -*- coding: utf-8 -*-

from nltk.tokenize import word_tokenize


def Lemmatisation(liste,dico):
    
    lemmatisation = []
    
    for nliste in range(len(liste)):
        
        texte_lemmatized = ""
        
        texte_tokenized = word_tokenize(liste[nliste], language ='french')
      
        
        for nmot in range( len(texte_tokenized) ):
            texte_lemmatized = texte_lemmatized + str(dico.get(texte_tokenized[nmot],texte_tokenized[nmot])) + " "
        
        lemmatisation.append(texte_lemmatized)
    
    return lemmatisation
        



