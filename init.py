import customtkinter as ctk
from window import app, Window_Cadastro

# Tema e apaência da janela
ctk.set_appearance_mode('Dark')
ctk.set_default_color_theme('dark-blue')

# Instanciamento das classes das informações presentes nas janelas
window_cad = Window_Cadastro()

# Classe da janela
class Window:
    def __init__(self):
        app.geometry("400x500")
        app.resizable(False, False)
        
        self.title = window_cad.title
        app.title(self.title)
        
        window_cad.criar_todos_elementos()
        window_cad.exibir_todos_elementos()
    
    def run(self):
        app.mainloop()
        
window = Window()

window.run()