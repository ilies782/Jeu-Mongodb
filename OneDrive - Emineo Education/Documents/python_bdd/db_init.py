from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client["python_bdd"]

collection_personnages = db["personnages"]
collection_monstres = db["monstres"]
collection_scores = db["meilleurs_scores"]

personnages = [
    {"nom": "Guerrier", "attaque": 15, "defense": 10, "pv": 100},
    {"nom": "Mage_noir", "attaque": 20, "defense": 5, "pv": 80},
    {"nom": "Archer", "attaque": 12, "defense": 8, "pv": 90},
    {"nom": "Paladin_des_mers", "attaque": 14, "defense": 12, "pv": 110},
    {"nom": "Voleur", "attaque": 16, "defense": 6, "pv": 85},
    {"nom": "Berserker", "attaque": 18, "defense": 7, "pv": 95},
    {"nom": "Druide", "attaque": 13, "defense": 9, "pv": 100},
    {"nom": "Chasseur", "attaque": 14, "defense": 8, "pv": 90},
    {"nom": "Assassin", "attaque": 20, "defense": 4, "pv": 75},
    {"nom": "Chevalier", "attaque": 15, "defense": 15, "pv": 120},
]


collection_personnages.insert_many(personnages)
print("Personnages insérés avec succès !")

monstres = [
    {"nom": "Gobelin", "attaque": 8, "defense": 5, "pv": 50},
    {"nom": "Orc", "attaque": 12, "defense": 8, "pv": 80},
    {"nom": "Dragon", "attaque": 25, "defense": 20, "pv": 200},
    {"nom": "Zombie", "attaque": 6, "defense": 4, "pv": 40},
]

collection_monstres.insert_many(monstres)
print("Monstres insérés avec succès !")


meilleurs_scores = [
    {"joueur": "Alice", "score": 1500},
    {"joueur": "Bob", "score": 1200},
    {"joueur": "Charlie", "score": 1000},
]

collection_scores.insert_many(meilleurs_scores)
print("Scores insérés avec suc cès !")



