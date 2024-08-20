import customtkinter as ctk
import gerencia_banco

# Criação da janela
global app
app = ctk.CTk()

# Classe da tela de cadastro com as informações da tela (título, elementos presentes, etc)
# Pronta e já funciona
class Window_Cadastro:
    def __init__(self):
        # Título da janela
        self.title:str = 'Cadastro'
        
    # Cria os elementos da tela como, Label, Entry e Botões
    def criar_todos_elementos(self):
        self.label_login = ctk.CTkLabel(app, text_color='white', text='Cadastro', font=('TkDefaultFont', 26))
        self.label_bem_vindo = ctk.CTkLabel(app, text_color='white', text='Bem-vindo!', font=('TkDefaultFont', 22))
        
        self.label_dados_existem = ctk.CTkLabel(app, text_color='red', text='Os dados não podem ser adicionados', font=('TkDefaultFont', 16))
        self.label_dados_nao_existem = ctk.CTkLabel(app, text_color='green', text='Os dados foram adicionados', font=('TkDefaultFont', 16))
        self.label_insira_dados = ctk.CTkLabel(app, text_color='red', text='Por favor insira algum dado', font=('TkDefaultFont', 16))

        self.label_nome = ctk.CTkLabel(app, text='Nome', text_color='white', font=('TkDefaultFont', 16), )
        self.entry_nome = ctk.CTkEntry(app, width=200, placeholder_text='Nome', placeholder_text_color='gray')

        self.label_senha = ctk.CTkLabel(app, text='Senha', text_color='white', font=('TkDefaultFont', 16))
        self.entry_senha = ctk.CTkEntry(app, width=200, placeholder_text='Senha', placeholder_text_color='gray')

        self.botao_cadastro = ctk.CTkButton(app, text='Cadastre-se', text_color='white', font=('TkDefaultFont', 16), command=self.press_botao_cad)
        
        self.botao_faca_login = ctk.CTkButton(app, text_color='white', text='Faça seu Login', font=('TkDefaultFont', 12), height=28, width=70, command=self.press_botao_faca_login)
        self.botao_faca_exclusao = ctk.CTkButton(app, text_color='white', text='Exclua seus dados', font=('TkDefaultFont', 12), height=28, width=70, command=self.press_botao_faca_exclusao)
        self.botao_faca_atualizacao = ctk.CTkButton(app, text_color='white', text='Atualize dados', font=('TkDefaultFont', 12), height=28, width=70, command=self.press_botao_faca_atualizacao)

    # Exibe os elementos da tela
    def exibir_todos_elementos(self):
        self.label_login.pack(side='top', pady=20)
        self.label_bem_vindo.pack(side='top', pady=20)
        
        self.label_nome.place(x=100, y=180)
        self.entry_nome.place(x=100, y=210)
        
        self.label_senha.place(x=100, y=270)
        self.entry_senha.place(x=100, y=300)
        
        self.botao_cadastro.place(x=130, y=375)
        self.botao_cadastro.configure(cursor='hand2')
        
        self.botao_faca_login.place(x=40, y=430)
        self.botao_faca_login.configure(cursor='hand2')
        
        self.botao_faca_exclusao.place(x=145, y=430)
        self.botao_faca_exclusao.configure(cursor='hand2')
        
        self.botao_faca_atualizacao.place(x=270, y=430)
        self.botao_faca_atualizacao.configure(cursor='hand2')
    
    # Remove todos os elementos da tela
    def remover_todos_elementos(self):
        self.label_login.pack_forget()
        self.label_bem_vindo.pack_forget()
        
        self.label_nome.place_forget()
        self.entry_nome.place_forget()
        
        self.label_senha.place_forget()
        self.entry_senha.place_forget()
        
        self.botao_cadastro.place_forget()
        
        self.botao_faca_login.place_forget()
        self.botao_faca_exclusao.place_forget()
        self.botao_faca_atualizacao.place_forget()
        
        self.label_dados_existem.place_forget()
        self.label_dados_nao_existem.place_forget()
        self.label_insira_dados.place_forget()
    
    # Função que salva os dados no banco de dados SQLite e realiza o cadastro
    def press_botao_cad(self):
        geren_banco = gerencia_banco.DataBase()
        if self.entry_nome.get() == '' and self.entry_senha.get() == '':
            self.label_dados_existem.place_forget()
            self.label_dados_nao_existem.place_forget()
            self.label_insira_dados.place(x=100, y=150)
            
        else:
            self.label_insira_dados.place_forget()
            
            if geren_banco.add_dados_banco(self.entry_nome.get(), self.entry_senha.get()) == True:
                self.label_dados_existem.place_forget()
                self.label_dados_nao_existem.place(x=100, y=150)
                
            else:
                self.label_dados_nao_existem.place_forget()
                self.label_dados_existem.place(x=80, y=150)
    
    # Função que direciona a pessoa para a janela de login
    def press_botao_faca_login(self):
        window_login = Window_Login()
        
        app.title(window_login.title)
        self.remover_todos_elementos()
        window_login.criar_todos_elementos()
        return window_login.exibir_todos_elementos()

    # Função que direciona a pessoa para a janela de exclusão
    def press_botao_faca_exclusao(self):
        window_exclusao = Window_Delete_Dados()
        
        app.title(window_exclusao.title)
        self.remover_todos_elementos()
        window_exclusao.criar_todos_elementos()
        return window_exclusao.exibir_todos_elementos()
    
    # Função que direciona a pessoa para a janela de atualização de dados
    def press_botao_faca_atualizacao(self):
        window_atualiza = Window_Atualiza_Dados()
        
        app.title(window_atualiza.title)
        self.remover_todos_elementos()
        window_atualiza.criar_todos_elementos()
        return window_atualiza.exibir_todos_elementos()

