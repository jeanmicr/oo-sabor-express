class Restaurante: #classe
    restaurantes = []
    
    def __init__(self, nome, categoria):  #construtor   
        self._nome = nome .title()  #atributos da classe
        self.categoria = categoria.upper() #atributos da classe
        self._ativo = False #atributos da classe PRIVADO(Protegido) deve usar property para modificar
        Restaurante.restaurantes.append(self)
        
    def __str__(self):
       return f'{self._nome} | {self.categoria}' #retorna o que está escrito dentro do objeto e não o código do objeto
   
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}')
        print()
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo}')
            
    @property
    def ativo(self):
        return 'ativado' if self._ativo else 'desativado'
    
    def alternar_estado(self):
        self._ativo = not self._ativo
    
restaurante_praca = Restaurante('praça','Gourmet')
restaurante_praca.alternar_estado()
restaurante_pizza = Restaurante('pizza express', 'Italiana')

Restaurante.listar_restaurantes()