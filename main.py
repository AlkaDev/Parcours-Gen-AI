import tkinter as tk

root = tk.Tk()
root.title("similation de route")

canvas = tk.Canvas(root, width=900, height=600, bg="#056920")
canvas.pack()

class Route:  pass
route = Route()

root.mainloop()

