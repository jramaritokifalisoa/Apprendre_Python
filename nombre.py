counter = 0
Liste_nombre = []

# Boucle pour entrer 6 nombres
while counter < 6:
    nbr = int(input(f"Entrez le nombre {counter + 1} : "))
    Liste_nombre.append(nbr)  # Ajouter le nombre à la liste
    counter += 1

print(f"Vous avez entré la liste : {Liste_nombre}")

# Supprimer un nombre spécifié par l'utilisateur
nombre_a_supprimer = int(input("Entrez le nombre à supprimer : "))

if nombre_a_supprimer in Liste_nombre:
    Liste_nombre.remove(nombre_a_supprimer)
    print(f"Le nombre {nombre_a_supprimer} a été supprimé.")
else:
    print(f"Le nombre {nombre_a_supprimer} n'est pas dans la liste.")

# Trier et afficher la liste
Liste_nombre.sort()
print(f"Liste finale triée : {Liste_nombre}")



"""Liste = [1,2,5,7,8,9,7]

print(f"Les nombres presents sont : {Liste} ")
nombre_entrer  = int(input("Entrer un nombre  : "))

Liste.append(nombre_entrer)
Liste.sort()
print(f"Lsite = {Liste}")

nombre_a_supprimer = int(input("Entrer nombre à supprimer : "))
Liste.remove(nombre_a_supprimer)

print(f"Liste = {Liste}")"""