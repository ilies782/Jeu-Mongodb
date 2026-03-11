from utills import afficher_perso, afficher_equipe
from games import choisir_perso
from pymongo import MongoClient


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
      if choix == 1 :
        pass
      elif choix == 2 :
       print("Voici l'historique des jeux")
        # historique()
       exit()
      else:
        print(" Le jeu est eteint.")
        exit()

def demarrer_jeux(message):
    utilisateur = input(message)
    print(f"Bienvenue  {utilisateur} !")
    afficher_perso()
    choisir_perso()
    afficher_equipe()


def main():
    print_menu()
    choix = recuperer_nombre_valid(1,3,"Choisir une options :")
    print(f"Tu as choisi : {choix}")
    option_choisi(choix)
    demarrer_jeux("Quel est votre nom d'utilisateur : ")



main()



