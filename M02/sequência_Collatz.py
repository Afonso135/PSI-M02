x=int(input("insira um número"))
while x!=1:
   resto=x%2
   if resto==0:
      x=x//2
   else:
      x=x*3+1
print(x)
    
