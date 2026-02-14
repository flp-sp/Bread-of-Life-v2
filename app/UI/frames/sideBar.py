import customtkinter as ctk
from .colors.colors import *

from .widgets.menuRight import menuRight

def sideBar(app):
    frame = ctk.CTkFrame(app,fg_color=BACKGROUND)
    frame.pack(side='right', fill='y')

    menuRight(frame)