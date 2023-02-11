import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '7289',
    database = 'biblioteca'
)

cursor = conexao.cursor()
print("Conectado")



"""print(f'''Bem-Vindo
Escolha:
1.Consultar 
2.Cadastros   
3.Alugueis''')"""



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

                #CRIAR O BUSCAR NOME




def menuCadastros():
    print('''Escolha:
    1. Livros
    2. Clientes
    0. Voltar Menu Principal''')
    escolhamenucadastro = input("Digite: ")
    match escolhamenucadastro:
        case "1":
            print('''Escolha:
    1. Novo Cadastro
    2. Atualizar Cadastro
    3. Deletar Cadastro
    4. Voltar Menu Principal''')

                #menu1LIVRO

                #Novocadastro

            escolhanovocadastroLivros = input("Digite: ")
            match escolhanovocadastroLivros:
                case "1":
                    
                    nome_novo_livro = input('Digite nome novo Livro: ')
                    autor_novo_livro = input('Digite nome do autor: ')
                    categoria_novo_livro = input('Digite a categoria: ')

                    sql_inserir_livro = f''' INSERT INTO livros (nome, autor, categoria) VALUES ("{nome_novo_livro}", "{autor_novo_livro}", "{categoria_novo_livro}")'''
                    cursor.execute(sql_inserir_livro)
                    conexao.commit()
                    cursor.close()
                    conexao.close()
                    print("Cadastro Realizado com Sucesso")
                
                #Atualizarcadastro

                case "2":
                    
                    idbuscado = input("Digite id do livro deseja alterar: ")
                    print ('''Qual dado você deseja alterar:
                    1. Nome
                    2. Autor
                    3. Categoria''')
                    escolhadadolivro = input("Digite: ")
                    match escolhadadolivro:
                        case "1":
                            nomenovo = input("Digite sua mudança")
                            sql_atualizar_livro = f'UPDATE livros SET nome = "{nomenovo}" WHERE id = "{idbuscado}"'
                            cursor.execute(sql_atualizar_livro)
                            conexao.commit()
                            cursor.close()
                            conexao.close()
                            print("Atualizado com Sucesso")
                        
                        case "2":
                            nomeautor = input("Digite sua mudança")
                            sql_atualizar_autor = f'UPDATE livros SET autor = "{nomeautor}" WHERE id = "{idbuscado}"'
                            cursor.execute(sql_atualizar_autor)
                            conexao.commit()
                            cursor.close()
                            conexao.close()
                            print("Atualizado com Sucesso")
                        
                        case "3":
                            nomecategoria = input("Digite sua mudança")
                            sql_atualizar_categoria = f'UPDATE livros SET autor = "{nomecategoria}" WHERE id = "{idbuscado}"'
                            cursor.execute(sql_atualizar_categoria)
                            conexao.commit()
                            cursor.close()
                            conexao.close()
                            print("Atualizado com Sucesso")
                
                case "3":
                    dss = "legal"



        case "2":
            print('''Escolha:
            1. Novo Cadastro
            2. Atualizar Cadastro
            3. Deletar Cadastro
            4. Voltar Menu Principal''')




menuCadastros()






