import customtkinter as ctk
from ..colors.colors import *
from ...parser.parser import parseBible
from ..textDisplay import retornarLocal

bibliaNaa = parseBible('../src/PortugueseNAABible.xml')
#bibliaKj = parseBible('../src/EnglishKJBible.xml')

global glob_livros
glob_livros = '1'

global selecchap
selecchap = None

global _app
_app = None

def set_app(application):
    global _app
    _app = application

def printchapt(app):
    global selecchap
    global glob_livros

    if selecchap is not None:
        selecchap.pack_forget()
        selecchap = None

    selecchap = ctk.CTkScrollableFrame(app,height=250,fg_color=BACKGROUND)
    capLabel = ctk.CTkLabel(selecchap,text="Capitulos")
    capLabel.pack()
    for capitulos in bibliaNaa[glob_livros]:
        ctk.CTkButton(selecchap,text=capitulos, command=lambda c=capitulos:retornarLocal(c, glob_livros),fg_color=BUTTON).pack()
    selecchap.pack(padx=4,pady=4)

def currentBook(livros):
    global glob_livros
    glob_livros = livros
    printchapt(_app)

def menuSelect(app):
    selectbook = ctk.CTkScrollableFrame(app,fg_color=BACKGROUND)
    livroLabel = ctk.CTkLabel(selectbook,text="Livros")
    livroLabel.pack()
    for livros in bibliaNaa:
        ctk.CTkButton(selectbook,text=livros, command=lambda l=livros:currentBook(l),fg_color=BUTTON).pack()
    selectbook.pack()