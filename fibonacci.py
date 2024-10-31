n=int(input("insira quantos números da sequência de fibonacci deseja escrever"))
x1=0
x2=1
print(x1,",",x2)
for i in range(n,-2):
 soma=x1+x2
print(soma)
x2=soma
x1=x2

