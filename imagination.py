import sys


option = {
    "1" : "Ajouter un individu dans la liste",
    "2" : "Supprimer une personne dans la liste",
    "3" : "Afficher les elements dans la liste",
    "4" : "Vider la liste",
    "5" : "Pour Quitter"
}
personne = {
    "E-mail" : [],
    "Mot_de_passe" : [],
    "Confirmation" : []
}
def presentation() :
    print("Choisissez entre ces options !")
    for key , value  in option.items() :
        print(f"{key} : {value}")

while True : 
    presentation()
    choix = input("Entrer votre choix ici : ")
    
    if choix == "1" : 
      Email = input("Entrer votre adresse mail ici : ")
      Mot_de_passe = input("Entrer votre mot de passe ici : ")
      Confirmation= input("Confirmer votre mot de passe ici : ")
      personne['E-mail'].append(Email)
      personne['Mot_de_passe'].append(Mot_de_passe)
      personne['Confirmation'].append(Confirmation)
      if Mot_de_passe != Confirmation : 
          print("Désolé , votre mot de n'est pas identique ! , Vous devez recommencer ")
          personne["E-mail"].remove(Email)
          if len(Mot_de_passe) and len(Confirmation) < 4 :
              print("Désolé ,  le mot de passe doit être superieur à 4 , Vous devez recommencer")
              personne["E-mail"].remove(Email)
      else :     
       print(f"felicitaion, {personne['E-mail']} a bien été ajouter ")
    
    if choix == "2" :
      Personne_a_supprimer = input("Entrer seulement l'email de la personne à supprimer : ")
      
      Mot_de_pass = input("Entrer le mot de passe ici : ")
      if not personne["Mot_de_passe"] : 
          print("Erreur !! ")
      else :
       if Mot_de_pass in personne["Mot_de_passe"] and personne["Confirmation"]:
             personne["Mot_de_passe"].remove(Mot_de_pass)
             personne["Confirmation"].remove(Mot_de_pass)
             print("OK")
             if not personne["E-mail"] : 
               print("Erreur")
             else :
              if Personne_a_supprimer in personne["E-mail"] :
                personne['E-mail'].remove(Personne_a_supprimer)
                print (f"L'email {Personne_a_supprimer} n'est plus dans la liste")
              else : 
               print("Désoler ,  l'email n'existe pas !! ")
       else :
            print("Le mot de passe que vous avez entrer n'est pas identique !! ")
    if choix == "3" : 
        if not personne["E-mail"]: 
            print("Désoler ,  il y a personne dans la liste !!")
        else : 
            print (f"La liste ici presente  : {personne['E-mail']}")
    if choix == "4" :
        if not personne["E-mail"] : 
            print("Désoler ,  il y a personne dans la liste !!")
        else : 
            Confirmation_vidage = str(input("Voulez vous vraiment vider la liste ( Oui ou Non ):")).strip().lower()
            if Confirmation_vidage == 'Oui':             
               personne["E-mail"].clear()
               personne["Mot_de_passe"].clear()
               personne["Confirmation"].clear()
               print("felicitation ,  la liste est de nouveau vide !!")
            else :
                print("Vidage annuler !! ")
    if choix == "5" : 
           print("Au revoir !!!")
           sys.exit()
    else : 
        print("Il faut choisir entre ces options !! ")