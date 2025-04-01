def liste_de_courses():
    liste = []

    while True:
        action = input("Choisissez une action (ajouter, supprimer, afficher, quitter): ").lower()

        if action == 'ajouter':
            item = input("Entrez l'élément à ajouter: ")
            liste.append(item)
        elif action == 'supprimer':
            item = input("Entrez l'élément à supprimer: ")
            if item in liste:
                liste.remove(item)
            else:
                print("Élément non trouvé")
        elif action == 'afficher':
            print("Liste de courses:", liste)
        elif action == 'quitter':
            break
        else:
            print("Action non valide")

liste_de_courses()