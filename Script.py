marques = ['fiat', 'ferrari', 'mclaren', 'bmw', 'rolls-Royce', 'renault', 'lamborghini']

marques_triees = sorted(marques, key=len)

print("Marques de voitures triées par ordre croissant de longueur de nom :")
for marque in marques_triees:
    print(marque)