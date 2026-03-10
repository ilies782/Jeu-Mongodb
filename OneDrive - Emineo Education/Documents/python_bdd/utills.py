#On recupere la base de donnee
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017")
db = client["python_bdd"]
collection_personnages = db["personnages"]
#Creation de la fonction
def choisir_perso():
    print(" Choissiez 3 personnages parmi ceux proposer (un par un ) :")
    for personnage in collection_personnages.find({}) : # Recupere les valeur dans la liste 
        print("Nom :", personnage["nom"], end= ' ')# Affiche les personnages
        print("Attaque :", personnage["attaque"], end= ' ')
        print("Defense :", personnage["defense"], end= ' ' )
        print("PV : ", personnage["pv"], end= ' ')
        print("-----------------------") 
    perso= input("Entrer le nom de votre choix") #Demande des choix (3 fois )
    for personnage in collection_personnages.find({}) :
        perso_choisi[]= collection_personnages.pop(perso)
        print("Nom :", personnage["nom"], end= ' ')
        print("Attaque :", personnage["attaque"], end= ' ')
        print("Defense :", personnage["defense"], end= ' ' )
        print("PV : ", personnage["pv"], end= ' ')
        print("-----------------------") 

       

choisir_perso()