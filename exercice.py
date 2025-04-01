import sys
Element = []

option = {
    "1" : "Pour ajouter un element",
    "2" : "Pour supprimer l'element",
    "3" : "Pour afficher la liste",
    "4" : "vider la liste",
    "5" : "Pour quitter"
}

def presentation() : 
    print("Veuillez choisir un option ! ")
    for key , value in option.items() :
        print(f"{key} : {value}")
while True : 
    presentation() 
    choix = input("Entrer votre choix : ")
    
    if choix  == "1" : 
        nouvel_element = input("Entrer element à ajouter")
        Element.append(nouvel_element)
        print(f"L'element {nouvel_element} a bien été ajouter")
    if choix == "2" : 
        if not Element : 
            print("Désolé , aucun element dans la liste")
        else : 
            Element_a_supprimer = input("Entrer l'element a supprimer")
        if Element_a_supprimer in Element : 
            Element.remove(Element_a_supprimer)
            print(f"L'element {Element_a_supprimer} a bien été supprimer")
        else : 
            print("Aucun element trouver !! ")
    if choix == "3" : 
        if not Element : 
            print("Aucun element dans la liste")
        else : 
            print(f"L'element  : {Element}")
    if choix == "4" : 
        if not Element : 
            print("Aucun element dans la liste")
        else : 
            Element.clear()
            print("Tout les elements a bien été vider")
    if choix  == "5" : 
        sys.exit()
        print("Au revoir !! ")
    else : 
        print("Vous devez choisir entre ces option")
        