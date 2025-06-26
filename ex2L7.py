numeros = []
i = 0

while i < 5:
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)
    i += 1

n = len(numeros)
i = 0
while i < n - 1:
    j = 0
    while j < n - 1 - i:
        if numeros[j] > numeros[j + 1]:
            temp = numeros[j]
            numeros[j] = numeros[j + 1]
            numeros[j + 1] = temp
        j += 1
    i += 1


print("Números em ordem crescente:")
print(numeros)
