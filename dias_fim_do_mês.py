
dias=int(input("insira um dia"))
mês=int(input("insira um mês"))
ano=int(input("insira um ano"))
ano=input("insira um ano")
dias_mês=31
if (ano % 4==0 and ano % 100!=0) or ano % 400==0:
 dias=30
if (ano % 4==0 and ano % 100!=0) or ano % 400==0:
    dias_mês=29
else:
    dias_mês=28
dias_restantes=dias_mês-dias
print("faltam",dias_restantes,"dias pra o fim do mês")

