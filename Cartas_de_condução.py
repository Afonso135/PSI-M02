pontos_total=12
infração_leve=pontos_total-1
infração_grave=pontos_total-4
infração_muito_grave=pontos_total-6
escolha=0
while escolha!="4":
    print(pontos_total)
if infração_leve>0:
    print(infração_leve)
elif escolha==infração_grave:
    print ("descontou-se 4 pontos. O seu total de pontos é de",pontos_total)
elif escolha==infração_muito_grave:
    print("decontou-se 6 pontos. O seu total de pontos é de",pontos_total)
elif pontos_total==0:
    print("perdeu a carta de condução")
if escolha==(infração_muito_grave==1 and infração_grave==1) or (infração_grave==2):
    pontos=0  
