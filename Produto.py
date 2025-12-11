class Produto:
    def __init__(self,nome,preco,estoque):
        self.__nome = nome
        self.__preco = preco
        self.__estoque = estoque

    def __str__(self):
        return f"nome:{self.nome}, preco:{self.__preco}, estoque:{self.__estoque}"
    
    #metodos getters
    @property
    def nome(self):
        return self.__nome
    
    @property
    def preco(self):
        return self.__preco
    
    @property
    def estoque(self):
        return self.__estoque
    
    #metodos setters
    @nome.setter
    def nome(self,novo_nome):
        if len(novo_nome) > 0 and isinstance(novo_nome,str):
            self.__nome = novo_nome
        else:
            print("Erro:Digite um nome valido")

    @preco.setter
    def preco(self,novo_preco):
        if novo_preco > 0 and isinstance(novo_preco,(int,float)):
            self.__preco = novo_preco
        else:
            print("Digite um preco valido")

    @estoque.setter
    def estoque(self,novo_estoque):
        if novo_estoque >= 0 and isinstance(novo_estoque,int):
            self.__estoque = novo_estoque
        else:
            print("Digite um estoque valido")

    
    