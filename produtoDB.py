import sqlite3
from GerenciamentoProdutos import GerenciamentoProdutos

def conectar():
    conexao = sqlite3.connect("produtos.db")
    return conexao

def criarTabela():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS produtos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    estoque INTEGER NOT NULL
    );
    """
    )
    conexao.commit()

def inserir_dados(nome,preco,estoque):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
    """
    INSERT INTO produtos(nome,preco,estoque)
    VALUES(?,?,?)
    """,
    (nome,preco,estoque)

    )
    conexao.commit()

def diminuir_estoque(nome_produto, quantidade):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT estoque FROM produtos WHERE nome = ?", (nome_produto,))
    resultado = cursor.fetchone()

    if not resultado:
        print("Produto não encontrado.")
        return

    estoque_atual = resultado[0]

    if quantidade > estoque_atual:
        print("Erro: quantidade maior que o estoque atual.")
        return

    novo_estoque = estoque_atual - quantidade

    cursor.execute("""
        UPDATE produtos SET estoque = ? WHERE nome = ?
    """, (novo_estoque, nome_produto))

    conexao.commit()
    conexao.close()
    print("Estoque diminuído com sucesso!")


def aumentar_estoque(nome_produto, quantidade):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT estoque FROM produtos WHERE nome = ?", (nome_produto,))
    resultado = cursor.fetchone()

    if not resultado:
        print("Produto não encontrado.")
        return

    estoque_atual = resultado[0]
    novo_estoque = estoque_atual + quantidade

    cursor.execute("""
        UPDATE produtos SET estoque = ? WHERE nome = ?
    """, (novo_estoque, nome_produto))

    conexao.commit()
    conexao.close()
    print("Estoque aumentado com sucesso!")


def deletar_tudo():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
    """
    DELETE FROM produtos
    """
    )
    conexao.commit()
    conexao.close()

def deletar_produto_pelo_nome(nome):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        """
        DELETE FROM produtos WHERE nome = ? 
        """,
        (nome,)
    )


def visualizar_dados():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM produtos")
    

    dados = cursor.fetchall()
    return dados
   



    

