
def print_menu():
    print("1. Lancer le jeu")
    print("2. Voir l'historique")   
    print("3. Quitter le jeu")  

def recuperer_nombre_valid(min_val, max_val, message):
    saisie = int (input(message))
    while ((saisie < min_val) or (saisie > max_val)):
        print(f"Erreur, entrez un nombre entre {min_val} et {max_val}")
        saisie = int(input(message))
    return int(saisie)

def option_choisi(choix):
   for nombre in range(1):
      if choix == 1 :
        continue
      elif choix == 2 :
       print("Voici l'historique des jeux")
        # historique()
       exit()
      else:
        exit()
        print(" Le jeu est eteint.")

def demarrer_jeux(message):
    utilisateur = input(message)
    print(f"Bienvenue  {utilisateur} !")


def main():
    print_menu()
    choix = recuperer_nombre_valid(1,5,"Choisir une options :")
    print(f"Tu as choisi : {choix}")
    option_choisi(choix)
    demarrer_jeux("Quel est votre nom d'utilisateur : ")


main()


