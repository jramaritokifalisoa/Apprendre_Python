Operateur  = input("Choisissez entre ces operateurs : ( + , - , * , / , %) : ")
Nombre1 = int(input("Entrer le premier nombre :"))
Nombre2 = int(input("Entrer le second nombre :"))
def multiplication( x , y) :
     return x * y 
def addition( x , y) :
    return x + y 
def division( x , y) :
    return x / y
def modulo( x , y) :
    return x % y
def moin( x , y) :
    return x - y   
if Operateur == "+" : 
        print(addition(Nombre1,Nombre2))
elif Operateur == "*" : 
        print(multiplication(Nombre1,Nombre2))
elif Operateur == "/" : 
        print(division(Nombre1,Nombre2))
elif Operateur == "%" : 
        print(modulo(Nombre1,Nombre2))
elif Operateur == "-" : 
        print(moin(Nombre1,Nombre2))
else : 
    print("Désolé, vous devez choisir entre ces operateurs")