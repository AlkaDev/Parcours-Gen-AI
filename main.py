import tkinter as tk

# Création de la fenêtre
root = tk.Tk()

root.title("Simulation trafic routier")

# Création du canvas
canvas = tk.Canvas(
    root,
    width=900,
    height=600,
    bg="#056920"
)

canvas.pack()

# Classe pour dessiner la route
class Route:

 def dessiner(self):

    # Route horizontale
    canvas.create_rectangle(
        0,
        200,
        900,
        400,
        fill="#555555",
        outline=""
    )

    # Route verticale
    canvas.create_rectangle(
        350,
        0,
        550,
        600,
        fill="#555555",
        outline=""
    )

# Création de la route
route = Route()

# Dessin de la route
route.dessiner()



root.mainloop()

