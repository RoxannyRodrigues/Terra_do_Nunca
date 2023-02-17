import mysql.connector
from biblioteca import *

conexao = mysql.connector.connect(
host = 'localhost',
user = 'root',
password = '7289',
database = 'biblioteca'
)

cursor = conexao.cursor()
print("Conectado")



def menuprincipal():
        
    print(f'''Bem-Vindo
    Escolha:
    1.Consultar 
    2.Cadastros   
    3.Alugueis''')

    escolha = input("Digite: ")
    match escolha:
        case "1":
            print(f'''Escolha:
            1. Consultar Livro
            2. Consultar Cliente''')
            escolha2 = input("Digite: ")
            match escolha2:
                case "1":
                    menuconsultarLivros()


menuprincipal()