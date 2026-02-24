import customtkinter as ctk
from .colors.colors import *
from ..frames.widgets.pickLocation import menuSelect, set_app

def leftFrame(app):
    frame = ctk.CTkFrame(app,fg_color=FRAMES)
    frame.pack(side='left', fill='y')

    menuSelect(frame)

    set_app(frame)