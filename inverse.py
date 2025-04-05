#recursive
def reverse(world) : 
    if len(world) in [0,1] : 
        return world
    else : 
        return world[-1] + world[:-1]
print(reverse("abcdef"))



"""mot  = input("Entrer un mot  : ")
mot_inverse = mot[::-1]

print(f"L'inverse : {mot_inverse}")"""

