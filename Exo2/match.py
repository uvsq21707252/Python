from personnages import ListeAttaques

class Match:
    def __init__(self, joueur1, joueur2):
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.vie_joueur1 = 100
        self.vie_joueur2 = 100
        self.attaque_joueur1 = None
        self.attaque_joueur2 = None
        self.liste_attaques = ListeAttaques()

    def effectuer_tour(self):
        # Joueur 1 attaque Joueur 2
        if self.attaque_joueur1 is None:
            self.choisir_attaque(self.joueur1, self.joueur2)
        self.utiliser_attaque(self.attaque_joueur1, self.joueur1, self.joueur2)
        self.attaque_joueur1 = None

        # Vérifier si Joueur 2 est mort
        if self.vie_joueur2 <= 0:
            return self.joueur1

        # Joueur 2 attaque Joueur 1
        if self.attaque_joueur2 is None:
            self.choisir_attaque(self.joueur2, self.joueur1)
        self.utiliser_attaque(self.attaque_joueur2, self.joueur2, self.joueur1)
        self.attaque_joueur2 = None

        # Vérifier si Joueur 1 est mort
        if self.vie_joueur1 <= 0:
            return self.joueur2

        return None

    def choisir_attaque(self, attaquant, defenseur):
        print(f"\nJoueur {attaquant.pseudo}, c'est à votre tour !")
        self.liste_attaques.afficher_attaques()
        choix = int(input("Choisissez une attaque (entrez le numéro correspondant) : "))
        attaque = self.liste_attaques.attaques[choix-1]
        attaquant.attaque_utilisee = attaque
        print(f"Le joueur {attaquant.pseudo} a choisi l'attaque : {attaque}")

    def utiliser_attaque(self, attaque, attaquant, defenseur):
        puissance = attaque.puissance
        defenseur.vie -= puissance
        print(f"\nLe joueur {attaquant.pseudo} utilise {attaque.nom} sur le joueur {defenseur.pseudo} !")
        print(f"Le joueur {defenseur.pseudo} perd {puissance} points de vie.")
        print(f"Points de vie restants pour le joueur {defenseur.pseudo} : {defenseur.vie}")

