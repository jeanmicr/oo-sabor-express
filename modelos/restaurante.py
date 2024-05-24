from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio 
class Restaurante: #classe
    restaurantes = []
    
    def __init__(self, nome, categoria):  #construtor   
        self._nome = nome .title()  #atributos da classe
        self.categoria = categoria.upper() #atributos da classe
        self._ativo = False #atributos da classe PRIVADO(Protegido) deve usar property para modificar
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)
        
    def __str__(self):
       return f'{self._nome} | {self.categoria}' #retorna o que está escrito dentro do objeto e não o código do objeto
   
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'\nNome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} |{'Status'}')
        print()
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')
            
    @property
    def ativo(self):
        return 'ativado' if self._ativo else 'desativado'
    
    def alternar_estado(self):
        self._ativo = not self._ativo
    
    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
        
    @property        
    def media_avaliacoes(self):
        if not self._avaliacao:
            return f'Sem avaliações'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_notas, 1)
        return media
    
    # def adcionar_bebida_cardapio(self, bebida):
    #     self._cardapio.append(bebida)
        
    # def adcionar_prato_cardapio(self, prato):
    #     self._cardapio.append(prato)
     
    def adcionar_no_cardapio(self, item):           
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)
            
    @property
    def exibir_cardapio(self):
        print(f'Cardápio do restaurante {self._nome}\n')
        for i,item in enumerate(self._cardapio,start=1):
            if hasattr(item,'descricao'):
                mensagem_prato  = f'{i}. Nome:{item._nome} | Preço: R${item._preco:.2f} | Descrição: {item.descricao}'
                print(mensagem_prato)
            elif hasattr(item,'sabor'):
                mensagem_sobremesa  = f'{i}. Nome:{item._nome} | Preço: R${item._preco:.2f} | Sabor: {item.sabor}'
                print(mensagem_sobremesa)
            else:
                mensagem_bebida  = f'{i}. Nome:{item._nome} | Preço: R${item._preco:.2f} | Tamanho: {item.tamanho}'
                print(mensagem_bebida)
        
        print()
        