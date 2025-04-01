def table_de_multiplication() :
    nombre  = int(input("Entrer un nombre :"))
    
    for i in range(1 , 10) :
        print(f"{nombre} x {i} = {nombre * i}")
table_de_multiplication()