# Classe da tela de login com as informações da tela (título, elementos presentes, etc)
# Pronta e já funciona
class Window_Login:
    def __init__(self):
        # Título da janela
        self.title:str = 'Login'
        
    # Cria os elementos da tela, como, Label, Entry e Botões
    def criar_todos_elementos(self):
        self.label_login = ctk.CTkLabel(app, text_color='white', text='Login', font=('TkDefaultFont', 26))
        self.label_bem_vindo = ctk.CTkLabel(app, text_color='white', text='Bem-vindo de volta!', font=('TkDefaultFont', 22))
        
        self.label_incoerencia_dados = ctk.CTkLabel(app, text_color='red', text='Os dados não existem ou não foram encontrados', font=('TkDefaultFont', 16))
        self.label_coerencia_dados = ctk.CTkLabel(app, text_color='green', text='Os dados existem e foram encontrados', font=('TkDefaultFont', 16))
        self.label_insira_dados = ctk.CTkLabel(app, text_color='red', text='Por favor insira algum dado', font=('TkDefaultFont', 16))
        
        self.label_nome = ctk.CTkLabel(app, text='Nome', text_color='white', font=('TkDefaultFont', 16), )
        self.entry_nome = ctk.CTkEntry(app, width=200, placeholder_text='Nome', placeholder_text_color='gray')
        
        self.label_senha = ctk.CTkLabel(app, text='Senha', text_color='white', font=('TkDefaultFont', 16))
        self.entry_senha = ctk.CTkEntry(app, width=200, placeholder_text='Senha', placeholder_text_color='gray')
        
        self.botao_login = ctk.CTkButton(app, text='Login', text_color='white', font=('TkDefaultFont', 16), command=self.press_botao_log)
        
        self.botao_faca_cadastro = ctk.CTkButton(app, text_color='white', text='Cadastre-se', font=('TkDefaultFont', 12), height=28, width=70, command=self.press_botao_faca_cadastro)
        self.botao_faca_exclusao = ctk.CTkButton(app, text_color='white', text='Exclua seus dados', font=('TkDefaultFont', 12), height=28, width=70, command=self.press_botao_faca_exclusao)
        self.botao_faca_atualizacao = ctk.CTkButton(app, text_color='white', text='Atualize dados', font=('TkDefaultFont', 12), height=28, width=70, command=self.press_botao_faca_atualizacao)
    
    # Exibe os elementos da tela
    def exibir_todos_elementos(self):
        self.label_login.pack(side='top', pady=20)
        self.label_bem_vindo.pack(side='top', pady=20)
        
        self.label_nome.place(x=100, y=180)
        self.entry_nome.place(x=100, y=210)
        
        self.label_senha.place(x=100, y=270)
        self.entry_senha.place(x=100, y=300)
        
        self.botao_login.place(x=130, y=375)
        self.botao_login.configure(cursor='hand2')
        
        self.botao_faca_cadastro.place(x=40, y=430)
        self.botao_faca_cadastro.configure(cursor='hand2')
        
        self.botao_faca_exclusao.place(x=135, y=430)
        self.botao_faca_exclusao.configure(cursor='hand2')
        
        self.botao_faca_atualizacao.place(x=260, y=430)
        self.botao_faca_atualizacao.configure(cursor='hand2')
    
    # Remove todos os elementos da tela
    def remover_todos_elementos(self):
        self.label_login.pack_forget()
        self.label_bem_vindo.pack_forget()
        
        self.label_nome.place_forget()
        self.entry_nome.place_forget()
        
        self.label_senha.place_forget()
        self.entry_senha.place_forget()
        
        self.botao_login.place_forget()
        
        self.botao_faca_cadastro.place_forget()
        self.botao_faca_exclusao.place_forget()
        self.botao_faca_atualizacao.place_forget()
        
        self.label_coerencia_dados.place_forget()
        self.label_incoerencia_dados.place_forget()
        self.label_insira_dados.place_forget()
    
    # Verifica se os dados obtidos estão no banco e, se sim, se são coerentes
    def press_botao_log(self):
        geren_banco = gerencia_banco.DataBase()
        if self.entry_nome.get() == '' and self.entry_senha.get() == '':
            self.label_incoerencia_dados.place_forget()
            self.label_coerencia_dados.place_forget()
            self.label_insira_dados.place(x=100, y=150)
        
        else:
            self.label_insira_dados.place_forget()
            
            if geren_banco.verifica_coesao_dados(self.entry_nome.get(), self.entry_senha.get()) == True:
                self.label_insira_dados.place_forget()
                self.label_incoerencia_dados.place_forget()
                self.label_coerencia_dados.place(x=80, y=150)
        
            else:
                self.label_insira_dados.place_forget()
                self.label_coerencia_dados.place_forget()
                self.label_incoerencia_dados.place(x=60, y=150)
    
    # Função que direciona a pessoa para a janela de cadastro
    def press_botao_faca_cadastro(self):
        window_cadastro = Window_Cadastro()
        
        app.title(window_cadastro.title)
        self.remover_todos_elementos()
        window_cadastro.criar_todos_elementos()
        return window_cadastro.exibir_todos_elementos()
    
    # Função que direciona a pessoa para a janela de exclusão
    def press_botao_faca_exclusao(self):
        window_exclusao = Window_Delete_Dados()
        
        app.title(window_exclusao.title)
        self.remover_todos_elementos()
        window_exclusao.criar_todos_elementos()
        return window_exclusao.exibir_todos_elementos()

    def press_botao_faca_atualizacao(self):
        window_atualiza = Window_Atualiza_Dados()
        
        app.title(window_atualiza.title)
        self.remover_todos_elementos()
        window_atualiza.criar_todos_elementos()
        return window_atualiza.exibir_todos_elementos()

