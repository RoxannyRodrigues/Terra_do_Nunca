import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '7289',
    database = 'biblioteca'
)

cursor = conexao.cursor()
print("Conectado")



print(f'''Bem-Vindo
Escolha:
1.Consultar
2.Cadastros ou Atualização
3.Alugueis''')



def menuconsultarLivros ():

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
          



def menuconsultarClientes ():

    print(f'''
    Selecione o que deseja fazer:
    1. Buscar Cliente por ID
    2. Buscar Cleinte por CPF
    ''')
    escolha = input("Digite: ")
    match escolha:
        case "1":
            iddocliente = input("Digite o ID: ")
            sqlcliente = f'''SELECT * FROM cliente
                        WHERE ID = {iddocliente} '''
            cursor.execute(sqlcliente)            
            resultadocliente = cursor.fetchall()
            cursor.close()
            conexao.close()

            for client in resultadocliente:
                print(f"ID: {client[0]} - Nome: {client[1]} - CPF: {client[2]} - Limite de Livros: {client[3]} \n")
        
        case "2":
            cpfdocliente = input("Digite o CPF: ")
            sqlcliente = f'''SELECT * FROM cliente
                        WHERE cpf = {cpfdocliente}'''
            cursor.execute(sqlcliente)            
            resultadocpfcliente = cursor.fetchall()
            cursor.close()
            conexao.close()

            for cpfcliente in resultadocpfcliente:
                print(f"ID: {cpfcliente[0]} - Nome: {cpfcliente[1]} - CPF: {cpfcliente[2]} - Limite de Livros: {cpfcliente[3]} \n")



menuconsultarClientes()



             