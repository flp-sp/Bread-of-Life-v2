import customtkinter as ctk
from google import genai
from google.genai import types
from dotenv import load_dotenv
from ..colors.colors import *
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

global outText

def callGemini(prompt):
    global outText
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(model="gemini-3-flash-preview",
            config=types.GenerateContentConfig(system_instruction="Voce deve saber responder perguntas sobre a biblia de forma honesta e sem associação a nenhuma instituição religiosa, voce vai embasar suas respostas baseados na interpretacao mais plausivel para o dado assunto perguntado. Nao use markdown"), 
                contents=prompt)
    outText.insert('0.0', text=response.text)
    

def inputFrame(app):
    inFrame = ctk.CTkFrame(app,fg_color=BACKGROUND)
    inFrame.pack(side='left',expand=True, fill='x')

    inLabel = ctk.CTkLabel(inFrame, text="Pergunte a IA:")
    inLabel.pack()
    inText = ctk.CTkTextbox(inFrame,fg_color=FRAMES)
    inText.pack(fill='x',expand=True,padx=4,pady=4)
    inButton = ctk.CTkButton(inFrame, text='>',command=lambda: callGemini(inText.get('1.0','end')),fg_color=BUTTON)
    inButton.pack(side='right',padx=4,pady=4)

def outputFrame(app):
    outFrame = ctk.CTkFrame(app,fg_color=BACKGROUND)
    outFrame.pack(side='left',expand=True, fill='both')
    
    global outText
    outText = ctk.CTkTextbox(outFrame,fg_color=FRAMES)
    outText.pack(fill='both',expand=True,padx=4,pady=4)