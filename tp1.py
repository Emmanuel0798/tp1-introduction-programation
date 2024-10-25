import os
print("Run\n")

while True:     # Boucle de l'application
    os.system("cls")

    login = input("Veuillez entrer votre login :\n > ")
    motDePasse = input("Veuillez entrer votre mot de passe :\n > ")
    os.system("cls")

    # Variable pour déterminer si l'utilisateur veut quitter la boucle de l'application
    quitterLogin = False 

    if login != "démon" or motDePasse != "intérieur":
        while True:    
            # Boucle pour recommencer le login si l'utilisateur utilise une mauvaise commande
            os.system("cls")
            print("Erreur dans le login ou le mot de passe")
            choix = input("Veuillez (r)ecommencer ou (q)uitter :\n > ")
            if choix == "r" or choix == "R":
                os.system("cls")
                confirmationChoix = input("Voulez vous vraiment recommencer ? (oui/non) :\n > ")
                if confirmationChoix == "oui" or confirmationChoix == "Oui" or confirmationChoix == "OUI":
                    break
                elif confirmationChoix == "non" or confirmationChoix == "Non" or confirmationChoix == "NON":
                    os.system("cls")
                    input("Bien, donc veuillez recommencer votre choix.\nEnter...")
                    continue
            elif choix == "q" or choix == "Q":
                os.system("cls")
                confirmationChoix = input("Voulez vous vraiment quitter ? (oui/non) :\n > ")
                if confirmationChoix == "oui" or confirmationChoix == "Oui" or confirmationChoix == "OUI":
                    quitterLogin = True
                    break
                elif confirmationChoix == "non" or confirmationChoix == "Non" or confirmationChoix == "NON":
                    os.system("cls")
                    input("Bien, donc veuillez recommencer votre choix.\nEnter...")
                    continue
            else:
                os.system("cls")
                input("Vous avez taper une mauvaise commande, veuillez recommencer votre choix\nEnter... ")
                continue      
    else:
        # Si l'utilisateur a entrer les bonnes identifiants, l'application commence ici :
        os.system("cls")
        print("Démarage de l'application")
        input("Enter...")

        pointDeStupidite = 5
        pointDeFaiblesse = 5
        pointDeGaucherie = 5

        print("(C)ompétence\n(I)nventaire\n(Quitter)")
        choixJeu = input("Faite votre choix\n > ")
        if  choixJeu == "q" or choixJeu == "Q":
            break
        elif choixJeu == "i" or choixJeu == "I":

        elif  choixJeu == "c" or choixJeu == "C":
            os.system("cls")
            print("1 : Stupidité    5\n2 : Faiblesse    5\nGaucherie :  5")
            choixCompetence = input("Faite votre choix\n > ")
            if choixCompetence == 1:
                pointDeStupidité = input(f"Stupidité : {pointDeStupidite}\nEntrer la nouvelle valeur :\n > ")
            if choixCompetence == 2:
                pointDeFaiblesse = input(f"Faiblesse  : {pointDeFaiblesse}")
            if choixCompetence == 3:

            
        break

    # Condition pour savoir si l'utilisateur veut quitté la boucle pour le login
    if quitterLogin:
        break



os.system("cls")
print("Fin du programme")