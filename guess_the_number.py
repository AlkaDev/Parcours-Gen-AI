import random
nombre_secret = random.randint(1, 200)
print("Moi j'ai choisi le nombre entre 1 et 200. À toi de deviner !")
gagne = False
print("Bienvenue dans mon jeu de devinette !")
tentatives = 0
# la boucle while va nous aider à signaler à l'utilisateur que tant que :
while not gagne:
    saisir = input("Propose un chiffre ou nombre : ")
    # et converti le texte en un nombre entier
    essaye = int(saisir)
    tentatives = tentatives + 1
    
    if essaye < nombre_secret:
        print("Trop petit")
    elif essaye > nombre_secret:
        print("Trop grand")
    else:
        print("Félicitation ! tu as trouvé le nombre secret")
        print("Nombre d'essais :", tentatives)
        gagne = True

#fin de la partie
