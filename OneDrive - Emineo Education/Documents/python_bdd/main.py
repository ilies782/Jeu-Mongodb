from utills import afficher_perso, afficher_equipe
from games import choisir_perso, choisir_monstre,attaque_monstre,attaque_perso
from pymongo import MongoClient


def print_menu():
    print("1. Lancer le jeu")
    print("2. Voir l'historique")   
    print("3. Quitter le jeu")  

def recuperer_nombre_valid(min_val, max_val, message):
    saisie = int (input(message)) #Je demande a l'utilisateur de taper un nombre compris entre 1 et 3
    while ((saisie < min_val) or (saisie > max_val)): # Je fait une boucle pour que meme si il met plus que 3 le programme lui redemande le choix
        print(f"Erreur, entrez un nombre entre {min_val} et {max_val}")
        saisie = int(input(message))
    return int(saisie)

def option_choisi(choix):
      if choix == 1 : # Si il choissis le choix 1 le programme se lance 
        pass
      elif choix == 2 : # Si il choisis le choix 2 je lance la fonction historique
       print("L'historique de jeux n'est pas encore fini")
       exit()
      else: # Si il fait le choix 3 le programme quitte
        print(" Le jeu est eteint.")
        exit()

def demarrer_jeux(message): #Je demande un nom d'utilisateur 
    utilisateur = input(message)
    print(f"Bienvenue  {utilisateur} !")
    afficher_perso()# On affiche les fonctions creer dans les autre fichier du code
    equipe=choisir_perso()
    afficher_equipe(equipe)
    monstre_aleatoire=choisir_monstre()
    while monstre_aleatoire["pv"] > 0: # Je dois creer une boucle pour que les personnages attaque et le monstre reponde tant que le monstre est en vie
       attaque_monstre(equipe,monstre_aleatoire)
       if monstre_aleatoire ["pv"]> 0:
          attaque_perso(equipe,monstre_aleatoire)


def main():
    print_menu()
    choix = recuperer_nombre_valid(1,3,"Choisir une options :")
    print(f"Tu as choisi : {choix}")
    option_choisi(choix)
    demarrer_jeux("Quel est votre nom d'utilisateur : ")



main()



