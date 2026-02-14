import customtkinter as ctk
from .colors.colors import BACKGROUND

from UI.frames.geminiHolder import GeminiHolder
from UI.frames.leftFrame import leftFrame
from UI.frames.sideBar import sideBar
from UI.frames.textDisplay import menuBiblia

def frame_principal(app):
    frame = ctk.CTkFrame(app, fg_color=BACKGROUND)
    frame.pack(fill="both", expand=True)

    GeminiHolder(frame)
    leftFrame(frame)
    sideBar(frame)
    menuBiblia(frame)