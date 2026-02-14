import customtkinter as ctk 
from UI.frames.mainFrame import frame_principal

float_value = 1.3

ctk.set_widget_scaling(float_value)  # widget dimensions and text size
ctk.set_window_scaling(float_value)  # window geometry dimensions

app = ctk.CTk()
app.geometry("1080x720")
app.title("Bread of Life")

frame_principal(app)

app.mainloop()