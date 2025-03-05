# Receba um número inteiro e calcule sua raiz quadrada.
numero = input("Digite um número para saber a raiz quadrada: ")
numero = int(numero)

raiz = numero ** (1/2) #Operador de Potência
raiz = round(raiz, 4)

print("Raiz Quadrada de ", numero, "é", raiz)