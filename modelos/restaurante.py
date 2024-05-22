from modelos.avaliacao import Avaliacao
class Restaurante: #classe
    restaurantes = []
    
    def __init__(self, nome, categoria):  #construtor   
        self._nome = nome .title()  #atributos da classe
        self.categoria = categoria.upper() #atributos da classe
        self._ativo = False #atributos da classe PRIVADO(Protegido) deve usar property para modificar
        self._avaliacao = []
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