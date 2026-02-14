import customtkinter as ctk
from ..colors.colors import BUTTON

def noteblock(app):
    texto = ctk.CTkTextbox(app, state='normal')
    texto.pack(fill='both', expand=True)

    save_btn = ctk.CTkButton(app,text="Salvar",fg_color=BUTTON)
    open_btn = ctk.CTkButton(app,text="Abrir",fg_color=BUTTON)

    save_btn.pack(side='right')
    open_btn.pack(side='left')