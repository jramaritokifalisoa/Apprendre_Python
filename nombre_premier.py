def est_premier():
    nombre = int(input("Entrez un nombre: "))
    if nombre > 1:
        for i in range(2, int(nombre ** 0.5) + 1):
            if nombre % i == 0:
                print(f"{nombre} n'est pas un nombre premier.")
                break
        else:
            print(f"{nombre} est un nombre premier.")
    else:
        print(f"{nombre} n'est pas un nombre premier.")

est_premier()