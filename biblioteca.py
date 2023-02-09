import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '7289',
    database = 'biblioteca'
)

cursor = conexao.cursor()
print("Conectado")