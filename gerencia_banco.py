import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Variável com o nome da tabela
nome_tabela = 'usuarios'

# Verifica a existência da tabela
cursor.execute(f'select name from sqlite_master where type="table" and name="{nome_tabela}";')
result = cursor.fetchone()

# Se o resultado for None a tabela será criada
if result is None:
    cursor.executescript(f'''
            create table {nome_tabela} (
                id integer primary key autoincrement,
                nome text not null,
                senha text not null
            );
    ''')

# Classe do banco de dados
class DataBase:
    # Verifica se os dados inseridos no cadastro já existem
    def verifica_existencia_dados(self, nome:str, senha:str):
        procurar_dados = cursor.execute(f'select nome, senha from usuarios where nome = "{nome}" and senha = "{senha}";')
        dados = procurar_dados.fetchall()
        
        if (dados == []):
            return False
        
        if (nome == dados[0][0] and senha == dados[0][1]):
            return True
    
    # Verifica se os dados inseridos são iguais a algum dado do banco de dados
    def verifica_coesao_dados(self, nome:str, senha:str):
        if (self.verifica_existencia_dados(nome, senha) == True):
            procurar_dados = cursor.execute(f'select nome, senha from usuarios where nome = "{nome}" and senha = "{senha}";')
            dados = procurar_dados.fetchall()
            
            if (nome == dados[0][0] and senha == dados[0][1]):
                return True
            
            else:
                return False
            
        else:
            return False
        
    # Adiciona os dados no banco de dados a partir da verificação da existencia desses dados
    def add_dados_banco(self, nome:str, senha:str):
        if (self.verifica_existencia_dados(nome, senha) == False):
            cursor.executescript(f'insert into usuarios (nome, senha) values ("{nome}", "{senha}")')
            return True
        
        else:
            return False
        
    # Deleta os dados no banco de dados a partir da verificação da existencia desses dados   
    def deleta_dados_banco(self, nome:str, senha:str):
        if (self.verifica_coesao_dados(nome, senha) == True and self.verifica_existencia_dados(nome, senha) == True):
            cursor.executescript(f'delete from usuarios where nome = "{nome}" and senha = "{senha}";')
            return True
        
        else:
            return False
        
    # Atualiza os dados no banco de dados a partir da verificação da existencia desses dados
    def atualiza_dados_banco(self, nome_atual:str, senha_atual:str, nome_mod:str, senha_mod:str):
        if (self.verifica_coesao_dados(nome_atual, senha_atual) == True and self.verifica_existencia_dados(nome_atual, senha_atual) == True):
            cursor.executescript(f'update usuarios set nome = "{nome_mod}", senha = "{senha_mod}" where nome = "{nome_atual}" and senha = "{senha_atual}"')
            return True
        
        else:
            return False