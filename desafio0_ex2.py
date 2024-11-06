hora=int(input("insira uma hora"))
madrugada=5,6,7
manhã=8,9,10,11,12
tarde=13,14,15,16,17,18,19
noite=20,21,22,23,00,1,3,4
if hora  in madrugada:
    print("madrugada")
elif hora in manhã:
    print("manhã")
elif hora in tarde:
    print("tarde")
elif hora in noite:
    print("noite")