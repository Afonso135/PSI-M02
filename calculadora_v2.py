n1=int(input("insira um número"))
n2=int(input("insira outro número"))
multiplicação=n1*n2
divisão=n1/n2
soma=n1+n2
subtração=n1-n2
escolha=0
while escolha:
operação=input("insira a operação a realizar")
if operação.lower() in soma:
elif operação.lower() in multiplicação:
elif opreação.lower() in divisão:
elif operação.lower() in subtração:

else:
 (None)
 