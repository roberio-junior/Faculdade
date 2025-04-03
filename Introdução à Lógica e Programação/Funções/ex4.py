#   Crie uma função em linguagem Python que receba 2 números e retorne
# o maior valor.

def maiorNumero(num1, num2):
    if num1 > num2:
        maior = num1
    elif num2 > num1:
        maior = num2
    else:
        return "Os números são iguais"
    return f"O maior numero é o {maior}"

numero1 = float(input("Informe o 1º número: "))
numero2 = float(input("Informe o 2º número: "))

maiorNumero(numero1, numero2)