numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operador = input("Digite o operador (+, -, *, /): ")

#se
if operador == "+":
    resultado = numero1 + numero2
    print(f"{numero1} + {numero2} = {resultado}")
#senao
elif operador == "-":
    resultado = numero1 - numero2
    print(f"{numero1} - {numero2} = {resultado}")
elif operador == "*":
    resultado = numero1 * numero2
    print(f"{numero1} * {numero2} = {resultado}")
elif operador == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
        print(f"{numero1} / {numero2} = {resultado}")
        #é esse
    else:
        print("não é possivel dividir essa operação")
else:
    print("Operador inválido. Use +, -, * ou /") 

