import customtkinter as ctk
from .colors.colors import FRAMES

def GeminiHolder(app):
    frame = ctk.CTkFrame(app, fg_color=FRAMES)
    frame.pack(side='bottom', fill='x')