import psycopg
from dotenv import load_dotenv
import os

load_dotenv()

conexao = psycopg.connect(
    host=os.getenv("DB_HOST"),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)

cursor = conexao.cursor()

     
def cadastrar_produto():
    while True:
        
        while True:

            produto = input('Digite qual produto deseja cadastrar: ').strip()

            if not produto:
                print('O nome do produto não pode ficar vazio.')
                continue
            
            break

        while True:
            try:
                preco = float(input('Digite o valor do produto: '))

                if preco < 0:
                    print('O preço não pode ser negativo')
                    continue

                break

            except ValueError:
                print('Digite um valor válido!')

        while True:
            try:
                quantidade = int(input('Digite a quantidade do produto: '))

                if quantidade < 0:
                    print('Quantidade não pode ser menor que 0')
                    continue

                break

            except ValueError:
                print('Digite um valor válido!')

        cursor.execute("""
        INSERT INTO produtos (produto, preco, quantidade)
        VALUES (%s, %s, %s)
        """, (produto, preco, quantidade))

        conexao.commit()

        continuar = input(
            'Deseja cadastrar mais um produto? (sim/não): '
        ).lower()

        if continuar == 'não' or continuar == 'nao':
            break  
        
def produtos_cadastrados():

   cursor.execute("SELECT * FROM produtos")

   produtos = cursor.fetchall()

   print('\n===== PRODUTOS CADASTRADOS =====')

   for produto in produtos:

      id_produto = produto[0]
      nome = produto [1]
      preco = produto[2]
      quantidade = produto[3]

      print(f'ID: {id_produto}')
      print(f'Produto: {nome}')
      print(f'Preço: R$: {preco:.2f}')
      print(f'Quantidade: {quantidade}')
      print('-' * 30)

def buscar_produtos():

    produto_busca = input('Qual produto gostaria de buscar: ').lower()

    cursor.execute("""
    SELECT * FROM produtos
    WHERE LOWER(produto) = LOWER(%s)
    """, (produto_busca,))

    produto = cursor.fetchone()

    if produto:

     print('\n========= Produto Encontrado =========\n')

     print(f"ID: {produto[0]}")
     print(f"Produto: {produto[1]}")
     print(f"Preço: R$ {produto[2]:.2f}")
     print(f"Quantidade: {produto[3]}")

     print('\n======================================')

    else:
        print('Produto indisponível.')

def atualizar_valores():

    nome_busca = input('Qual produto deseja atualizar: ').strip()

    cursor.execute("""
        SELECT * FROM produtos
        WHERE LOWER(produto) = LOWER(%s)
    """, (nome_busca,))

    produto = cursor.fetchone()

    if produto:

        id_produto = produto[0]

        print(f"Produto encontrado: {produto[1]}")

        opcao = input(
            'Deseja alterar o preço ou a quantidade deste produto? '
        ).lower()

        if opcao in ('preço', 'preco'):

            novo_preco = float(
                input('Digite o novo valor: ')
            )

            cursor.execute("""
                UPDATE produtos
                SET preco = %s
                WHERE id = %s
            """, (novo_preco, id_produto))

            conexao.commit()

            print('Preço atualizado com sucesso!')

        elif opcao == 'quantidade':

            nova_quantidade = int(
                input('Digite a nova quantidade: ')
            )

            cursor.execute("""
                UPDATE produtos
                SET quantidade = %s
                WHERE id = %s
            """, (nova_quantidade, id_produto))

            conexao.commit()

            print('Quantidade atualizada com sucesso!')

        else:

            print('Opção inválida.')

    else:

        print('Produto indisponível.')

def excluir_produto():

    produto_busca = input('Qual produto deseja excluir: ').lower()

    cursor.execute("""
        SELECT * FROM produtos
        WHERE LOWER(produto) = LOWER(%s)
    """, (produto_busca,))

    produto = cursor.fetchone()

    if produto:

       id_produto = produto[0]

       print(f'Produto encontrado: {produto[1]}')

       confirmacao = input('Tem certeza que deseja excluir?(sim/não): ').lower()

       if confirmacao in 'sim,':

          cursor.execute("""
                DELETE FROM produtos
                WHERE id = %s
            """, (id_produto,))

          conexao.commit()

          print('Produto excluído com sucesso!')

       else:
            print('Exclusão cancelada.')

    else:
        print('Produto indisponível.')

