n=float(input("insira um número"))
n=n+0.5
somatório=0
for i in range(10):
   if i<9:
    print(n,end=",")
   else:
    print(n,end="")
somatório=somatório+n
print(somatório)
 