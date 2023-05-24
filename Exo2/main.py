import random
from joueurs import Joueur, ClassementJoueurs
from personnages import Personnage, ListePersonnages
from attaques import Attaque, ListeAttaques
from match import Match


classement_joueurs = ClassementJoueurs()
liste_personnages = ListePersonnages()

# Fonction pour choisir le pseudo de tous les joueurs
def choisir_pseudos():
    nb_joueurs = int(input("Entrez le nombre de joueurs : "))
    for i in range(nb_joueurs):
        pseudo = input(f"Entrez le pseudo du joueur {i+1} : ")
        joueur = Joueur(pseudo)
        classement_joueurs.ajouter_joueur(joueur)
    print("Pseudos des joueurs enregistrés !")

# Fonction pour choisir le personnage de tous les joueurs
def choisir_personnages():
    for joueur in classement_joueurs.joueurs:
        print(f"\nJoueur : {joueur.pseudo}")
        liste_personnages.afficher_personnages()
        choix = int(input("Choisissez un personnage (entrez le numéro correspondant) : "))
        nom_personnage = liste_personnages.personnages[choix-1]
        personnage = Personnage(nom_personnage)
        joueur.champion_choisi = personnage
        print(f"Personnage {personnage.nom} choisi pour le joueur {joueur.pseudo} !")

# Fonction pour effectuer le tirage au sort des matchs
def tirage_matchs():
    print("\n=== Tirage au sort des matchs ===")
    random.shuffle(classement_joueurs.joueurs)
    nb_matchs = len(classement_joueurs.joueurs) // 2
    for i in range(nb_matchs):
        joueur1 = classement_joueurs.joueurs[i * 2]
        joueur2 = classement_joueurs.joueurs[i * 2 + 1]
        print(f"Match {i+1} : {joueur1.pseudo} ({joueur1.champion_choisi.nom}) vs {joueur2.pseudo} ({joueur2.champion_choisi.nom})")


def jouer_matchs(matchs):
    print("\n=== Début des matchs ===")
    for match in matchs:
        print(f"\nMatch : {match.joueur1.pseudo} vs {match.joueur2.pseudo}")
        vainqueur = match.jouer_match()
        print(f"Le vainqueur du match est : {vainqueur.pseudo}")


# Fonction principale du jeu
def jouer():
    choisir_pseudos()
    choisir_personnages()
    tirage_matchs()


# Point d'entrée de l'application
if __name__ == "__main__":
    jouer()
