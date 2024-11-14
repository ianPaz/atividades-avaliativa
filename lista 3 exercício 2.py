
# pede o valor de N
N = int(input("Digite um número para saber quantos numeros primos há entre eles: "))

# números primos entre 1 e N
print(f"Os números primos entre 1 e {N} são:")

for num in range(2, N + 1):  #0 e 1 não vai nessa bomba
    # Verifica se num é primo
    for i in range(2, num):  # Verifica se num é divisível por qualquer número de 2 até num-1
        if num % i == 0:  # Se for divisível, não é primo
            break
    else:
        print(num, end=" ")  # Se não encontrar divisores, num é primo e é exibido
