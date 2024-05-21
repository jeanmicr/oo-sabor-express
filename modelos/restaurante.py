class Restaurante: #classe
    restaurantes = []
    
    def __init__(self, nome, categoria):  #construtor   
        self.nome = nome   #atributos da classe
        self.categoria = categoria #atributos da classe
        self.ativo = False #atributos da classe
        Restaurante.restaurantes.append(self)
        
    def __str__(self):
       return f'{self.nome} | {self.categoria}' #retorna o que está escrito dentro do objeto e não o código do objeto
   
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')
    
restaurante_praca = Restaurante('Praça','Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

restaurantes = [restaurante_pizza, restaurante_praca]

Restaurante.listar_restaurantes()