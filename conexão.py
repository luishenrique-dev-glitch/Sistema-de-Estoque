import psycopg

conexao = psycopg.connect(
    host="localhost",
    dbname="Estoque",
    user="postgres",
    password="Minha_senha"
)

cursor = conexao.cursor()

cursor.execute("SELECT * FROM produtos")

produtos = cursor.fetchall()

print(produtos)

cursor.close()
conexao.close()