def ordenar_produtos():

    opcao = input('Você deseja ordenar por qual ordem? (produto / preço / quantidade): ').lower()

    ordem = input('Gostaria de ordenar na ordem crescente ou decrescente? ').lower()

    if ordem == 'crescente':
        ordem_sql = 'ASC'

    elif ordem == 'decrescente':
        ordem_sql = 'DESC'

    else:
        print('Ordem inválida.')
        return

    if opcao == 'produto':

        cursor.execute(f"""
            SELECT * FROM produtos
            ORDER BY produto {ordem_sql}
        """)

    elif opcao in ('preço', 'preco'):

        cursor.execute(f"""
            SELECT * FROM produtos
            ORDER BY preco {ordem_sql}
        """)

    elif opcao == 'quantidade':

        cursor.execute(f"""
            SELECT * FROM produtos
            ORDER BY quantidade {ordem_sql}
        """)

    else:
        print('Opção inválida.')
        return

    produtos = cursor.fetchall()

    print('\n===== PRODUTOS ORDENADOS =====')

    for produto in produtos:

        print(f"ID: {produto[0]}")
        print(f"Produto: {produto[1]}")
        print(f"Preço: R$ {produto[2]:.2f}")
        print(f"Quantidade: {produto[3]}")
        print('-' * 30)

def relatorio_estoque():

    # 1 - Quantidade de produtos cadastrados
    cursor.execute("SELECT COUNT(*) FROM produtos")
    quantidade_produtos = cursor.fetchone()[0]

    # Verifica se existem produtos
    if quantidade_produtos == 0:
        print("\nNão existem produtos cadastrados.")
        return

    # 2 - Quantidade total em estoque
    cursor.execute("SELECT SUM(quantidade) FROM produtos")
    quantidade_total = cursor.fetchone()[0]

    # 3 - Valor total do estoque
    cursor.execute("""
        SELECT SUM(preco * quantidade)
        FROM produtos
    """)
    valor_total = cursor.fetchone()[0]

    # 4 - Produto mais caro
    cursor.execute("""
        SELECT * FROM produtos
        ORDER BY preco DESC
        LIMIT 1
    """)
    produto_mais_caro = cursor.fetchone()

    # 5 - Produto mais barato
    cursor.execute("""
        SELECT * FROM produtos
        ORDER BY preco ASC
        LIMIT 1
    """)
    produto_mais_barato = cursor.fetchone()

    # 6 - Produto com menor estoque
    cursor.execute("""
        SELECT * FROM produtos
        ORDER BY quantidade ASC
        LIMIT 1
    """)
    produto_menor_estoque = cursor.fetchone()

    cursor.execute("""
        SELECT COUNT(*)
        FROM produtos
        WHERE quantidade = 0
         """)

    produtos_zerados = cursor.fetchone()[0]

    # Relatório
    print("\n=============== RELATÓRIO DE ESTOQUE ===============\n")

    print(f"Quantidade de produtos cadastrados: {quantidade_produtos}")
    print(f"Quantidade total em estoque: {quantidade_total}")
    print(f"Valor total do estoque: R$ {valor_total:.2f}")

    print()

    print(
        f"Produto de maior preço: "
        f"{produto_mais_caro[1]} — R$ {produto_mais_caro[2]:.2f}"
    )

    print(
        f"Produto de menor preço: "
        f"{produto_mais_barato[1]} — R$ {produto_mais_barato[2]:.2f}"
    )

    print(
        f"Produto de menor estoque: "
        f"{produto_menor_estoque[1]} — "
        f"{produto_menor_estoque[3]} unidades"
    )

    print(
        f"Produtos com estoque zerado: "
        f"{produtos_zerados}"
    )
    print("\n====================================================\n")
    
def menu():
      
   while True:

       print('\n===== SISTEMA DE PRODUTOS =====')
       print()
       print('1 - Cadastrar produtos')
       print('2 - Produtos Cadastrados')
       print('3 - Buscar Produtos')
       print('4 - Atualizar Produtos')
       print('5 - Exluir produtos')
       print('6 - Ordenar produtos')
       print('7 - Relatorio de Estoque')
       print('8 - Sair')
       print('\n===============================')

       opcao = (input('Qual opção deseja usar? '))
   
       if opcao == '1':
         cadastrar_produto()

       elif opcao =='2':
         produtos_cadastrados()

       elif opcao == '3':
        buscar_produtos()

       elif opcao == '4':
        atualizar_valores()

       elif opcao == '5':
        excluir_produto()

       elif opcao == '6':
        ordenar_produtos()

       elif opcao == '7':
        relatorio_estoque()
       elif opcao == '8':
        break

menu()

cursor.close()
conexao.close()