# Classe da tela de exclusão com as informações da tela (título, elementos presentes, etc)
# Pronta e já funciona
class Window_Delete_Dados:
    def __init__(self):
        self.title:str = 'Exclusão'
        
    # Cria os elementos da tela, como, Label, Entry e Botões
    def criar_todos_elementos(self):
        self.label_exclusao = ctk.CTkLabel(app, text_color='white', text='Exclua dados', font=('TkDefaultFont', 26))
        self.label_exclua_dados = ctk.CTkLabel(app, text_color='white', text='Como excluir os dados?\n\nInsira dados já existentes no banco de dados\n e clique no botão "Excluir"', font=('TkDefaultFont', 16))
        
        self.label_incoerencia_dados = ctk.CTkLabel(app, text_color='red', text='Os dados não existem ou não foram encontrados', font=('TkDefaultFont', 16))
        self.label_coerencia_dados = ctk.CTkLabel(app, text_color='green', text='Os dados existem e foram excluídos', font=('TkDefaultFont', 16))
        self.label_insira_dados = ctk.CTkLabel(app, text_color='red', text='Por favor insira algum dado', font=('TkDefaultFont', 16))
        
        self.label_nome = ctk.CTkLabel(app, text='Nome', text_color='white', font=('TkDefaultFont', 16), )
        self.entry_nome = ctk.CTkEntry(app, width=200, placeholder_text='Nome', placeholder_text_color='gray')
        
        self.label_senha = ctk.CTkLabel(app, text='Senha', text_color='white', font=('TkDefaultFont', 16))
        self.entry_senha = ctk.CTkEntry(app, width=200, placeholder_text='Senha', placeholder_text_color='gray')
        
        self.botao_excluir = ctk.CTkButton(app, text='Excluir', text_color='white', font=('TkDefaultFont', 16), command=self.press_botao_del)
        
        self.botao_faca_cadastro = ctk.CTkButton(app, text_color='white', text='Cadastre-se', font=('TkDefaultFont', 12), height=28, width=70, command=self.press_botao_faca_cadastro)
        
        self.botao_faca_login = ctk.CTkButton(app, text_color='white', text='Faça seu Login', font=('TkDefaultFont', 12), height=28, width=70, command=self.press_botao_faca_login)
        
        self.botao_faca_atualizacao = ctk.CTkButton(app, text_color='white', text='Atualize dados', font=('TkDefaultFont', 12), height=28, width=70, command=self.press_botao_faca_atualizacao)
    
    # Exibe os elementos da tela
    def exibir_todos_elementos(self):
        self.label_exclusao.pack(side='top', pady=20)
        self.label_exclua_dados.pack(side='top', pady=0)
        
        self.label_nome.place(x=100, y=180)
        self.entry_nome.place(x=100, y=210)
        
        self.label_senha.place(x=100, y=270)
        self.entry_senha.place(x=100, y=300)
        
        self.botao_excluir.place(x=130, y=375)
        self.botao_excluir.configure(cursor='hand2')
        
        self.botao_faca_cadastro.place(x=60, y=430)
        self.botao_faca_cadastro.configure(cursor='hand2')
        
        self.botao_faca_login.place(x=153, y=430)
        self.botao_faca_login.configure(cursor='hand2')
        
        self.botao_faca_atualizacao.place(x=260, y=430)
        self.botao_faca_atualizacao.configure(cursor='hand2')
    
    # Remove todos os elementos da tela
    def remover_todos_elementos(self):
        self.label_exclusao.pack_forget()
        self.label_exclua_dados.pack_forget()
        
        self.label_nome.place_forget()
        self.entry_nome.place_forget()
        
        self.label_senha.place_forget()
        self.entry_senha.place_forget()
        
        self.botao_excluir.place_forget()
        
        self.botao_faca_cadastro.place_forget()
        self.botao_faca_login.place_forget()
        self.botao_faca_atualizacao.place_forget()
        
        self.label_coerencia_dados.place_forget()
        self.label_incoerencia_dados.place_forget()
        self.label_insira_dados.place_forget()
    
    # Verifica se os dados obtidos estão no banco e, se sim, se são coerentes e assim os exclui
    def press_botao_del(self):
        geren_banco = gerencia_banco.DataBase()
        if self.entry_nome.get() == '' and self.entry_senha.get() == '':
            self.label_incoerencia_dados.place_forget()
            self.label_coerencia_dados.place_forget()
            self.label_insira_dados.place(x=100, y=150)
        
        else:
            self.label_insira_dados.place_forget()
        
            if (geren_banco.deleta_dados_banco(self.entry_nome.get(), self.entry_senha.get()) == True):
                self.label_insira_dados.place_forget()
                self.label_incoerencia_dados.place_forget()
                self.label_coerencia_dados.place(x=80, y=150)
        
            else:
                self.label_insira_dados.place_forget()
                self.label_coerencia_dados.place_forget()
                self.label_incoerencia_dados.place(x=40, y=150)
    
    # Função que direciona a pessoa para a janela de cadastro
    def press_botao_faca_cadastro(self):
        window_cadastro = Window_Cadastro()
        
        app.title(window_cadastro.title)
        self.remover_todos_elementos()
        window_cadastro.criar_todos_elementos()
        return window_cadastro.exibir_todos_elementos()
    
    # Função que direciona a pessoa para a janela de login
    def press_botao_faca_login(self):
        window_login = Window_Login()
        
        app.title(window_login.title)
        self.remover_todos_elementos()
        window_login.criar_todos_elementos()
        return window_login.exibir_todos_elementos()
    
    # Função que direciona a pessoa para a janela de atualização de dados
    def press_botao_faca_atualizacao(self):
        window_atualiza = Window_Atualiza_Dados()
        
        app.title(window_atualiza.title)
        self.remover_todos_elementos()
        window_atualiza.criar_todos_elementos()
        return window_atualiza.exibir_todos_elementos()

