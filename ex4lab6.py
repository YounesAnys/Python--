#Auteur : Younes Anys
#Numero d'étudiant : 300145843

print("Auteur : Anys Younes")
print("Numero d'étudiant : 300145843")

#Exercice 4 lab 6

def compte1(s,c):
    return s.count(c)

def compte2(s,c):
    compteur = 0
    index = 0
    while (index < len(s)):
        if (c==s[index]):
            compteur += 1 #compteur = compteur + 1
            index = index + 1
    return compteur

s = input("SVP donnez une chaine de caractères :")
print(compte1(s,'s'))
print(compte1(s, 'de la'))

print(compte2(s,'s'))
print(compte2(s, 'de la'))
