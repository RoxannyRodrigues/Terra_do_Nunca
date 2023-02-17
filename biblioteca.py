import mysql.connector

conexao = mysql.connector.connect(
host = 'localhost',
user = 'root',
password = '7289',
database = 'biblioteca'
)

cursor = conexao.cursor()
print("Conectado")

def visualizarBanco(sql):
    
    cursor = conexao.cursor()
    cursor.execute(sql)
    resultado = cursor.fetchall()
    for liv in resultado:
        print(f' ID: {liv[0]} - Nome: {liv[1]} - Autor: {liv[2]} - Categoria: {liv[3]} \n')
    cursor.close()
    

def manipularBanco(sql):
    
    cursor = conexao.cursor()
    cursor.execute(sql)
    conexao.commit()
    cursor.close()
    print("Processo realizado com sucesso")



#MENUCONSULTAR

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
            visualizarBanco(lista_livros)

        case "2":
            idlivroescolhido = input("Digite o ID: ")
            sqlid = f'''SELECT * FROM livros
                        WHERE id = {idlivroescolhido}'''
            visualizarBanco(sqlid)
        
        case "0":
            menuprincipal()
        
          

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


#MENUCADASTROS

def menuCadastrosLivro():
    print('''Escolha:
    1. Novo Cadastro
    2. Atualizar Cadastro
    3. Deletar Cadastro
    0. Voltar Menu Principal''')

    #Novocadastro

    escolhanovocadastroLivros = input("Digite: ")
    match escolhanovocadastroLivros:
        case "1": #NOVOCADASTRO
            
            nome_novo_livro = input('Digite nome novo Livro: ')
            autor_novo_livro = input('Digite nome do autor: ')
            categoria_novo_livro = input('Digite a categoria: ')

            sql_inserir_livro = f''' INSERT INTO livros (nome, autor, categoria) VALUES ("{nome_novo_livro}", "{autor_novo_livro}", "{categoria_novo_livro}")'''
            manipularBanco(sql_inserir_livro)
        
        #Atualizarcadastro

        case "2":   #menu Atualizar Cadastro Livro
            
            idbuscado = input("Digite id do livro deseja alterar: ")
            print ('''Qual dado você deseja alterar:
            1. Nome
            2. Autor
            3. Categoria''')
            escolhadadolivro = input("Digite: ")
            match escolhadadolivro:
                case "1": #NOME
                    nomenovo = input("Digite sua mudança")
                    sql_atualizar_livro = f'UPDATE livros SET nome = "{nomenovo}" WHERE id = "{idbuscado}"'
                    manipularBanco(sql_atualizar_livro)

                case "2": #AUTOR
                    nomeautor = input("Digite sua mudança")
                    sql_atualizar_autor = f'UPDATE livros SET autor = "{nomeautor}" WHERE id = "{idbuscado}"'
                    manipularBanco(sql_atualizar_autor)
                
                case "3": #CAATEGORIA
                    nomecategoria = input("Digite sua mudança")
                    sql_atualizar_categoria = f'UPDATE livros SET autor = "{nomecategoria}" WHERE id = "{idbuscado}"'
                    manipularBanco(sql_atualizar_categoria)

        
        case "3": #DELETARLIVRO
            idlivrodeletar = input("Digite ID livro vai ser deletado: ")
            VisualizarLIvrodelete = f'''SELECT nome FROM livros WHERE id = {idlivrodeletar}'''
            visualizarBanco(VisualizarLIvrodelete)


            print (f'''

            Tem certeza que você quer Deletar?
            1. SIM
            2. Não''')

            opcaoescolhida = input("Digite: ")
            match opcaoescolhida:
                case "1":
                    deletarlivro = f'''DELETE FROM livros WHERE id = "{idlivrodeletar}"'''
                    manipularBanco(deletarlivro)
                        


def menuCadastrosClientes():
    print('''Escolha:
    1. Novo Cadastro
    2. Atualizar Cadastro
    3. Deletar Cadastro
    0. Voltar Menu Principal''')

    #Novocadastro

    escolhanovocadastroCliente = input("Digite: ")
    match escolhanovocadastroCliente:
        case "1": #NOVOCADASTRO
            
            nome_novo_cliente = input('Digite nome novo cliente: ')
            cpf_novo_cliente = input('Digite nome do cpf: ')
            limitelivro_novo_cliente = int(input('Digite Limite de Livros: '))

            sql_inserir_cliente = f''' INSERT INTO cliente (nome,cpf, `limite de livros`) VALUES ("{nome_novo_cliente}", "{cpf_novo_cliente}", {limitelivro_novo_cliente})'''
            manipularBanco(sql_inserir_cliente)

        
        case "2":   #menu Atualizar 
            
            idbuscado = input("Digite id do cliente deseja alterar: ")
            print ('''Qual dado você deseja alterar:
            1. Nome
            2. Cpf
            3. Limite de Livros
            ''')
            escolhadocliente = input("Digite: ")
            match escolhadocliente:
                case "1": #NOME
                    nomenovo = input("Digite sua mudança: ")
                    sql_atualizar_nome = f'UPDATE cliente SET nome = "{nomenovo}" WHERE id = "{idbuscado}"'
                    manipularBanco(sql_atualizar_nome)
                
                case "2": #AUTOR
                    cpfnovo = input("Digite sua mudança")
                    sql_atualizar_cpf = f'UPDATE cliente SET cpf = "{cpfnovo}" WHERE id = "{idbuscado}"'
                    manipularBanco(sql_atualizar_cpf)
                
                case "3": #CATEGORIA
                    novolimite = input("Digite sua mudança")
                    sql_atualizar_limite = f'UPDATE cliente SET `limite de livros` = "{novolimite}" WHERE id = "{idbuscado}"'
                    manipularBanco(sql_atualizar_limite)
        
        case "3": #DELETARLIVRO
            idlivrodeletar = input("Digite ID livro vai ser deletado: ")
            VisualizarLIvrodelete = f'''SELECT nome FROM livros WHERE id = {idlivrodeletar}'''
            visualizarBanco(VisualizarLIvrodelete)

            print (f'''

            Tem certeza que você quer Deletar?
            1. SIM
            2. Não''')

            opcaoescolhida = input("Digite: ")
            match opcaoescolhida:
                case "1":
                    deletarlivro = f'''DELETE FROM livros WHERE id = "{idlivrodeletar}"'''
                    manipularBanco(deletarlivro)
                        
#---------------------------------------------------   
#---------------------------------------------------         

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
    1. Consultar Livros
    2. Consultar Clientes
    0. Voltar''')
            escolha2 = input("Digite: ")
            match escolha2:
                case "1":
                    menuconsultarLivros()
                case "2":
                    menuconsultarClientes()
                case "0":
                    menuprincipal()


menuprincipal()
                  
               
