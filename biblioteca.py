import mysql.connector


conexao = mysql.connector.connect(
host = 'localhost',
user = 'root',
password = '7289',
database = 'biblioteca'
)

cursor = conexao.cursor()
print("Conectado")

#--------------------------------
# FUNÇÕES VISUALIAR E MANIPULAR
#--------------------------------

def visualizarBanco(sql):
    
    cursor = conexao.cursor()
    cursor.execute(sql)
    resultado = cursor.fetchall()
    cursor.close()
    return resultado
    

def manipularBanco(sql):
    
    cursor = conexao.cursor()
    cursor.execute(sql)
    conexao.commit()
    cursor.close()
    print("Processo realizado com sucesso")


#--------------------------------
# MENUS SECUNDÁRIOS
#--------------------------------

#-----------MENU CONSULTAR LIVROS---_-----#
def menuvoltar():
    print(f'''Que deseja fazer agora?
    1. Voltar
    2. Volta Menu Principal''')
    escolhafinal = input("Digite: ")
    match escolhafinal:
        case "1":
            print("")
        case "2":
            menuprincipal()
        case _:
            print("Opção Inválida")
                

def menuconsultarLivros ():         #falta validar str

    #escolha = "0"
    
    while True:
        print(f'''
    Selecione o que deseja fazer:
    1. Consultar Todos os Livros
    2. Consultar por ID do Livro
    0. Voltar Menu Principal''')


        escolha = (input("Digite: "))
        match escolha:
            case "1":
                lista_livros = f' SELECT * FROM livros'
                resultado = visualizarBanco(lista_livros)
                for liv in resultado:
                    print(f' ID: {liv[0]} - Nome: {liv[1]} - Autor: {liv[2]} - Categoria: {liv[3]} \n')

                menuvoltar()

            case "2":  #CONSULTA POR ID
                while True:
                    idlivroescolhido = input('Digite o ID: ')
                    try:
                        idlivroescolhido = int(idlivroescolhido)
                        sqlid = f'''SELECT * FROM livros
                                    WHERE id = {idlivroescolhido}'''
                        resultadoid = visualizarBanco(sqlid)
                        if resultadoid == []:
                            print ("ID não Existe")
                        else:
                            for liv in resultadoid:
                                print(f' ID: {liv[0]} - Nome: {liv[1]} - Autor: {liv[2]} - Categoria: {liv[3]} \n')
                                menuvoltar()
                            break
                    except ValueError:
                        print("Digite um ID Válido")    
               

                 
                         
            case "0":
                menuprincipal()
            
            #verificar com tarik
            case _:
                print (f'Digite uma opção válida!')
                                   

#-----------MENU CONSULTAR CLIENTE--------#          

def menuconsultarClientes ():

    while True:
        print(f'''
        Selecione o que deseja fazer:
        1. Buscar Cliente por ID
        2. Buscar Cliente por CPF
        3. Consultar Aluguel de Cliente
        0. Voltar Menu Principal
        ''')
        escolha = input("Digite: ")

        match escolha:
            case "1":
                iddocliente = input("Digite o ID: ")
                sqlcliente = f'''SELECT * FROM cliente
                            WHERE id = {iddocliente} '''
                resultadoidcliente = visualizarBanco(sqlcliente)
                for liv in resultadoidcliente:
                    print(f' ID: {liv[0]} - Nome: {liv[1]} - Cpf: {liv[2]} - Limite de Livros: {liv[3]} \n')

                print(f'''Que deseja fazer agora?
        1. Voltar
        2. Volta Menu Principal''')
                escolhafinal = input("Digite: ")
                match escolhafinal:
                    case "1":
                            print("")
                    case "2":
                        menuprincipal()
                        break

            
            case "2":
                cpfdocliente = input("Digite o CPF: ")
                sqlcliente = f'''SELECT * FROM cliente
                            WHERE cpf = {cpfdocliente}'''
                resultadocpfcliente = visualizarBanco(sqlcliente)
                for liv in resultadocpfcliente:
                    print(f' ID: {liv[0]} - Nome: {liv[1]} - Cpf: {liv[2]} - Limite de Livros: {liv[3]} \n')

                print(f'''Que deseja fazer agora?
        1. Voltar
        2. Volta Menu Principal''')
                escolhafinal = input("Digite: ")
                match escolhafinal:
                    case "1":
                            print("")
                    case "2":
                        menuprincipal()
                        break
            
            case "3":
                id_cliente_consulta = input("Digite o ID do cliente: ")
                sql_consulta_aluguel = f'''SELECT * FROM aluguel
                                           WHERE `id cliente` = {id_cliente_consulta} '''
                resultadoidaluguel = visualizarBanco(sql_consulta_aluguel)
                for liv in resultadoidaluguel: 
                    (f' ID: {liv[0]} - Data Aluguel: {liv[1]} - ID cliente: {liv[2]} - ID livro: {liv[3]} \n')


                sql_consulta_livro_alugado = f'''SELECT nome FROM livros WHERE id = {liv[3]}'''
                resultadoidlivro = visualizarBanco(sql_consulta_livro_alugado)
              
                for Alug2 in resultadoidlivro:
                    print (f' Livro: {Alug2[0]} ')

            
            case "0":
                menuprincipal()
            
            case _:
                print("Digite opção válida!")


                    #CRIAR O BUSCAR NOME

