import customtkinter as ctk
from tkinter import *

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')

root_tela = ctk.CTk()
root_tela.geometry('700x400')
root_tela.title("Login")
# root_tela.iconbitmap('icon.ico')
root_tela.resizable(False, False)

img = PhotoImage(file='rocket.png')
label_img = ctk.CTkLabel(master=root_tela, image=img)
label_img.place(x=5, y=65)


root_tela.mainloop()
