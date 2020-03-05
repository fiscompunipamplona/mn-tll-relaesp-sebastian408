import math as mt

R=float(input("ingrese el valor del Radio R= "))
Tetha=float(input("ingrese el valor del angulo en grados theta= "))

x=R*mt.cos(Tetha*mt.pi/180)
y=R*mt.sin(Tetha*mt.pi/180)



print("el valor de la coordenada x= ",x,"el valor de la coordenada y= ",y)

