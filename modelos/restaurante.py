class Restaurante: #classe
    restaurantes = []
    
    def __init__(self, nome, categoria):  #construtor   
        self.nome = nome   #atributos da classe
        self.categoria = categoria #atributos da classe
        self._ativo = False #atributos da classe PRIVADO(Protegido) deve usar property para modificar
        Restaurante.restaurantes.append(self)
        
    def __str__(self):
       return f'{self.nome} | {self.categoria}' #retorna o que está escrito dentro do objeto e não o código do objeto
   
    def listar_restaurantes():
        print(f'{'Nome do Restaurante'} | {'Categoria'} | {'Status'}')
        print()
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo}')
            
    @property
    def ativo(self):
        return 'ativado' if self._ativo else 'desativado'
    
restaurante_praca = Restaurante('Praça','Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

Restaurante.listar_restaurantes()