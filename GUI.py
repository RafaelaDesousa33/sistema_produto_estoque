import produtoDB
import streamlit as st

produtoDB.criarTabela()

st.title("Produtos")

nome = st.text_input("Nome do produto:")
preco = st.number_input("Preco do produto:",step=1)
estoque = st.number_input("Estoque do produto:", step=1)

if st.button("adicionar"):
    produtoDB.inserir_dados(nome,preco,estoque)
    st.success("Produto cadastrado")

if st.button("aumentar estoque"):
    produtoDB.aumentar_estoque(nome,estoque)

if st.button("diminuir estoque"):
    produtoDB.diminuir_estoque(nome,estoque)


if st.button("remover todos os produtos"):
    produtoDB.deletar_tudo()

if st.button("deletar pelo nome"):
    produtoDB.deletar_produto_pelo_nome(nome)

produtos = produtoDB.visualizar_dados()
produtos_formatado = []

for p in produtos:
    id_, nome, preco, estoque = p

    preco_formatado = f"{preco:.2f}"
    produtos_formatado.append((id_, nome, preco_formatado, estoque))

st.header("Lista produtos:")
st.table(produtos_formatado)
