import customtkinter as ctk
from ..colors.colors import *
from tkinter import filedialog

global texto

def openFile():
    global texto
    caminho = filedialog.askopenfilename(
        title="Abrir arquivo",
        filetypes=[("Arquivos de texto", "*.txt")]
    )
    with open(caminho,'r',encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
        texto.insert('0.0',conteudo)

def saveFile():
    global texto
    caminho = filedialog.asksaveasfilename(
        title="Salvar arquivo",
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt")]
    )
    
    if caminho:
        with open(caminho, "w", encoding="utf-8") as f:
            f.write(texto.get("0.0", ctk.END))

def noteblock(app):
    global texto
    texto = ctk.CTkTextbox(app, state='normal',fg_color=FRAMES)
    texto.pack(fill='both', expand=True)

    save_btn = ctk.CTkButton(app,text="Salvar",fg_color=BUTTON,command=saveFile)
    open_btn = ctk.CTkButton(app,text="Abrir",fg_color=BUTTON,command=openFile)

    save_btn.pack(side='right',pady=4)
    open_btn.pack(side='left',pady=4)