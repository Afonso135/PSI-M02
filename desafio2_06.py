n=int(input("insira um número"))
if n==0:
    print("o fatorial é de 1")
M=0
for i in range(1,n,1):
    M=n*i
    print(M)
