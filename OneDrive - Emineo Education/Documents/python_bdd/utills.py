#On recupere la base de donnee
from games import choisir_perso
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017")
db = client["python_bdd"]
collection_personnages = db["personnages"]

#Creation de la fonction
def afficher_perso():
    print(" Choissiez 3 personnages parmi ceux proposer (un par un ) :")
    for personnage in collection_personnages.find({}) : # Recuperer les valeur dans la db
        print("Nom :", personnage["nom"], end= ' ')# Afficher les personnages disponible
        print("Attaque :", personnage["attaque"], end= ' ')
        print("Defense :", personnage["defense"], end= ' ' )
        print("PV : ", personnage["pv"], end= ' ')
        print("-----------------------") 

def afficher_equipe(equipe):
   print("\nVotre équipe de gagnant :")
   for i in equipe: # On affiche l'equipe 
        print(i["nom"], "- Attaque:", i["attaque"], "Defense:", i["defense"], "PV:", i["pv"])
   




    



