dias=int(input("insira um dia"))
mês_atual=int(input("insira um mês"))
ano=int(input("insira um ano"))
for mês in range(mês_atual,13):
    if (ano % 4==0 and ano % 100!=0) or ano % 400==0:
     dias=30
    if (ano % 4==0 and ano % 100!=0) or ano % 400==0:
        dias_mês=29
    else:
        dias_mês=28
    dias_restantes=dias_mês-dias
    dia=0
    soma=soma+dias_restantes
    print("faltam",dias_restantes,"dias pra o fim do ano")
   
