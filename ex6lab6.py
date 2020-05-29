#Auteur : Younes Anys
#Numero d'étudiant : 300145843

print("Auteur : Anys Younes")
print("Numero d'étudiant : 300145843")

#Exercice 6 lab 6

def coder(s):
    '''(str)->str
    Retourne une nouvelle chaine code
    '''
    s_coder = ''

    for i in range(0, len(s)-1,2):
        s_coder = s_coder + s[i+1] + s[i]
    if (len(s)%2==1):
        s_coder=s_coder + s[len(s)-1]
    return s_coder

s1 = input("SVP entrer une chaine de character:")
print(coder(s1))
