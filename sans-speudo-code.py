import os
os.system("cls")
print("Run")


# Les variables utilié lors du programme : 
choix = ""
choixPersonne = 0
choixSupprimerPersonnage = ""
personneEnregistre = []    # Cette variable permet de stocker le nom et la classe des personnes enregistré dans la compagnie
nbrPersonneFullCaster = 0   # Cette variable permet de compter le nombre de personnage "full caster"
nomPersonne = ""
choixClassNum = 0   # Nuéreau de la classe choisie par le joueur
choixClassNom = ""  # Nom de la classe chosie par le joueur
nbrPersonneCompagnie = 0

# Variable utilisé pour manipuler la list personneEnregistre
indicePersonneEnregistre = 0     # Indice de la personne qu'on veut enregistrer
listPersonneEnregistre = []    #La list enfant dans la liste parent indicePersonneEnregistre


# Fonction utilisé dans le programme  :
def afficherPersonneEnregistre() :  
    print("** Les membres de la compagnie sont les suivants ! **\n")
    indicePersonneEnregistre = 0
    for listPersonneEnregistre in personneEnregistre : 
        indicePersonneEnregistre = indicePersonneEnregistre + 1 
        print(f"{indicePersonneEnregistre} : {listPersonneEnregistre[0]} : {listPersonneEnregistre[1]}")
    print()


def afficherClass() :
    # Dans cette boucle, on intervient pas une variable du style "error" qui permet à la boucle de recommencer lors d'une erreur de l'utilisateur, on prend seulement
    # le fonction "continue" pour faire recommencer la boucle lors d'une erreurs
    while True :
        print("***** Classe disponible *****")
        print("1 : Barbare\n2 : Barbe\n3 : Clerc\n4 : Druide\n5 : Ensorceleur\n6 : Guerrier\n7 : Magicien\n8 : Moine\n9 : Occultiste\n10 : Paladin\n11 : Rôdeur\n12 : Roublard\n")
        print("Entrer la classe choisie : ")
        # Numéreau du choix de la classe
        choixClassNum = int(input(" > "))
        os.system("cls")

        # Confirmation du choix de "choixClassNum" : 
        if choixClassNum < 1 or choixClassNum > 12 : 
            print("Erreur, vous avez sélectionner une valeur qui n'existe pas dans la classe, donc non comprise entre 1 et 12, veuillez recommencer.")
            input("enter...\n > ")
            continue 
        elif choixClassNum == 5 or choixClassNum == 7 or choixClassNum == 9 :
            nbrPersonneFullCaster = nbrPersonneFullCaster + 1
            if nbrPersonneFullCaster > 1 :
                nbrPersonneFullCaster = nbrPersonneFullCaster - 1
                print("L'équipe contient déja un personnage \"full caster\", veuillez recommencer")
                input("enter...\n > ")
                os.system("cls")
                continue

        # Permet de retrouver et de stocker le nom de la classe choisie
        if choixClassNum == 1:
            choixClassNom = "Barbare"
        elif choixClassNum == 2:
            choixClassNom = "Barde"
        elif choixClassNum == 3:
            choixClassNom = "Clerc"
        elif choixClassNum == 4:
            choixClassNom = "Druide"
        elif choixClassNum == 5:
            choixClassNom = "Ensorceleur"
        elif choixClassNum == 6:
            choixClassNom = "Guerrier"
        elif choixClassNum == 7:
            choixClassNom = "Magicien"
        elif choixClassNum == 8:
            choixClassNom = "Moine"
        elif choixClassNum == 9:
            choixClassNom = "Occultiste"
        elif choixClassNum == 10:
            choixClassNom = "Paladin"
        elif choixClassNum == 11:
            choixClassNom = "Rôdeur"
        else :
            choixClassNom = "Roublard"
        break
    return choixClassNom



# Début du programme : 
print("******************************************************************************************")
print("Bienvenue dans l'éditeur de la compagnie du Cégep\nUn démogorgone a été aperçu dans les murs du cégep\nVous devez former l'équipe qui aura pour mission de le trucider")
print("******************************************************************************************\n")
input("Appuyez sur une touche pour commencer (enter)...\n > ")
os.system("cls")

while True :
    # Le menu principal 
    if len(personneEnregistre) != 0 :   # S'il y a au moin une personne enregistré dans la compagnie
        os.system("cls")
        choix = ""

        afficherPersonneEnregistre()

        print("[A] : Ajoute un membre\n[B] : Modifier un membre\n[C] : Supprimer un membre")
        print("\nOption choisie : ")
        choix = input(" > ")  
#    elif len(personneEnregistre) == 5 :     # Si le nombre de personnes dans la compagnie à atteind 5
        

    else : 
        os.system("cls")
        print("Personne n'est inscrit dans la compagnie pour l'instant !\n\n[A] : Ajouter un membre...\n\nOptions choisie : ")
        choix = input(" > ")
        
    if choix == "a" or choix == "A" : 
        os.system("cls")

        print("Entrer le nom du personnage : ")
        nomPersonne = input(" > ")
        os.system("cls")  

        choixClassNom = afficherClass()
        
        # Si la confirmation n'a pas soulever d'errreur de la part de l'utilisateur, on continue avec le code suivant 
        # Je créer une list qui fonctionne de la manière suivant  :
        # nomListe [
        #   [value (nom), value (nom classe)]
        #   ...
        # ]
        personneEnregistre.append([nomPersonne, choixClassNom])
        choix = ""
    elif choix == "b" or choix == "B" : 
        while True : 
            os.system("cls")
            afficherPersonneEnregistre()
            print("Membre à modifier : ")
            choixPersonne = int(input(" > "))

            # Vérifie si l'utilisateur à bien rentré un bon nombre dans "choixPersonne"
            if choixPersonne < 1 or choixPersonne > len(personneEnregistre) : 
                os.system("cls")
                print("Vous choisi un personnage qui n'existe pas, veuillez recommencer : (enter)")
                input(" > ")
                continue
                
            os.system("cls")
            print("[A] : Modifier le nom\n[B] : Modifier la classe\n")
            print("Option choisie  :")
            choix = input(" > ")

            if choix == "a" : 
                os.system("cls")
                print("Entrer le nom du personnage  :")
                nomPersonne = input(" > ")
                personneEnregistre[choixPersonne - 1][0] = nomPersonne
                break
            elif choix == "b" : 
                os.system("cls")
                choixClassNom = afficherClass()
                personneEnregistre[choixPersonne - 1][1] = choixClassNom
                break
        choix = ""
    elif choix == "c" or choix == "C" :
        while True : 
            os.system("cls")
            afficherPersonneEnregistre() 
            print("Membre à supprimer : ")
            choixPersonne = int(input(" > "))

            # Vérifie si l'utilisateur à bien rentré un bon nombre dans "choixPersonne"
            if choixPersonne < 1 or choixPersonne > len(personneEnregistre) : 
                os.system("cls")
                print("Vous avez choisi un personnage qui n'existe pas, veuillez recommencer : (Entrer)")
                input(" > ")
                continue

            print("Vous êtes certain de supprimer le personnage ? : (Y / N)")
            choixSupprimerPersonnage = input(" > ")
            if choixSupprimerPersonnage == "Y" or choixSupprimerPersonnage == "y" :
                del personneEnregistre[choixPersonne - 1]
                break
            elif choixSupprimerPersonnage == "n" or choixSupprimerPersonnage == "N" :
                break
        choix = ""