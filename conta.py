

class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de R$ {} na conta {} de {}".format(self.__saldo, self.__numero, self.__titular))

    def deposito(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel

    def saque(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print("R$ {} Não disponível para saque, necessário aumento de limite.".format(valor))

    def transferencia(self, valor, destino):
        self.saque(valor)
        destino.deposito(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "748"

    @staticmethod
    def codigo_bancos():
        return {"BB": "001", "Caixa": "104", "Bradesco": "237"}
