import psycopg

conexao = psycopg.connect(
    host="localhost",
    dbname="Estoque",
    user="postgres",
    password="minha_senha"
)

cursor = conexao.cursor()

nome = input("Digite o nome do produto: ")
preco = float(input("Digite o preço: "))
quantidade = int(input("Digite a quantidade: "))

cursor.execute("""
    INSERT INTO produtos (produto, preco, quantidade)
    VALUES (%s, %s, %s)
""", (nome, preco, quantidade))

conexao.commit()

cursor.execute("SELECT * FROM produtos")

produtos = cursor.fetchall()

for produto in produtos:
    id_produto = produto[0]
    nome = produto[1]
    preco = produto[2]
    quantidade = produto[3]

    print(f"\nID: {id_produto}\n")
    print(f"Produto: {nome}")
    print(f"Preço: R$ {preco:.2f}")
    print(f"Quantidade: {quantidade}")
    print("-" * 30)

cursor.close()
conexao.close()