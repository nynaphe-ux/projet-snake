"""
Programme Snake version 1

"""
from tkinter import * # Importation de la bibliothèque  Tkinter 

# On crée un environnement Tkinter
tk = Tk()
   
# On crée un canevas dans l'environnement Tkinter d'une taille de 500x500
# Ce constructeur prend comme premier paramètre l'objet dans lequel il sera
# intégré (ici l'environnement Tkinter)
# Les trois autres paramètres permettent de spécifier la taille et la couleur
# de fond du canevas
can = Canvas(tk, width=500, height=500, bg='black')
def computeNextFrame(numframe,coordonnee):
    print(numframe)
    numframe= numframe + 1
    can.delete('all')
    if coordonnee <= 0:
        coordonnee = 0
    else:
        coordonnee += -20
    can.create_rectangle(coordonnee,200, coordonnee +20 , 220, outline='yellow',fill='red')
    tk.after(100, lambda:computeNextFrame(numframe,coordonnee))
# On affiche le canevas
can.pack()
computeNextFrame(0, 500)
# lancement de la boucle principale qui écoute les évènements (claviers...)
tk.mainloop() # Cet appel doit être la derniere instruction du programme




