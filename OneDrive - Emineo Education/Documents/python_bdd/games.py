import numpy.random as random
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017")
db = client["python_bdd"]
collection_personnages = db["personnages"]
collection_monstres = db["monstres"]


def choisir_perso():
   equipe=[]
   personnages_total = list(collection_personnages.find({}))
   for i in range (3): #Demande des choix (3 fois )
        perso= input("Entrer le nom de votre choix") 
        for personnage in personnages_total: # Trouver dans la liste creer le choix de perso demander 
            if personnage["nom"] == perso: #Verifier si le nom est compris dans la liste
                personnage_estvalide = personnage
        if personnage_estvalide: 
         equipe.append(personnage) # Si personnage valide on l'ajoute a l'equipe
         personnages_total.remove(personnage_estvalide)#  On le supprime de la db
         print(f"{perso} ajouté a l'equipe")
        else:
           print(" Personnage introuvable !")
  


def choisir_monstre():
    liste_monstre_aleatoire= list(collection_monstres.find({})) #stocke les monstre dans une liste
    monstre_aleatoire=random.choice(liste_monstre_aleatoire)#fonction qui va tirer au hasard un monstre 
    print(f"Le monstre choisi est {monstre_aleatoire['nom']}, PV : {monstre_aleatoire['pv']}, Attaque : {monstre_aleatoire['attaque']} et Defense:  {monstre_aleatoire['defense']}")



    #Recuperer les 3 personnage dans la liste equipe
    
    #Recuperer les PV, attaque et defense des hero et stocker dans des variables
    
    #Creer fonction de combat qui va affecter lezs pv et les degats
    
    #Utiliser la fonction random pour faire attaquer le monstre


