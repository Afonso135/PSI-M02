for i in range(1,10):
letra=str(input("insira 10 letras"))
letra=letra.strip
if len(letra)!=1:
    print("Só pode inserir uma letra")
contar_vogais=0
for i in range(1,10):
    if i in "aeiouAEIOU":
        contar_vogais=contar_vogais+1


