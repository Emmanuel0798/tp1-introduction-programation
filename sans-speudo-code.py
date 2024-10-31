import os
os.system("cls")
print("Run")


# Les variables utilisées lors du programme : 
choix = ""
choixPersonne = 0
choixSupprimerPersonnage = ""
personneEnregistre = []    # Cette variable permet de stocker le nom et la classe des personnes enregistrées dans la compagnie
nbrPersonneFullCaster = 0   # Cette variable permet de compter le nombre de personnage "full caster"
nomPersonne = ""
choixClassNum = 0   # Numéro de la classe choisie par le joueur
choixClassNom = ""  # Nom de la classe chosie par le joueur
nbrPersonneCompagnie = 0

# Variable utilisée pour manipuler la list personneEnregistre
indicePersonneEnregistre = 0     # Indice de la personne qu'on veut enregistrer
listPersonneEnregistre = []    #La list enfant dans la liste parent personneEnregistre avec l'indice de indicePersonneEnregistre


# Fonction utilisée dans le programme  :
def afficherPersonneEnregistre() :  
    print("** Les membres de la compagnie sont les suivants ! **\n")
    indicePersonneEnregistre = 0
    for listPersonneEnregistre in personneEnregistre : 
        indicePersonneEnregistre = indicePersonneEnregistre + 1 
        print(f"{indicePersonneEnregistre} : {listPersonneEnregistre[0]} : {listPersonneEnregistre[1]}")
    print()


def afficherClass(nbrPersonneFullCaster) :
    # Dans cette boucle, on intervient pas une variable du style "error" qui permet à la boucle de recommencer lors d'une erreur de l'utilisateur, on prend seulement
    # le fonction "continue" pour faire recommencer la boucle lors d'une erreur de la part de l'utilisateur
    while True :
        print("***** Classe disponible *****")
        print("1 : Barbare\n2 : Barbe\n3 : Clerc\n4 : Druide\n5 : Ensorceleur\n6 : Guerrier\n7 : Magicien\n8 : Moine\n9 : Occultiste\n10 : Paladin\n11 : Rôdeur\n12 : Roublard\n")
        print("Entrer la classe choisie : ")
        # Numéro du choix de la classe
        choixClassNum = int(input(" > "))
        os.system("cls")

        # Confirmation du choix de "choixClassNum" : 
        if choixClassNum < 1 or choixClassNum > 12 : 
            print("Erreur, vous avez sélectionné une valeur qui n'existe pas dans la classe, donc non comprise entre 1 et 12, veuillez recommencer.")
            input("Enter...\n > ")
            continue 
        elif choixClassNum == 5 or choixClassNum == 7 or choixClassNum == 9 :

            nbrPersonneFullCaster = nbrPersonneFullCaster + 1

            if nbrPersonneFullCaster > 1 :
                nbrPersonneFullCaster = nbrPersonneFullCaster - 1
                print("L'équipe contient déja un personnage \"full caster\", veuillez recommencer")
                input("Enter...\n > ")
                os.system("cls")
                continue

        # Permet de retrouver et de stocker le nom de la classe choisi
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
    return choixClassNom, nbrPersonneFullCaster



# Début du programme : 
print("******************************************************************************************")
print("Bienvenue dans l'éditeur de la compagnie du Cégep\nUn démogorgone a été aperçu dans les murs du cégep\nVous devez former l'équipe qui aura pour mission de le trucider")
print("******************************************************************************************\n")
input("Appuyez sur une touche pour commencer (Enter)...\n > ")
os.system("cls")

nbrPersonneFullCaster = 0   # Au début du programme, il n'y pas encore de personnage, donc il n'a pas de "fullCaster"

while True :
    # Le menu principal 
    if len(personneEnregistre) == 5 :     # Si le nombre de personnes dans la compagnie à atteind 5
        afficherPersonneEnregistre()
        print("[B] : Modifier un membre\n[C] : Supprimer un membre\n[D] : Afficher les membres")
        print("\nOption choisi  : ")
        choix = input(" > ")
    elif len(personneEnregistre) != 0 :   # S'il y a au moin une personne enregistré dans la compagnie
        os.system("cls")
        choix = ""

        afficherPersonneEnregistre()

        print("[A] : Ajoute un membre\n[B] : Modifier un membre\n[C] : Supprimer un membre")
        print("\nOption choisi : ")
        choix = input(" > ")  
    else :  # S'il n'a personne enregistré dans la compagnie
        os.system("cls")
        print("Personne n'est inscrit dans la compagnie pour l'instant !\n\n[A] : Ajouter un membre...\n\nOptions choisi : ")
        choix = input(" > ")
        
    if choix == "a" or choix == "A" : 
        os.system("cls")

        print("Entrer le nom du personnage : ")
        nomPersonne = input(" > ")
        os.system("cls")  

        choixClassNom, nbrPersonneFullCaster = afficherClass(nbrPersonneFullCaster)

        # Si la confirmation n'a pas soulevé d'errreur de la part de l'utilisateur, on continue avec le code suivant 
        # Je créer une liste qui fonctionne de la manière suivant  :
        # nomListe [
        #   [value (nom de personnage 1), value (nom classe de personnnage 1)]
        #   [value (nom de personnage 2), value (nom classe de personnage 2)]
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
                print("Vous avez choisi un personnage qui n'existe pas, veuillez recommencer : (Enter)")
                input(" > ")
                continue
                
            os.system("cls")
            print("[A] : Modifier le nom\n[B] : Modifier la classe\n")
            print("Option choisi  :")
            choix = input(" > ")

            if choix == "a" : 
                os.system("cls")
                print("Entrez le nom du personnage  :")
                nomPersonne = input(" > ")
                personneEnregistre[choixPersonne - 1][0] = nomPersonne
                break
            elif choix == "b" : 
                os.system("cls")

                # Vérifie si la personnage supprimé est un "Full Caster", si c'est le cas, alors ajuster la variable "nbrPersonnageFullCaster"
                if personneEnregistre[choixPersonne - 1][1] == "Ensorceleur" or  personneEnregistre[choixPersonne - 1][1] == "Magicien" or personneEnregistre[choixPersonne - 1][1] == "Occuliste" :
                    nbrPersonneFullCaster = nbrPersonneFullCaster - 1

                choixClassNom, nbrPersonneFullCaster = afficherClass(nbrPersonneFullCaster)
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

            # Vérifie si la personnage supprimer est un "Full Caster", si c'est le cas, alors ajuster la variable "nbrPersonnageFullCaster"
            if personneEnregistre[choixPersonne - 1][1] == "Ensorceleur" or  personneEnregistre[choixPersonne - 1][1] == "Magicien" or personneEnregistre[choixPersonne - 1][1] == "Occuliste" :
                nbrPersonneFullCaster = nbrPersonneFullCaster - 1

            if choixSupprimerPersonnage == "Y" or choixSupprimerPersonnage == "y" :
                del personneEnregistre[choixPersonne - 1]
                break
            elif choixSupprimerPersonnage == "n" or choixSupprimerPersonnage == "N" :
                break
        choix = ""
    elif choix == "d" or choix == "D" : 
        os.system("cls")
        afficherPersonneEnregistre()
        print("Bonne chance !\nVous en aurez besoin !\nLongue vie à la compagnie du cégep !!")
        exit()