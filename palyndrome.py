def est_palindrome():
    texte = input("Entrer un mot ou une lettre : ")
    
    if texte == texte[::-1]:
        print("ceci est un palindrome !! ")
    else :
        print("ceci n'est pas un palindrome...")
        
    

est_palindrome()