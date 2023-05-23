import tkinter as tk

# Fonction appelée lorsque la souris bouge
def on_mouse_move(event):
    x = event.x  # Coordonnée X de la souris
    y = event.y  # Coordonnée Y de la souris

    # Mettre à jour la couleur du pixel correspondant aux coordonnées de la souris
    canvas.create_rectangle(x, y, x+1, y+1, fill='#%02x%02x%02x' % (x % 256, y % 256, (x+y) % 256))

# Fonction appelée lorsque le bouton Effacer est cliqué
def effacer_canvas():
    canvas.delete("all")  # Effacer tous les éléments du canvas

# Créer une fenêtre
window = tk.Tk()
window.title("Canvas interactif")

# Créer un canvas de 300x300 pixels
canvas = tk.Canvas(window, width=300, height=300, bg='white')
canvas.pack()

# Lier l'événement de mouvement de souris à la fonction on_mouse_move
canvas.bind("<Motion>", on_mouse_move)

# Créer un bouton Effacer
effacer_button = tk.Button(window, text="Effacer", command=effacer_canvas)
effacer_button.pack()

# Lancer la boucle principale de l'interface graphique
window.mainloop()
