import math #importar da biblioteca a funçâo math
n=12.65
print(int(n))
print (round (n,1)) #arredonda para o número par mais próximo
print(math.ceil(n)) #arredonda sempre para o inteiro seguinte (para cima)
print(math.floor(n)) #arredonda sempre para o inteiro anterior (para baixo)

#arredondar para cima se a parte decimal >= 0.5
parte_decimal = n- int(n)
if parte_decimal >= 0.5:
    n= int(n) + 1
else:
    n = int(n)
print(n)


