Note  = int(input("Entrer la note de l'etudiant :  "))



if Note > 0 and Note < 3 :
    print("Sans commentaire !!!")
elif Note > 3 and Note <= 6 :
    print("Tu n'as rien compris !!! ")
elif Note > 6 and Note < 10 :
    print("Il faut revoir ...")
elif Note > 10 and Note < 14:
    print("Peux mieux faire !! ")
elif Note > 14 and Note < 18 : 
    print("Bon travail ...")
elif Note > 18 and Note == 19 :
    print("Excellent !! ")
elif Note == 20 :
    print("C'est sans faute !! ")