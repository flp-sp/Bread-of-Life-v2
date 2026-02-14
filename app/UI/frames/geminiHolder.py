import customtkinter as ctk
from .colors.colors import FRAMES
from .widgets.aiprompt import inputFrame, outputFrame

def GeminiHolder(app):
    frame = ctk.CTkFrame(app, fg_color=FRAMES)
    frame.pack(side='bottom', fill='x')

    inputFrame(frame)
    outputFrame(frame)