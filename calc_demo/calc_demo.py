def sum_call(a,b):
    return a + b

def div_call(a,b):
    return a / b

def mult_call(a,b):
    return a * b

def sub_call(a,b):
    return a - b

def main():

    num1 = int(500)
    num2 = int(39)

    # Soma
    print(f"A soma de {num1} + {num2} é : {sum_call(num1,num2)}")

    # Divisão
    print(f"A divisão de {num1} / {num2} é : {div_call(num1,num2)} ")

    # Multiplicação
    print(f"A multiplicacao de {num1} *  {num2} é: {mult_call(num1,num2)}")

    # Subtracao
    print(f"A subtracao de {num1} - {num2} é : {sub_call(num1,num2)}")
if __name__ == '__main__':
    main()
