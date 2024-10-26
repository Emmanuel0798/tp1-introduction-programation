import os
import time
print("Run\n")

# Constantes : 
BON_LOGIN = "demon"
BON_PASSWORD = "interieur"
RECOMMENCER = 'r'
QUITTER = 'q'
COMPETENCE = 'c'
INVENTAIRE = 'i'
CASQUES = 'c'
BOTTES = 'b'
GANTS	= 'g'
EDITER = 'e'
MENU_PRINCIPAL = 'm'
MAX_COMPETENCE = 10
MAX_TOTAL_COMPETENCE = 15
COMPETENCE_DEPART  = 5

# Variable : 
login = ""
motPasse = ""
choixMenu = ''
valeurComp = None
choixInventaire = None

listeCompetence = [5,5,5]
listeCompString = "Stupidité", "Faiblesse", "Gaucherie"
listeInventaire = None
listeCasques = "Casse de bain", "Perruque", "Chapeau melon"
listeBottes = "Bottes de cowboy", "Bottes à talon haut", "Bottes à cap"		
listeGants = "Gants de travail", "Gant de baseball", "Gants de meurtrier"

erreur = None
quitter = None
totalCompetence = None

# Début du code
os.system("cls")

erreur = False
quitter = False
# for i < 2 :
# NE COMPREND PAS CETTE PARTIE DU CODE, À REVOIR ABSOLUMENT À LA FIN DU CODE

print("Veuillez entrer le login : ")    
login = input(" > ")

print("Veuillez entrer votre mot de passe : ")
motPasse = input(" > ")

if login != BON_LOGIN or motPasse != BON_PASSWORD :
    erreur = True

while erreur == True : 
    print("Erreur dans le login ou le mot de pass")
    print("Veuillez (r)ecommencer ou (q)uitter : ")
    choixMenu = input(" > ")

    while choixMenu != QUITTER and choixMenu != RECOMMENCER : 
        print("L'option choisie n'est pas valide ! Faite à nouveau un choix !")
        print("Veuillez (r)ecommencer ou (q)uitter : ")
        input(" > ")
    
    os.system("cls")

    if choixMenu == RECOMMENCER : 
        print("Veuillez entrer le login  : ")
        login = input(" > ")
        
        print("Veuillez entrer le mot de passe : ")
        motPasse = input(" > ")

        if motPasse != BON_PASSWORD or login != BON_LOGIN : 
            erreur = True
        else : 
            erreur = False
    else : 
        erreur = False
        quitter = True 

while choixMenu != QUITTER :
    os.system("cls")

    print("(C)ompétences")
    print("(I)nventaire")
    print("(Q)uitter")

    print("\nFaites votre choix : ")
    choixMenu = input(" > ")

    if choixMenu == COMPETENCE :
        while choixMenu != MENU_PRINCIPAL : 
            os.system("cls")

            for i in range(3)  :
                print(f"{i + 1}:{listeCompString[i]}    {listeCompetence[i]}")
            print("\nFaites votre choix : ")
            choixMenu = input(" > ")

            print(f"La valeur de la compétence choisi est de {listeCompetence[i - 1]}")
            print("Entrez la nouvelle valeur : ")
            valeurComp = input(" > ")

            while valeurComp < 0 or valeurComp > MAX_COMPETENCE : 
                print("La valeur doit être comprise entre 0 et 10 !")
                print("Entrez la nouvelle valeur : ")
                valeurComp = input(" > ")

            totalCompetence = 0

            for i in range(3) : 
                if i != choixMenu : 
                    totalCompetence = totalCompetence + listeCompetence[i - 1]
            
            if totalCompetence + valeurComp > MAX_TOTAL_COMPETENCE :
                print(f"Le total des compétence ne doit pas dépasser {MAX_TOTAL_COMPETENCE}")

                valeurComp = MAX_COMPETENCE - totalCompetence
            
            listeCompetence[choixMenu - 1] = valeurComp

            for i in range(3) : 
                print(f"{i + 1}:{listeCompString[i]}    {listeComptence[i]}")

            print("(M)enu principal ou (e)diter une autre compétence : ")
            choixMenu = input(" > ")
        
    elif choixMenu == INVENTAIRE :
        while choixMenu != MENU_PRINCIPAL : 
            os.system("cls")

            print("(C)asque")
            print("(B)otte")
            print("(G)ants")
            print("(M)enu principal")

            print("\nFaites votre choix : ")
            choixMenu = input(" > ")

            os.system("cls")

            if choixMenu == CASQUES :
                print("Casques : ", listeCasques[listeInventaire[0]])

                for i in range(3) :
                    print(i, ":", listeCasques[i - 1])
                
                print("Faites votre choix : ") 
                choixInventaire = input(" > ")

                listeInventaire[0] = choixInventaire - 1
            elif choixMenu == BOTTES :
                print("Bottes : ", listeBottes[listeInventaire[1]])

                for i in range(3) : 
                    print(i, ":", listeBottes[i - 1])
                
                print("\nFaites votre choix")
                choixInventaire = input(" > ")

                listeInventaire[1] = choixInventaire - 1
            elif choixMenu == GANTS : 
                print("Gants :", listeGants[listeInventaire[2]])
                for i in range(3) : 
                    print(i, ":", listeGants[i - 1])

                print("\nFaites votre choix : ")
                choixInventaire = input(" > ")
                listeInventaire[2] = choixInventaire - 1

os.system("cls")

for i in range(3) : 
    print(i, ":", listeCompString[i - 1], "\t:", listeCompetence[i - 1])

print("\nCasques : ", listeCasques[listeInventaire[0]])
print("Bottes : ", listeBottes[listeInventaire[1]])
print("Gants : ", listeGants[listeInventaire[2]])

print("\nMerci d'avoir fait confiance à notre équipe !")
time.sleep(3)