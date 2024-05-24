from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

restaurante_praca = Restaurante('praça','Gourmet') #instância para testar restaurante
bebida_suco = Bebida('Suco de Melância', 5.0, 'grande')
bebida_suco.aplicar_desconto()
prato_pao = Prato('Paozinho', 2.0, 'O melhor pão da cidade')
prato_pao.aplicar_desconto()
sobremesa_gelatina = Sobremesa('Gelatina', 7.0, 'Morango')
sobremesa_gelatina.aplicar_desconto()
restaurante_praca.adcionar_no_cardapio(bebida_suco)
restaurante_praca.adcionar_no_cardapio(prato_pao)
restaurante_praca.adcionar_no_cardapio(sobremesa_gelatina)

def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()