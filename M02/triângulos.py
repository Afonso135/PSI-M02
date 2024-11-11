a=float(input("insira a medida do lado"))
b=float(input("insira a medida do lado"))
c=float(input("insira a medida do lado"))
if a<0 and b<0 and c<0:
 print("os valores têm de ser positivos")
if (a+b)<c and (b+c)<a and (a+c)<b:
 print("não é triângulo")
 if a==b and b==c:
  print("triângulo equilátero")
 elif a==b and b!=c:
  print("triângulo equilátero")
  print("triângulo")
else:
   print("triângulo escaleno")
   