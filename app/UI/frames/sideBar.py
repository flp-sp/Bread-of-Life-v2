import customtkinter as ctk
from .colors.colors import FRAMES

from .widgets.menuRight import menuRight

def sideBar(app):
    frame = ctk.CTkFrame(app,fg_color=FRAMES)
    frame.pack(side='right', fill='y')

    menuRight(frame)