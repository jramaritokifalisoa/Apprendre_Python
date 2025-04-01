import random 

def deviner_le_nombre(): 
    
    nombre_a_deviner = random.randint(1, 100)
    tentative = 0 
     
    while True : 
        tentative += 1
        nombre = int(input("Entrer un nombre (entre 1 à 100) : "))
        
        if nombre > nombre_a_deviner :
            print("Trop haut")
        elif nombre < nombre_a_deviner :
            print("Trop bas")
        else : 
            print(f"Felicitation !! vous avez trouver le nombre en {tentative} tentative")
            break
    
deviner_le_nombre()