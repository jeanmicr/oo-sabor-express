from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self,nome,preco,tamanho):
       super().__init__(nome,preco)
       self.tamanho = tamanho
        
    def __str__(self):  
        return self._nome #retornar o nome em forma de string e não de objeto.
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.05)
        