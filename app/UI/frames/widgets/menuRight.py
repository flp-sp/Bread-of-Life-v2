import customtkinter as ctk
from .noteblock import noteblock
from ..colors.colors import *

def menuRight(app):
    tabview = ctk.CTkTabview(app,fg_color=BACKGROUND,segmented_button_fg_color=FRAMES,segmented_button_selected_color=BUTTON)
    tabview.pack(padx=5, pady=5, fill='y', expand=True)

    bloco_notas = tabview.add("Bloco de notas")
    passagens = tabview.add("Passagens salvas")
    tabview.set("Bloco de notas")

    noteblock(bloco_notas)
