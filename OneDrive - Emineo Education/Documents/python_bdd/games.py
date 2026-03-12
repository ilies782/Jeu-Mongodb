import numpy.random as random
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017")
db = client["python_bdd"]
collection_personnages = db["personnages"]
collection_monstres = db["monstres"]


def choisir_perso():
   equipe=[] #J'initialise une liste vide pour stocker mon equipe
   personnages_total = list(collection_personnages.find({}))#on recherche dans toute la db et stocke les personnages dans personnages_total pour pas que les choix se supprime definitivement de la db
   i=0
   while i< 3:#Demande des choix (3 fois )
        personnage_estvalide= None 
        perso= input("Entrer le nom de votre choix") 
        for personnage in personnages_total: # On cherche le perso demander dans la liste des personnages
            if personnage["nom"] == perso: # On Verifie si le nom est compris dans la liste
                personnage_estvalide = personnage # Si oui, on le stock dans une variable
        if personnage_estvalide :  
         equipe.append(personnage_estvalide) # Si personnage valide on l'ajoute a l'equipe
         personnages_total.remove(personnage_estvalide)#  On le supprime de la db
         print(f"{perso} ajouté a l'equipe")
         i +=1
        else:
           print(" Personnage introuvable !")
   return equipe 
  
def choisir_monstre():
    liste_monstre_aleatoire= list(collection_monstres.find({})) #stocke les monstre dans une liste pour pas 
    monstre_aleatoire=random.choice(liste_monstre_aleatoire) #fonction qui va tirer au hasard un monstre 
    print(f"Le monstre choisi est {monstre_aleatoire['nom']}, PV : {monstre_aleatoire['pv']}, Attaque : {monstre_aleatoire['attaque']} et Defense:  {monstre_aleatoire['defense']}")
    return monstre_aleatoire


def attaque_monstre(equipe,monstre_aleatoire):
   for personnage in equipe: #On parcourt les perso de l'equipe
       degats_perso= personnage["attaque"] - monstre_aleatoire["defense"] # Je calcule les degats en fesant attention a la defense du monstre
       monstre_aleatoire["pv"] -=degats_perso # Je soustrains les pv du monstre avec les degats faites par le perso
       print(f"{personnage['nom']} attaque {monstre_aleatoire['nom']} et inflige {degats_perso} degats (PV monstre : {monstre_aleatoire["pv"]})")
       if monstre_aleatoire["pv"]<= 0: # Je verifie si le monstre est vaincu
                print(f"\nVictoire, {monstre_aleatoire['nom']} a ete vaincu")
                return 
         
def attaque_perso(equipe,monstre_aleatoire):
    attaque_perso_aleatoire=random.choice(equipe) # On commence par choisir un personnage aleatoire
    degats_monstre=monstre_aleatoire["attaque"] -attaque_perso_aleatoire["defense"] # On calcule les degats en fesant attention a la defense du perso
    attaque_perso_aleatoire["pv"]-=degats_monstre #On soustrains les pv du perso avec les degats faites par le monstre
    print(f"{monstre_aleatoire['nom']} attaque {attaque_perso_aleatoire['nom']} et inflige {degats_monstre} degats (PV {attaque_perso_aleatoire['nom']}: {attaque_perso_aleatoire['pv']})")
    if attaque_perso_aleatoire["pv"] <= 0: # Je verifie que le perso a ete vaincu et si oui le sortir de la liste
        print(f"\ndefaite {attaque_perso_aleatoire['nom']} a ete vaincu")
        equipe.remove(attaque_perso_aleatoire)
        if len(equipe) == 0: # Je verifie si tout les perso sont vaincus, si oui defaite et je sort du jeu
            print("Defaite de toute l'equipe")
            exit()
 

   
   
   


