from attaques import Attaque, ListeAttaques
class Personnage:
    def __init__(self, nom):
        self.nom = nom

    def afficher_informations(self):
        print(f"Nom du personnage : {self.nom}")


class ListePersonnages:
    def __init__(self):
        self.personnages = ["Zeus", "Naruto", "Sasuke", "Tobi", "Luffy", "Mike Tyson", "Zlatan", "Lucario"]

    def afficher_personnages(self):
        print("Liste des personnages disponibles :")
        for personnage in self.personnages:
            print(personnage)