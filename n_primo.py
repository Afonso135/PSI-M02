numero = int(input("Insira o nº a testar:"))
primo = True
for x in range(2,numero):
    if numero % x == 0:
        primo = False
        break
if primo == True:
    print("O nº ",numero," é primo")
else:
    print("O nº ",numero," não é primo")