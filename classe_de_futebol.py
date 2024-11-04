# este programa diz qual a sua classe dependendo da sua idade 
idade=int(input("insira asua idade"))
if idade<10:
    print("estás nos infantis")
elif idade>=10 and idade<14:
    print("estás nos juniores")
elif idade>=14 and idade<18:
    print("séniores")
