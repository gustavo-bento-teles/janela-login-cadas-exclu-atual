# Janela de login, cadastro, atualização e exclusão

## Índice

- [Descrição](#descrição)
- [Estrutura de arquivos](#estrutura-de-arquivos)
- [Uso](#uso)
- [Banco de dados](#banco-de-dados)
- [Contribuição](#contribuição)

## Descrição

O projeto é uma **tela de cadastro** que dentro dela há uma tela de **login, de atualização e exclusão** usando **SQLite como banco de dados relacional e Python como a linguagem de programação principal.**

**O projeto já está completo e foi todo feito com a biblioteca customtkinter**, além de que já está implementada todas as funcionalidades que previamente eu desejava colocar.

#### Bibliotecas usadas:

1. sqlite3
2. customtkinter

## Estrutura de arquivos

> Dentro do projeto existem 3 arquivos (gerencia_banco.py, init.py e window.py).

 ### Arquivo "init.py"
 
É o arquivo base que inicia toda a janela com as informações como a geometria da janela, tema, aparência e se é redimensionável.

> **Ela inicia pela janela de cadastro.**

---

### Arquivo "gerencia_banco.py"

É o arquivo que **contém a lógica de gerenciamento do banco de dados**, tanto para cadastrar dados, verificar a existência de dados, verificar a coerência de dados, etc.

> Foi utilizado a biblioteca "sqlite3" para o gerenciamento do banco de dados SQLite.
---
### Arquivo "window.py"

É o arquivo responsável por conter todas as informações de cada janela, como título, as informações da tela, etc.

Dentro dele existem 4 classes:
1. Window_Cadastro
2. Window_Login
3. Window_Delete_Dados
4. Window_Atualiza_Dados

> Cada janela tem sua própria classe contendo suas informações.

##  Uso

### Requisitos
1. Versão atualizada do Python (Python 3.8+);
2. Ter as [bibliotecas necessárias](#bibliotecas-usadas) para o projetos instaladas.

A biblioteca **sqlite3 não necessita ser instalada**, mas **a customtkinter necessita.**

Caso não tenha a customtkinter instalada siga a seguir:

1. Escreva o seguinte código no seu terminal:

```bash
pip install customtkinter
```
---
### Utilização prática

Para iniciar o projeto se deve rodar o arquivo [init.py](#arquivo-init.py).

Então vá até a pasta onde estão os arquivos do projeto e rode o seguinte código:

Para Windows:
```bash
python .\init.py
```

Para Linux e MacOS:
```bash
python3 .\init.py
```
---
> O arquivo init.py irá procurar pelo arquivo window.py e o arquivo window.py irá procura pelo arquivo gerencia_banco.py, então lembre-se de mantê-los todos na mesma pasta.

## Banco de Dados

O nome do arquivo do banco de dados é **"database.db"**.

O banco de dados SQLite do projeto é composto por 3 colunas com seus respectivos tipos de dados aceitos:

| id | nome | senha |
|----|------|-------|
| int | varchar | varchar |

*A chave primária (primary key) é a coluna "id".*

> Caso a tabela não exista ao iniciar o código, ela automaticamente será criada, caso já exista e tenha dados (ou não), os dados se manterão.

## Contribuição

Caso queira modificar ou ter uso próprio do projeto pode ficar à vontade, **para mais informações do que é permitido ou não, recomendo que leia o arquivo "LICENSE.md"** que está presente neste mesmo repositório.

*Este projeto está licenciado sob a Licença MIT.*
