email=str("Trump")
password=str("ginger_rocoon")
tentativas=1
for i in range(3):
 email_u=input("insira o seu email")
 password_u=input("insira a palvra passe") 
 if password_u==password and email_u==email:
  print("sessão iniciada com sucesso")
  break
 if email_u!=email and password_u!=password:
  print("O login falhou")
 elif email_u==email and password_u!=password:
  print("O sua password está errada")
 else:
  print(" asua password está errada")
else:
  print("esgotou as tentativas")

