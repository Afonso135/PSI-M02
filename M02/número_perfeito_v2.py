n=int(input("insira o lilmte máximo:"))
for k in range(1,n):
     soma=0
     for i in range(1,k):
      resto=k%1
     if resto==0:
      soma=soma+1
     if soma==k:
        print(f"o número{k} perfeito")
else:
        print("o número{k} não é perfeito")
