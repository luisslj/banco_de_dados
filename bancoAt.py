import mysql.connector

# Conectar ao banco de dados
conexao = mysql.connector.connect(
    host='localhost',           # ou IP do servidor
    user='seu_usuario_mysql',   # ex: 'root'
    password='sua_senha_mysql', # ex: '123456'
    database='banco_digital'    # nome do seu banco
)

# Criar cursor para executar comandos SQL
cursor = conexao.cursor()

# Exemplo: listar clientes
cursor.execute("SELECT nome, cpf FROM Cliente")
resultados = cursor.fetchall()

for nome, cpf in resultados:
    print(f"Nome: {nome} | CPF: {cpf}")

# Fechar conexão
cursor.close()
conexao.close()