#1.Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.

#2.Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.

class ContaBancaria:
    def __init__(self, titular, saldo = 0,ativo = True):
        self.titular = titular
        self.saldo = saldo
        self._ativo = ativo
        
    def __str__(self):
        return f'Titular da Conta é {self.titular} e o seu saldo atual é: R$ {self.saldo}'

conta1 = ContaBancaria(titular='Jean', saldo=5000)
conta2 = ContaBancaria(titular='Michel', saldo=2500)

print(conta1)
print(conta2)