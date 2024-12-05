import tkinter as tk
from controller.tspController import TSPGUI

if __name__ == "__main__":
    root = tk.Tk()
    app = TSPGUI(root)
    root.mainloop()
