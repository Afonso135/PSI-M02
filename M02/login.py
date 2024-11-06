email=str("Trump")
password=str("ginger_rocoon")
tentativas=1
while tentativas<3:
 email_u=input("insira  o seu email")
 password_u=input("insira a palvra passe") 
 if password_u==password and email_u==email:
  print("sessão iniciada com sucesso")
  break
 if email_u!=email and password_u!=password:
  print("O login falhou")
  break
 elif email_u==email and password_u!=password:
  print("O seu email está errado")
  break
 else:
  print(" asua password está erradaa")
  break
if tentativas>3:
  print("esgotou as tentativas")

