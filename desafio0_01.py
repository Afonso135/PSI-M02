"""
Um programa para ler 2 números e indicar se são diferentes.se forem diferentes mostrar a diferença entre eles,
com um valor positivo
"""
n1=int(input("insira um número"))
n2=int(input("insira outro número"))
if n1==n2:
    print("iguais")
if n1<n2:
   print("O primeiro valor tem de ser maior")
else:
 print("diferentes")
 print(n1-n2)
