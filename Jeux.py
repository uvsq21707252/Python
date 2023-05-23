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