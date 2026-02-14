import customtkinter as ctk
from ..parser.parser import parseBible
from .colors.colors import *

bibliaNaa = parseBible('../src/PortugueseNAABible.xml')
bibliaKj = parseBible('../src/EnglishKJBible.xml')

def atualizarTextoNaa(livro, cap):
    global textoNaa
    if textoNaa is not None:
        textoNaa.configure(state='normal')
        textoNaa.delete('0.0', 'end')  # limpa o texto antigo
        for verso in bibliaNaa[livro][cap]:
            textoNaa.insert('end', f"{verso} {bibliaNaa[livro][cap][verso]}\n")
        textoNaa.configure(state='disabled')

def atualizarTextoKj(livro, cap):
    global textoKj
    if textoKj is not None:
        textoKj.configure(state='normal')
        textoKj.delete('0.0', 'end')
        for verso in bibliaKj[livro][cap]:
            textoKj.insert('end', f"{verso} {bibliaKj[livro][cap][verso]}\n")
        textoKj.configure(state='disabled')

def retornarLocal(cap, liv):
    global glob_liv, glob_cap
    glob_liv = liv
    glob_cap = cap

    atualizarTextoNaa(liv, cap)
    atualizarTextoKj(liv, cap)

def menuBiblia(master):
    global textoNaa, textoKj, menuBibliaRef
    menuBibliaRef = ctk.CTkTabview(master,fg_color=FRAMES,segmented_button_fg_color=FRAMES,segmented_button_selected_color=BUTTON)
    menuBibliaRef.pack(padx=5, pady=5, fill='both', expand=True)

    kjv = menuBibliaRef.add("King James")
    naa = menuBibliaRef.add("Nova Almeida")
    menuBibliaRef.set("Nova Almeida")

    # cria os textboxes inicialmente com o primeiro livro/capítulo
    textoNaa = ctk.CTkTextbox(naa, height=1000, activate_scrollbars=False,fg_color=FRAMES)
    textoNaa.pack(fill='both', expand=True)
    atualizarTextoNaa('1', '1')

    textoKj = ctk.CTkTextbox(kjv, height=1000, activate_scrollbars=False,fg_color=FRAMES)
    textoKj.pack(fill='both', expand=True)
    atualizarTextoKj('1', '1')
    
    