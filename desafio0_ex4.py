carga_máx=1000
contar_malas=0
while carga_máx<=1000:
    peso_mala=float(input("insira o peso de cada mala"))
    if peso_mala>carga_máx:
        break
contar_malas=contar_malas+1
carga_máx=peso_mala+carga_máx

