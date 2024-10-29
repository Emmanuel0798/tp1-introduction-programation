import os
os.system("cls")
print("Run")

print("******************************************************************************************")
print("Bienvenue dans l'éditeur de la compagnie du Cégep\nUn démogorgone a été aperçu dans les murs du cégep\nVous devez former l'équipe qui aura pour mission de le trucider")
print("******************************************************************************************\n")
input("Appuyez sur une touche pour commencer (enter)...\n > ")
os.system("cls")

print("Personne n'est inscrit dans la compagnie pour l'instant !\n\n[A] : Ajouter un membre...\n\nOptions choisie : ")
choix = input(" > ")
# Cette variable permet de stocker le nom et la classe des personnes enregistré dans la compagnie
personneEnregistreCompagnie = {}
# Cette variable permet de compter le nombre de personnage "full caster"
nbrPersonneFullCaster = 0

# NOTE : Éventuellement une boucle "while"
if choix == "a" : 
    os.system("cls")

    print("Entrer le nom du personnage : ")
    nomPersonne = input(" > ")
    os.system("cls")

    while True :    # Dans cette boucle, on intervient pas une variable du style "error" qui permet à la boucle de recommencer lors d'une erreur de l'utilisateur, on prend seulment
                    # le fonction "continue" pour faire recommencer la boucle lors d'une erreur
        print("***** Classe disponible *****")
        print("1 : Barbare\n2 : Barbe\n3 : Clerc\n4 : Druide\n5 : Ensorceleur\n6 : Guerrier\n7 : Magicien\n8 : Moine\n9 : Occultiste\n10 : Paladin\n11 : Rôdeur\n12 : Roublard")
        print("Entrer la classe choisie : ")
        # Numéreau du choix de la classe
        choixClassNum = int(input(" > "))
        os.system("cls")

        # Confirmation du choix de "choixClassNum" : 
        if choixClassNum < 1 or choixClassNum > 12 : 
            print("Erreur, vous avez sélectionner une valeur qui n'existe pas dans la classe, donc non comprise entre 1 et 12, veuillez recommencer.")
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
        elif choixClassNum == 12:
            choixClassNom = "Roublard"
        
        # Si la confirmation n'a pas soulever d'errreur de la part de l'utilisateur, on continue avec le code suivant 
        if not len(personneEnregistreCompagnie) :   # Si la liste n'est pas nul, donc ne contient encore aucune personne enregistrer
            # Variable contenant le prochain numéreau à enregistrer
            nbrPersonneCompagnie = str((len(personneEnregistreCompagnie) / 2) + 1)
            personneEnregistreCompagnie["Nom du personnage " + nbrPersonneCompagnie] = nomPersonne
            personneEnregistreCompagnie["Classe du personnage" + nbrPersonneCompagnie] = choixClassNom
        else : # Si la liste est nul, simplement enregistrer une personne avec l'indice 1
            personneEnregistreCompagnie["Nom du personnage 1"] = nomPersonne 
            personneEnregistreCompagnie["Classe du personnage 2"] = choixClassNom


# NOTE : RENDU À DÉFINIR LA BOUCLE PRINCIPAL, DONC APRÈS L'AJOUR DU PREMIER MEMBRE
# Ne pas oublié de déclarer ses variables et ses constantes !!!!!!!!!!!!!