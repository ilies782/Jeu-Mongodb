from pymongo import MongoClient

def get_all_characters():
    client = MongoClient("mongodb://localhost:27017")
    db = client["python_bdd"]
    return list(db.personnages.find())

def choisir_equipe():
    personnages = get_all_characters()

    print("Choisissez votre équipe :")

    for i, p in enumerate(personnages):
        print(i + 1, p["nom"])

    choix = input("Entrez 3 numéros (ex: 1 2 3) : ").split()

    equipe = [
        personnages[int(choix[0]) - 1],
        personnages[int(choix[1]) - 1],
        personnages[int(choix[2]) - 1]
    ]

    return equipe


equipe = choisir_equipe()

print("Votre équipe :")
for p in equipe:
    print(p["nom"])
