import sys
Element = []

option = {
    "1" : "Ajouter un element dans la liste",
    "2" : "Supprimer element dans la liste",
    "3" : "Afficher les elements dans la liste",
    "4" : "Vider la liste",
    "5" : "Pour Quitter"
}

def presentation() :
    print("Choisissez entre ces options !")
    for key , value  in option.items() :
        print(f"{key} : {value}")
        
while True :
    presentation()
    choix  = input("Entrer votre choix ici : ")
    
    if choix == "1" : 
        Nouvel_element = input("Entrer l'element à ajouter ici : ")
        Element.append(Nouvel_element)
        print(f"L'element {Nouvel_element} a bien été ajouter avec succès")
    if choix == "2" :
        if not Element :
            print("Désolé, la liste est vide")
        else :
            Element_a_supprimer = input("Entrer l'element a supprimer ici : ")
            if Element_a_supprimer in Element :
                Element.remove(Element_a_supprimer)
                print(f"L'element {Element_a_supprimer} a bien été supprimer avec succès")
            else :
                print(f"L'element {Element_a_supprimer} n'a pas été trouver !")
    if choix  ==  "3" :
         if not Element :
            print("La liste est vide ")
         else : 
            print(f"L'element : {Element}")
            Element.sort()
            
    if choix == "4" : 
        if not Element :
            print("La liste est déjà vide")
        else : 
            confirmaton = input("Voulez vous vraiment vider la liste (Oui ou Non) :").strip().lower()
            if confirmaton == "Oui" :
                Element.clear()
                print("La liste a bien été vider avec succès !!")
            else :
                print("Vidage annuler")
    if choix == "5" :
        print("Au revoir !! ")
        sys.exit()
    else :
        print("Vous devez choisir entre ces otpions !!")
        