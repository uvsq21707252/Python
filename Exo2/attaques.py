
class Attaque:
    def __init__(self, nom, puissance):
        self.nom = nom
        self.puissance = puissance

    def afficher_informations(self):
        print(f"Attaque : {self.nom}")
        print(f"Puissance : {self.puissance}")


class ListeAttaques:
    def __init__(self):
        self.attaques = [
            Attaque("jab", 5),
            Attaque("crochet du droit", 10),
            Attaque("crochet du gauche", 10),
            Attaque("uppercut", 20),
            Attaque("lowkick", 5),
            Attaque("middlekick", 20),
            Attaque("highkick", 30),
            Attaque("coup de boule", 30)
        ]

    def afficher_attaques(self):
        print("Liste des attaques :")
        for attaque in self.attaques:
            attaque.afficher_informations()