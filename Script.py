import tkinter as tk

marques = ['fiat', 'ferrari', 'mclaren', 'bmw', 'rolls-Royce', 'renault', 'lamborghini']
preferences = {marque: 0 for marque in marques}
buttons = {}

def update_preferences(marque):
    preferences[marque] += 1
    sort_buttons()

def sort_buttons():
    sorted_preferences = sorted(preferences.items(), key=lambda x: x[1], reverse=True)
    for i, (marque, _) in enumerate(sorted_preferences):
        buttons[marque].pack_forget()
        buttons[marque].pack(side=tk.TOP, pady=5)

def show_preferences():
    sorted_preferences = sorted(preferences.items(), key=lambda x: x[1], reverse=True)
    print("Classement des marques de voitures par ordre de préférence :")
    for marque, count in sorted_preferences:
        print(f"{marque}: {count} clics")

root = tk.Tk()
root.title("Classement des marques de voitures")

for marque in marques:
    button = tk.Button(root, text=marque, command=lambda marque=marque: update_preferences(marque))
    buttons[marque] = button
    button.pack(side=tk.TOP, pady=5)

show_preferences_button = tk.Button(root, text="Afficher le classement", command=show_preferences)
show_preferences_button.pack()

root.mainloop()