
escolha=int(input("insira o número da operação que pretende realizar"))
saldo=0
while escolha!=4 and saldo<0:
   print("ATM")
1=("Ver saldo")
2=("depositar dinheiro")
3=("Levantar dinheiro")
4=("Terminar")
saldo=0
if escolha==1:
 print(saldo,"€")
elif escolha==2:
 dep=float(input("insira o valor a depositar"))
 if dep<0.01 and dep>1000:
      print("valor inválido")
if escolha==3:
  while saldo>0:
    saldo_lev=saldo-lev,round(saldo_lev,2)
    lev=float(input("insira o valor a levantar"))
  if lev<10 or lev>400: #or lev>saldo:
       print("valor inválido")