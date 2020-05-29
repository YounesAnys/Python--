#Auteur : Younes Anys
#Numero d'étudiant : 300145843

print("Auteur : Anys Younes")
print("Numero d'étudiant : 300145843")

#Exercice 5 lab 6

def espace(s):
    '''(str)->str
    Retourne une nouvelle chaine des espaces
    '''
    index = 0
    nS = ""

    while(index < len(s)):
        nS = nS + s[index] + ' '
        index += 1
        nS = nS.strip()
        return nS
     
        
        
s = input("SVP donnez une chaine de caratères")

print(espace(s))
