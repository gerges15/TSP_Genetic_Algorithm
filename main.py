import tkinter as tk
from controller.tspController import TSPApp

if __name__ == "__main__":
    root = tk.Tk()
    app = TSPApp(root)
    root.mainloop()
