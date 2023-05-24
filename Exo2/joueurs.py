class Joueur:
    def __init__(self, pseudo):
        self.pseudo = pseudo
        self.match_joue = 0
        self.match_gagne = 0
        self.match_perdu = 0
        self.champion_choisi = None

    def afficher_statistiques(self):
        print(f"Pseudo : {self.pseudo}")
        print(f"Matchs joués : {self.match_joue}")
        print(f"Matchs gagnés : {self.match_gagne}")
        print(f"Matchs perdus : {self.match_perdu}")
        print(f"Champion choisi : {self.champion_choisi}")


class ClassementJoueurs:
    def __init__(self):
        self.joueurs = []

    def ajouter_joueur(self, joueur):
        self.joueurs.append(joueur)

    def afficher_classement(self):
        classement = sorted(self.joueurs, key=lambda x: x.match_gagne, reverse=True)
        print("Classement des joueurs :")
        for i, joueur in enumerate(classement):
            print(f"{i+1}. {joueur}")