# Classe da tela de atualização com as informações da tela (título, elementos presentes, etc)
# Falta muita coisa
class Window_Atualiza_Dados:
    def __init__(self):
        self.title:str = 'Atualização e Modificação'
        
    # Cria os elementos da tela, como, Label, Entry e Botões
    def criar_todos_elementos(self):
        self.label_atualizacao = ctk.CTkLabel(app, text_color='white', text='Como atualizar os dados já inseridos?', font=('TkDefaultFont', 18))
        self.label_explicacao = ctk.CTkLabel(app, text_color='white', text='Insira os dados atuais e, após isso,\ninsira os dados que deverão ser colocados no lugar', font=('TkDefaultFont', 16))
        
        self.label_incoerencia_dados = ctk.CTkLabel(app, text_color='red', text='Os dados não existem ou não foram encontrados', font=('TkDefaultFont', 16))
        self.label_coerencia_dados = ctk.CTkLabel(app, text_color='green', text='Os dados existem e foram atualizados', font=('TkDefaultFont', 16))
        self.label_insira_dados = ctk.CTkLabel(app, text_color='red', text='Por favor insira algum dado', font=('TkDefaultFont', 16))
        
        self.label_nome_atual = ctk.CTkLabel(app, text='Nome atual', text_color='white', font=('TkDefaultFont', 16), )
        self.entry_nome_atual = ctk.CTkEntry(app, width=170, placeholder_text='Nome atual', placeholder_text_color='gray')
        
        self.label_senha_atual = ctk.CTkLabel(app, text='Senha atual', text_color='white', font=('TkDefaultFont', 16))
        self.entry_senha_atual = ctk.CTkEntry(app, width=170, placeholder_text='Senha atual', placeholder_text_color='gray')
        
        self.label_nome_modificado = ctk.CTkLabel(app, text='Nome modificado', text_color='white', font=('TkDefaultFont', 16), )
        self.entry_nome_modificado = ctk.CTkEntry(app, width=170, placeholder_text='Nome modificado', placeholder_text_color='gray')
        
        self.label_senha_modificado = ctk.CTkLabel(app, text='Senha modificada', text_color='white', font=('TkDefaultFont', 16))
        self.entry_senha_modificada = ctk.CTkEntry(app, width=170, placeholder_text='Senha modificada', placeholder_text_color='gray')
        
        self.botao_atualizar = ctk.CTkButton(app, text='Atualizar', text_color='white', font=('TkDefaultFont', 16), command=self.press_botao_atual)
        
        self.botao_faca_cadastro = ctk.CTkButton(app, text_color='white', text='Cadastre-se', font=('TkDefaultFont', 12), height=28, width=70, command=self.press_botao_faca_cadastro)
    
        self.botao_faca_login = ctk.CTkButton(app, text_color='white', text='Faça seu Login', font=('TkDefaultFont', 12), height=28, width=70, command=self.press_botao_faca_login)
        
        self.botao_faca_exclusao = ctk.CTkButton(app, text_color='white', text='Exclua seus dados', font=('TkDefaultFont', 12), height=28, width=70, command=self.press_botao_faca_exclusao)
    
    # Exibe os elementos da tela
    def exibir_todos_elementos(self):
        self.label_atualizacao.pack(side='top', pady=20)
        self.label_explicacao.pack(side='top', pady=0)
        
        self.label_nome_atual.place(x=20, y=180)
        self.entry_nome_atual.place(x=20, y=210)
        
        self.label_senha_atual.place(x=20, y=270)
        self.entry_senha_atual.place(x=20, y=300)
        
        self.label_nome_modificado.place(x=210, y=180)
        self.entry_nome_modificado.place(x=210, y=210)
        
        self.label_senha_modificado.place(x=210, y=270)
        self.entry_senha_modificada.place(x=210, y=300)
        
        self.botao_atualizar.place(x=130, y=375)
        self.botao_atualizar.configure(cursor='hand2')
        
        self.botao_faca_cadastro.place(x=60, y=430)
        self.botao_faca_cadastro.configure(cursor='hand2')
        
        self.botao_faca_login.place(x=153, y=430)
        self.botao_faca_login.configure(cursor='hand2')
        
        self.botao_faca_exclusao.place(x=260, y=430)
        self.botao_faca_exclusao.configure(cursor='hand2')
    
    # Remove todos os elementos da tela
    def remover_todos_elementos(self):
        self.label_atualizacao.pack_forget()
        self.label_explicacao.pack_forget()
        
        self.label_nome_atual.place_forget()
        self.entry_nome_atual.place_forget()
        
        self.label_senha_atual.place_forget()
        self.entry_senha_atual.place_forget()
        
        self.label_nome_modificado.place_forget()
        self.entry_nome_modificado.place_forget()
        
        self.label_senha_modificado.place_forget()
        self.entry_senha_modificada.place_forget()
        
        self.botao_atualizar.place_forget()
        
        self.botao_faca_cadastro.place_forget()
        self.botao_faca_login.place_forget()
        self.botao_faca_exclusao.place_forget()
        
        self.label_coerencia_dados.place_forget()
        self.label_incoerencia_dados.place_forget()
        self.label_insira_dados.place_forget()
    
    # Verifica se os dados obtidos estão no banco e, se sim, se são coerentes para atualizá-los
    def press_botao_atual(self):
        geren_banco = gerencia_banco.DataBase()
        if self.entry_nome_atual.get() == '' and self.entry_senha_atual.get() == '' and self.entry_nome_modificado.get() == '' and self.entry_senha_modificada.get() == '':
            self.label_incoerencia_dados.place_forget()
            self.label_coerencia_dados.place_forget()
            self.label_insira_dados.place(x=100, y=150)
        
        else:
            self.label_insira_dados.place_forget()

            if (geren_banco.atualiza_dados_banco(self.entry_nome_atual.get(), self.entry_senha_atual.get(), self.entry_nome_modificado.get(), self.entry_senha_modificada.get()) == True):
                self.label_insira_dados.place_forget()
                self.label_incoerencia_dados.place_forget()
                self.label_coerencia_dados.place(x=80, y=150)
        
            else:
                self.label_insira_dados.place_forget()
                self.label_coerencia_dados.place_forget()
                self.label_incoerencia_dados.place(x=40, y=150)
    
    # Função que direciona a pessoa para a janela de cadastro
    def press_botao_faca_cadastro(self):
        window_cadastro = Window_Cadastro()
        
        app.title(window_cadastro.title)
        self.remover_todos_elementos()
        window_cadastro.criar_todos_elementos()
        return window_cadastro.exibir_todos_elementos()
    
    # Função que direciona a pessoa para a janela de login
    def press_botao_faca_login(self):
        window_login = Window_Login()
        
        app.title(window_login.title)
        self.remover_todos_elementos()
        window_login.criar_todos_elementos()
        return window_login.exibir_todos_elementos()
    
    # Função que direciona a pessoa para a janela de exclusão
    def press_botao_faca_exclusao(self):
        window_exclusao = Window_Delete_Dados()
        
        app.title(window_exclusao.title)
        self.remover_todos_elementos()
        window_exclusao.criar_todos_elementos()
        return window_exclusao.exibir_todos_elementos()