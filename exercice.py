import sys 

Element = []

option = {
    "1" : "Ajouter element dans la liste",
    "2" : "Supprimer element dans la liste",
    "3" : "Afficher element de la liste",
    "4" : "Vider la lsite",
    "5" : "Pour Quitter "
}

def presentation() : 
    print("Choisissez entre ces options : ")
    for key , value in option.items(): 
        print(f"{key} : {value}")

while True : 
    presentation()
    choix  = input("Entrer votre choix ici : ")
    
    if choix == "1" :
        Nouvel_element = input("Entrer l'element à ajouter ici : ")
        Element.append(Nouvel_element)
        print(f"L'element {Nouvel_element} a bien été enregistrez !!")
    if choix == "2" : 
        if not Element : 
            print("La liste est vide")
        else : 
            Element_a_supprimer = input("Entrer ici l'element a supprimer : ")
            if Element_a_supprimer in Element :
             Element.remove(Element_a_supprimer)
             print(f"L'element {Element_a_supprimer} a bien été supprimer")
            else :
             print(f"L'element {Element_a_supprimer} n'a pas été trouver")
    if choix == "3" : 
        if not Element : 
            print("Désolé , la liste est vide ")
        else :
            Element.sort()
            print(f"L'element present dans la liste  : {Element}")
    if choix == "4" : 
        if not Element :
         print("Désolé , la liste est déjà vide ")
        else :
            confirmation = input("Voulez vous vraiment videz la liste? (Oui ou Non) :  ").strip().lower()
            if confirmation == "Oui" : 
                Element.clear()
                print("La lsite a bien été vider !!")
            else :
                print("Vidage annuler!!")
    if choix  == "5" : 
        sys.exit()
        print("Au revoir !!")
    else : 
        print("Vous devez choisir entre ces options pour continuer !!")