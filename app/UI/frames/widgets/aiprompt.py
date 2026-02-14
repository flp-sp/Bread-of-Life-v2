import customtkinter as ctk
from google import genai
from google.genai import types
from dotenv import load_dotenv
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
    inFrame = ctk.CTkFrame(app)
    inFrame.pack(side='left',expand=True, fill='x')

    inLabel = ctk.CTkLabel(inFrame, text="Pergunte a IA:")
    inLabel.pack()
    inText = ctk.CTkTextbox(inFrame)
    inText.pack(fill='x',expand=True)
    inButton = ctk.CTkButton(inFrame, text='>',command=lambda: callGemini(inText.get('1.0','end')))
    inButton.pack(side='right')

def outputFrame(app):
    outFrame = ctk.CTkFrame(app)
    outFrame.pack(side='left',expand=True, fill='both')
    
    global outText
    outText = ctk.CTkTextbox(outFrame)
    outText.pack(fill='both',expand=True)