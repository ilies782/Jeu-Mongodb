def print_menu():
    print("1. Lancer le jeu")
    print("2. Voir l'historique")   
    print("3. Quitter le jeu")  

def recuperer_nombre_valid(min_val, max_val, message):
    saisie = input("Entrez votre choix : ")
    while (saisie > 1) and (saisie < 3):
      return saisie
    
def main():
    recuperer_nombre_valid(1,5,"Choisir une options")


