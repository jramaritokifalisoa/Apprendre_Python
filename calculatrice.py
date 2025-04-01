def calculatrice() : 
    operateur = input("Choisissez un operateur ( + , - , * , / , %)")
    nombre1 = float(input("Entrer nombre1 : "))
    nombre2 = float(input("Entrer nombre2 : "))
    
    if operateur == '+' : 
        print(f"Resultat : {nombre1 + nombre2}")
    elif operateur == '-' : 
        print(f"Resultat : {nombre1 - nombre2}")
    elif operateur == '*' :
        print(f"Resultat : {nombre1 * nombre2}")
    elif operateur == '%' : 
        print(f"Resultat:  {nombre1 % nombre2}")
    elif operateur == '/' :
        if nombre2 != 0 :
         print(f"Resultat : {nombre1 / nombre2} ")
        else:
         print(f"tsy possible ....")
calculatrice()