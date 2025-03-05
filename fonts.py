import tkinter as tk
from tkinter import font

root = tk.Tk()
available_fonts = list(font.families())
root.destroy()

print(available_fonts)
