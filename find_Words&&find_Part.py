def find_Words(text, mot):#prend une liste de string et un mot
    taille = len(text)  #on calcule la taille du texte
    mot= ' ' + mot + ' '#on rajoute des espaces avant et apres le mot
    taille3=len(mot)    #on calcule la taille du mot
    dico=dict()     #on initialise un dico pour faire toutes les parties
    for k in range(0,taille):   #on parcourt toutes les parties
        compte=text[k].count(mot)   #on calcule le nombre de fois que le mot apparait dans la partie
        liste=list()    #On initialise une liste ou il y aura les indices pour une partie
        i=1     #permet de se deplacer dans la liste
        j=1
        if compte>0:    #si il y a au moins une occurence
            taille2=len(text[k])    #on calcule la taille de la partie qu'on analyse
            liste.append(text[k].find(mot)+1)   #on rajoute l'indice de la premiere lettre de la premiere
                                                #occurence du mot
            liste.append(liste[0]+taille3-3)    #On rajoute l'indice de la derniere lettre de la premiere
                                                #occurence du mot
            while (i< compte) :     #on continue tant qu'il existe encore des occurences du mot
                liste.append(text[k].find(mot,liste[j]+2,taille2)+1) 
                    #on ajoute l'indice de la premiere lettre de l'occurence suivante du mot
                j=j+1   #on incremente j 
                liste.append(liste[j]+taille3-3)
                    #on ajoute l'indice de la derniere lettre du mot
                i=i+1
                j=j+1
        dico[k]=liste #on ajoute la liste avec tous les indices pour la partie dans le dico
    return dico #retourne une clef du dico qui est le numero de la partie (paragraphe, page, proportion,...)
                # associe a une liste d'indice 


def find_Part(text,mot): #prend une liste de String et un mot
    dico=find_Words(text,mot)   #on effectue la fonction precedente
    taille = len(dico)  #taille du dictionnaire(donc nombre de partie)
    retour=list() #on initialise une liste qui portera le numero de chaque partie contenant le mot
    for i in range(0,taille):
        if(dico[i]!=[]):    #si la partie du dico ne contient rien
            retour.append(i)#on l'ajoute car elle ne contient pas le mot
    return retour

