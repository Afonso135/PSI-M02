#Elabore um programa em Python que lê números do utilizador. Para cada número que lê deve indicar se o número é positivo ou negativo. O programa deve terminar quando o utilizador insere o nº 0 (zero). Assuma que os valores são números inteiros.
n = 1
while n!=0:
    n = int(input("Nº"))
    if n > 0:
        print("Positivo")
    elif n < 0:
        print("Negativo")
