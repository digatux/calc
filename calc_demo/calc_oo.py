""" Calc Code example"""


class Calc():

    def __init__(self, num1, num2):
        self._num1 = num1
        self._num2 = num2

    def sum_call(self):
        return self._num1 + self._num2

    def div_call(self):
        return self._num1 / self._num2

    def mult_call(self):
        return self._num1 * self._num2

    def sub_call(self):
        return self._num1 - self._num2


def main():

    num1 = int(500)
    num2 = int(39)

    # Criando um objeto para rodar a classe
    calc_run = Calc(num1, num2)

    # Soma
    print(f"A soma de {num1} + {num2} é : {calc_run.sum_call()}")

    # Divisão
    print(f"A divisão de {num1} / {num2} é : {calc_run.div_call()} ")

    # Multiplicação
    print(f"A multiplicacao de {num1} *  {num2} é: {calc_run.mult_call()}")

    # Subtracao
    print(f"A subtracao de {num1} - {num2} é : {calc_run.sub_call()}")


if __name__ == '__main__':
    main()
