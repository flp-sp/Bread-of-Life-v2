import customtkinter as ctk
from .noteblock import noteblock

def menuRight(app):
    tabview = ctk.CTkTabview(app)
    tabview.pack(padx=5, pady=5, fill='y', expand=True)

    bloco_notas = tabview.add("Bloco de notas")
    passagens = tabview.add("Passagens salvas")
    tabview.set("Bloco de notas")

    noteblock(bloco_notas)