#-----------MENU CONSULTAR Aluguel--------#         

def menuconsultarAluguel ():
    escolhanovoAluguel = input("Digite: ")
    match escolhanovoAluguel:

        case "1":
            iddoaluguel = input("Digite o ID do aluguel: ")
            sqldealuguel = f'''SELECT * FROM aluguel
                            WHERE id = {iddoaluguel} '''
            resultadoidaluguel = visualizarBanco(sqldealuguel)
            for liv in resultadoidaluguel: 
                (f' ID: {liv[0]} - Data Aluguel: {liv[1]} - ID cliente: {liv[2]} - ID livro: {liv[3]} \n')


            sqlclientealugado = f'''SELECT * FROM cliente WHERE id = {liv[2]}'''
            resultadoidcliente = visualizarBanco(sqlclientealugado)


            sqllivroAlugado = f'''SELECT nome FROM livros WHERE id = {liv[3]}'''
            resultadoidlivro = visualizarBanco(sqllivroAlugado)

            for Alug in resultadoidcliente:
                print(f' ID: {Alug[0]} - Nome: {Alug[1]} - CPF: {Alug[2]} \n')
            
            for Alug2 in resultadoidlivro:
                print (f' Livro: {Alug2[0]} ')


#-----------MENU CADASTRAOS LIVROS--------# 

def menuCadastrosLivro():

    while True:
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
                print(f'''Que deseja fazer agora?
    1. Voltar
    2. Volta Menu Principal''')
                escolhafinal = input("Digite: ")
                match escolhafinal:
                    case "1":
                            print("")
                    case "2":
                        menuprincipal()
                        break

            
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
                        nomenovo = input("Digite sua mudança: ")
                        sql_atualizar_livro = f'UPDATE livros SET nome = "{nomenovo}" WHERE id = "{idbuscado}"'
                        manipularBanco(sql_atualizar_livro)
                        print(f'''Que deseja fazer agora?
    1. Voltar
    2. Volta Menu Principal''')
                        escolhafinal = input("Digite: ")
                        match escolhafinal:
                            case "1":
                                    print("")
                            case "2":
                                menuprincipal()
                                break

                    case "2": #AUTOR
                        nomeautor = input("Digite sua mudança: ")
                        sql_atualizar_autor = f'UPDATE livros SET autor = "{nomeautor}" WHERE id = "{idbuscado}"'
                        manipularBanco(sql_atualizar_autor)
                        print(f'''Que deseja fazer agora?
    1. Voltar
    2. Volta Menu Principal''')
                        escolhafinal = input("Digite: ")
                        match escolhafinal:
                            case "1":
                                    print("")
                            case "2":
                                menuprincipal()
                                break
                            
                    case "3": #CAATEGORIA
                        nomecategoria = input("Digite sua mudança: ")
                        sql_atualizar_categoria = f'UPDATE livros SET autor = "{nomecategoria}" WHERE id = "{idbuscado}"'
                        manipularBanco(sql_atualizar_categoria)
                        print(f'''Que deseja fazer agora?
    1. Voltar
    2. Volta Menu Principal''')
                        escolhafinal = input("Digite: ")
                        match escolhafinal:
                            case "1":
                                    print("")
                            case "2":
                                menuprincipal()
                                break

            
            case "3": #DELETARLIVRO
                idlivroescolhido = input("Digite o ID: ")
                sqlid = f'''SELECT * FROM livros
                            WHERE id = {idlivroescolhido}'''
                resultadoid = visualizarBanco(sqlid)
                for liv in resultadoid:
                    print(f' ID: {liv[0]} - Nome: {liv[1]} - Autor: {liv[2]} - Categoria: {liv[3]} \n')


                print (f'''

    Tem certeza que você quer Deletar?
    1. SIM
    2. Não''')

                opcaoescolhida = input("Digite: ")
                match opcaoescolhida:
                    case "1":
                        deletarlivro = f'''DELETE FROM livros WHERE id = "{idlivroescolhido}"'''
                        manipularBanco(deletarlivro)
                        
                        print(f'''Que deseja fazer agora?
    1. Voltar
    2. Volta Menu Principal''')
                        escolhafinal = input("Digite: ")
                        match escolhafinal:
                            case "1":
                                print("")
                            case "2":
                                menuprincipal()
                                break
            case "0":
                menuprincipal()
                                    
#-----------MENU CADASTRAOS CLIENTES--------# 

