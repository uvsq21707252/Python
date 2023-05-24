import random

# Liste des personnages & Attaques
personnages = ['Zeus', 'Hades', 'SanGoku', 'Naruto']


# Dictionnaire pour stocker les participants aux matchs
participants = {'Match 1': [], 'Match 2': [], 'Match Final': []}

# Fonction pour choisir les personnages des utilisateurs
def choisir_personnage(utilisateur):
    print(f"Utilisateur {utilisateur}, voici les personnages disponibles :")
    for i, personnage in enumerate(personnages):
        print(f"{i+1}. {personnage}")
    choix = int(input("Veuillez choisir le numéro du personnage : "))
    personnage = personnages[choix-1]
    personnages.remove(personnage)  # Supprimer le personnage choisi de la liste
    return personnage

# Choisir les personnages pour chaque utilisateur
for i in range(1, 5):
    personnage = choisir_personnage(i)
    if len(participants['Match 1']) < 2:
        participants['Match 1'].append(personnage)
    else:
        participants['Match 2'].append(personnage)

class CoupDeCombat:
    def __init__(self, nom, puissance):
        self.nom = nom
        self.puissance = puissance

    def effectuer_coup(self):
        print(f"Effectuer le coup de {self.nom} avec une puissance de {self.puissance}.")

# Création des instances de coups de combat
jab = CoupDeCombat("Jab", 10)
right_punch = CoupDeCombat("Right Punch", 20)
left_punch = CoupDeCombat("Left Punch", 20)
uppercut = CoupDeCombat("Uppercut", 30)
low_kick = CoupDeCombat("Low Kick", 15)
middle_kick = CoupDeCombat("Middle Kick", 25)
high_kick = CoupDeCombat("High Kick", 35)
coup_de_tete = CoupDeCombat("Coup de tête", 30)

# Utilisation des coups de combat
jab.effectuer_coup()
right_punch.effectuer_coup()
left_punch.effectuer_coup()
uppercut.effectuer_coup()
low_kick.effectuer_coup()
middle_kick.effectuer_coup()
high_kick.effectuer_coup()
coup_de_tete.effectuer_coup()


# Affichage des participants des deux premiers matchs
print("Les participants du Match 1 sont :", participants['Match 1'])
print("Les participants du Match 2 sont :", participants['Match 2'])

# Simuler les deux matchs
vainqueur_match1 = random.choice(participants['Match 1'])
vainqueur_match2 = random.choice(participants['Match 2'])

# Stocker les vainqueurs dans le match final
participants['Match Final'].extend([vainqueur_match1, vainqueur_match2])

# Affichage du match final
print("Le match final opposera", participants['Match Final'][0], "à", participants['Match Final'][1])

# Simuler les deux matchs
vainqueur_match_final = random.choice(participants['Match Final'])

# Affichage du match final
print("Le Grand Vainqueur Du Match Final est: ", vainqueur_match_final)