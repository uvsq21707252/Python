Le code de l'exo2 est un programme Python avec 4 modules différents :

C'est un Jeux de combats, on peux y choisir son pseudo de joueur, les personnages de combats. Ensuite un tirage aléatoire est fait pour déterminer les matchs, chaque match de déroule à la suite de l'autre, pendant ces matchs les joueurs choississent quels attaques faire, chaucn leur tour, un joueur attaque à son tour.
Le gagnant est celui qui parvient à faire descendre la vie de son adversaire à 0 en premier.
Le gagnant passe au prochani tour jusqu'au match final.

Le module joueurs.py contient la classe Joueur et la classe ClassementJoueurs.
Le module personnages.py contient la classe Personnage et la classe ListePersonnages.
Le module attaques.py contient la classe Attaque et la classe ListeAttaques.

Le module main.py est le point d'entrée de l'application et permet de gérer les actions principales du jeu.
Le module main.py permet aux joueurs de choisir leur pseudo, leur personnage, effectue un tirage au sort des matchs, et lance les matchs un par un. Chaque joueur a la possibilité de jouer une attaque lors de son tour.