def menuCadastrosClientes():

    while True:
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
            
            case "3": #DELETARCLIENTE
                iddocliente = input("Digite o ID: ")
                sqlcliente = f'''SELECT * FROM cliente
                                WHERE id = {iddocliente} '''
                resultadoidcliente = visualizarBanco(sqlcliente)
                for liv in resultadoidcliente:
                        print(f' ID: {liv[0]} - Nome: {liv[1]} - Cpf: {liv[2]} - Limite de Livros: {liv[3]} \n')

                print (f'''

    Tem certeza que você quer Deletar?
    1. SIM
    2. Não''')

                opcaoescolhida = input("Digite: ")
                match opcaoescolhida:
                    case "1":
                        deletarcliente = f'''DELETE FROM livros WHERE id = "{iddocliente}"'''
                        manipularBanco(deletarcliente)
                    
                    case "2":
                        print(f'''Que deseja fazer agora?
    1. Voltar
    2. Volta Menu Principal''')
                        escolhafinal = input("Digite: ")
                        match escolhafinal:
                            case "1":
                                print("")
                            case "2":
                                menuprincipal()
                                break
            
            case "0":
                menuprincipal()
                break
                        

#-----------MENU ALUGUEL--------# 


def menualuguel():
    
   while True:
        print(f'''
    1. Consultar Aluguel
    2. Cadastrar Aluguel
    3. Devolução
    0. Voltar Menu Principal


        ''')
        #------------------CONSULTA------------------#
        escolhanovoAluguel = input("Digite: ")
        match escolhanovoAluguel:
    
            case "1":
                iddoaluguel = input("Digite o ID do aluguel: ")
                sqldealuguel = f'''SELECT * FROM aluguel
                                WHERE id = {iddoaluguel} '''
                resultadoidaluguel = visualizarBanco(sqldealuguel)
                for liv in resultadoidaluguel: 
                    (f' ID: {liv[0]} - Data Aluguel: {liv[1]} - ID cliente: {liv[2]} - ID livro: {liv[3]} \n')


                sqlclientealugado = f'''SELECT * FROM cliente WHERE id = {liv[2]}'''
                resultadoidcliente = visualizarBanco(sqlclientealugado)


                sqllivroAlugado = f'''SELECT nome FROM livros WHERE id = {liv[3]}'''
                resultadoidlivro = visualizarBanco(sqllivroAlugado)

                for Alug in resultadoidcliente:
                    print(f' ID: {Alug[0]} - Nome: {Alug[1]} - CPF: {Alug[2]} \n')
                
                for Alug2 in resultadoidlivro:
                    print (f' Livro: {Alug2[0]} ')



            case "2": #NOVOCADASTRO
                
                clientealugando = input('Digite o ID do cliente: ')
                livro_alugado = input('Digite ID do Livro Cadastrado: ')
                dataaluguel = (input('Digite Data do Aluguel: '))

                sql_inserir_aluguel = f''' INSERT INTO aluguel (`data aluguel`,`id cliente`, `id livro`) VALUES ("{dataaluguel}", "{clientealugando}", {livro_alugado})'''
                manipularBanco(sql_inserir_aluguel)


            case "3": #DEVOLUÇÃO
                    iddoaluguel = input("Digite o ID do aluguel: ")
                    sqldealuguel = f'''SELECT * FROM aluguel
                                    WHERE id = {iddoaluguel} '''
                    resultadoidaluguel = visualizarBanco(sqldealuguel)
                    for liv in resultadoidaluguel:
                            print(f' ID: {liv[0]} - Data Aluguel: {liv[1]} - ID cliente: {liv[2]} - ID livro: {liv[3]} \n')

                    print (f'''

    Confira a Devolução?
    1. SIM
    2. Não''')

                    opcaoescolhida = input("Digite: ")
                    match opcaoescolhida:
                        case "1":
                            deletaraluguel = f'''DELETE FROM livros WHERE id = "{iddoaluguel}"'''
                            manipularBanco(deletaraluguel)
                        
                        case "2":
                            print(f'''Que deseja fazer agora?
    1. Voltar
    2. Volta Menu Principal''')
                            escolhafinal = input("Digite: ")
                            match escolhafinal:
                                case "1":
                                    print("")
                                case "2":
                                    menuprincipal()
                                    break


                        
#---------------------------------------------------
# MENU PRINCIPAL    
#---------------------------------------------------         

def menuprincipal():
        
    print(f'''Bem-Vindo - Menu Principal
    Escolha:
    1.Consultas 
    2.Cadastros   
    3.Alugueis''')

    escolha = input("Digite: ")
    match escolha:
        case "1":
            print(f'''Escolha:
    1. Consultar Livros
    2. Consultar Clientes
    3. Consultar Aluguel
    0. Voltar''')
            escolha2 = input("Digite: ")
            match escolha2:
                case "1":
                    menuconsultarLivros()
                case "2":
                    menuconsultarClientes()
                case "3":
                    menuconsultarAluguel
                case "0":
                    menuprincipal()
        
        case "2":
            print(f'''Escolha:
    1. Gerenciar Livros
    2. Gerenciar Clientes
    0. Voltar''')
            escolha3 = input("Digite: ")
            match escolha3:
                case "1":
                    menuCadastrosLivro()
                case "2":
                    menuCadastrosClientes()
                case "3":
                    menuprincipal()
        
        case "3":
            menualuguel()
        
        case _:
            print("Digitou algo errado")


menuprincipal() 
                  
               


