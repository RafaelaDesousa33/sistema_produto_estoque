from Produto import Produto

class GerenciamentoProdutos:
    def __init__(self):
        self.listaProdutos = []

    def adicionar_produto(self):
     while True:
        escolha = input("Digite sua escolha(adicionar,sair):")

        if escolha == "adicionar":
         nome_produto = input("Digite o nome do produto:")
         preco_produto = float(input("Digite o preco do produto"))
         estoque_produto = int(input("Digite o estoque:"))

         novoProduto = Produto(nome_produto,preco_produto,estoque_produto)
         self.listaProdutos.append(novoProduto)

        elif escolha == "sair":
           print("Obrigado!")
           break
        else:
           print("Escolha invalida.Tente novamente")

    def aumentar_estoque(self):
     while True:
      escolha = input("Digite sua escolha(aumentar,sair)")
      
      if escolha == "aumentar":
        produto_digitado = input("Digite o nome do produto que deseja aumentar:")
        for produtos in self.listaProdutos:
        
          if produtos.nome == produto_digitado:
            numero = int(input("Digite o numero:"))

            if numero >=0 and isinstance(numero,int):
              produtos.estoque+=numero
              print("Estoque aumentado com sucesso!")
            else:
              print("Digite um estoque valido")
            
            
      elif escolha == "sair":
         print("Obrigado!")
         break
      
      else:
         print("Escolha invalida. Tente novamente")
      
    def diminuir_estoque(self):
     while True:
      escolha = input("Digite sua escolha(diminuir,sair)")

      if escolha == "diminuir":
         produto_digitado = input("Digite o nome do produto que deseja diminuir:")
         for produtos in self.listaProdutos:
         
          if produtos.nome == produto_digitado:
            numero = int(input("Digite o numero:"))
            if numero >= 0 and isinstance(numero,int):
                produtos.estoque-=numero
                print("Estoque diminuido com sucesso!")

      elif escolha == "sair":
         print("Obrigado!")
         break
      
      else:
         print("Escolha invalida.Tente novamente")
    
    def listar_produtos(self):
      for produtos in self.listaProdutos:
        print(produtos)

  

 
