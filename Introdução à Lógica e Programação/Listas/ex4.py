a = []
maior_par = None
menor_impar = None
soma = 0

for i in range(5):
    num = int(input("Digite um número inteiro: "))

    if num % 2 == 0 and (maior_par is None or num > maior_par):
        maior_par = num

    if num % 2 != 0 and (menor_impar is None or num < menor_impar):
        menor_impar = num

    a.append(num)
    soma += num

media = soma / 5

if maior_par is not None:
    print(f"Maior número par: {maior_par}")
else:
    print("Nenhum número par foi digitado.")

if menor_impar is not None:
    print(f"Menor número ímpar: {menor_impar}")
else:
    print("Nenhum número ímpar foi digitado.")

print(f"Somatório dos elementos: {soma}")
print(f"Média dos elementos: {media:.2f}")
