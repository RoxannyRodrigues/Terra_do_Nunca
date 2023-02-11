import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '7289',
    database = 'biblioteca'
)

cursor = conexao.cursor()
print("Conectado")



print("Bem-Vindo")

def menuLivros ():

    print(f'''
    Selecione o que deseja fazer:
    1. Consultar Todos os Livros
    2. Consultar por ID do Livro
    0. Voltar Menu Principal''')

    escolha = (input("Digite: "))
    match escolha:
        case "1":
            lista_livros = f' SELECT * FROM livros'
            cursor.execute(lista_livros)
            resultado = cursor.fetchall()
            cursor.close()
            conexao.close()

            for liv in resultado:
                print(f' ID: {liv[0]} - Nome: {liv[1]} - Autor: {liv[2]} - Categoria: {liv[3]} \n')

        case "2":
            idlivroescolhido = input("Digite o ID: ")
            sqlid = f'''SELECT * FROM livros
                        WHERE id = {idlivroescolhido}'''
            cursor.execute(sqlid)            
            resultado = cursor.fetchall()
            cursor.close()
            conexao.close()

            for idliv in resultado:
                print(f'ID: {idliv[0]} - Nome: {idliv[1]} - Autor: {idliv[2]} - Categoria: {idliv[3]} \n')
          





teste = menuLivros()