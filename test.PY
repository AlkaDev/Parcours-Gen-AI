import tkinter as tk

# Dimensions de l'écran (W = Largeur, H = Hauteur)
W = 900
H = 600

# Largeur de la route (WR)
WR = 180

root = tk.Tk()
root.title("Intersection de Routes")

canvas = tk.Canvas(root, width=W, height=H, bg="#05932B")
canvas.pack()

# ======================
# 1. ROUTE HORIZONTALE 
# ======================
# partant des formules du cahier : y0 = (H - WR) / 2  et  y1 = (H + WR) / 2
x0_h = 0
x1_h = W
y0_h = (H - WR) / 2
y1_h = (H + WR) / 2

canvas.create_rectangle(x0_h, y0_h, x1_h, y1_h, fill="#555555", outline="#555555")


# ====================
# 2. ROUTE VERTICALE 
# ====================
# partant des Formules du cahier : x0 = (W - WR) / 2  et  x1 = (W + WR) / 2
x0_v = (W - WR) / 2
x1_v = (W + WR) / 2
y0_v = 0
y1_v = H

canvas.create_rectangle(x0_v, y0_v, x1_v, y1_v, fill="#555555", outline="#555555")


# Ligne blanche du milieu (y = H / 2)
canvas.create_line(0, H / 2, W, H / 2, fill="white", width=3, dash=(20, 10))

# Ligne jaune du haut : A'' -> y = (H / 2) - (WR / 4)
y_jaune_haut = (H / 2) - (WR / 4)
canvas.create_line(0, y_jaune_haut, W, y_jaune_haut, fill="yellow", width=2)

# Ligne jaune du bas : A' -> y = (H / 2) + (WR / 4)
y_jaune_bas = (H / 2) + (WR / 4)
canvas.create_line(0, y_jaune_bas, W, y_jaune_bas, fill="yellow", width=2)


# Ligne blanche du milieu (x = W / 2)
canvas.create_line(W / 2, 0, W / 2, H, fill="white", width=3, dash=(20, 10))

# Ligne jaune de gauche : B'' -> x = (W / 2) - (WR / 4)
x_jaune_gauche = (W / 2) - (WR / 4)
canvas.create_line(x_jaune_gauche, 0, x_jaune_gauche, H, fill="yellow", width=2)

# Ligne jaune de droite : B' -> x = (W / 2) + (WR / 4)
x_jaune_droite = (W / 2) + (WR / 4)
canvas.create_line(x_jaune_droite, 0, x_jaune_droite, H, fill="yellow", width=2)

root.mainloop()

