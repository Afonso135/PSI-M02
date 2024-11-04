palavra = input("Introduza uma palavra:")
 
#inverter a palavra
palavra_invertida=""
for i in range(len(palavra)-1,-1,-1):
    palavra_invertida = palavra_invertida + palavra[i]
print(palavra_invertida)
if palavra_invertida == palavra:
    print(f'"{palavra}" é um palindromo')
else:
    print("Não é um palindromo")