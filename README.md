Sistema de Gerenciamento de Produtos e Estoque

Este projeto implementa um sistema simples de gerenciamento de produtos utilizando Python, SQLite e Streamlit.
O sistema permite cadastrar produtos, controlar estoque e visualizar os dados de maneira prática.

Funcionalidades

Cadastro de produtos com nome, preço e quantidade.

Aumento e diminuição de estoque.

Remoção de produtos pelo nome.

Exclusão de todos os produtos do banco.

Exibição dos produtos em uma tabela organizada.

Tecnologias Utilizadas

Python

Streamlit

SQLite

Programação Orientada a Objetos

Captura de Tela

A imagem abaixo mostra parte da interface do sistema:

![Interface do sistema](sistema_estoque_produtos_foto.png)

Demonstração em Vídeo

Vídeo mostrando o funcionamento do projeto:

![Demonstração em vídeo](demo_video.mp4)


O GitHub não executa vídeos diretamente no README, mas exibirá um player quando o arquivo estiver no repositório.

Como Executar

Instale as dependências:

pip install streamlit


Execute o programa:

streamlit run GUI.py


O sistema será aberto automaticamente no navegador.

Estrutura do Projeto

GUI.py – Interface no Streamlit.

produtoDB.py – Acesso ao banco SQLite.

GerenciamentoProdutos.py – Lógica de gerenciamento.

Produto.py – Classe representando um produto.

produtos.db – Banco de dados.

sistema_estoque_produtos_foto.png – Imagem de demonstração.


Contribuição

Sugestões de melhorias são bem-vindas.
