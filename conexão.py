import psycopg

conexao = psycopg.connect(
    host="localhost",
    dbname="Estoque",
    user="postgres",
    password="luis9841"
)

cursor = conexao.cursor()

cursor.execute("SELECT * FROM produtos")

produtos = cursor.fetchall()

print(produtos)

cursor.close()
conexao.close()