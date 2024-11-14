
peso = float(input("Digite seu peso para calcular o seu IMC"))
altura = float(input("Digite sua altura para calcular o IMC"))

imc = peso / (altura ** 2)

print(f"Seu IMC é: {imc:.2f} ")
