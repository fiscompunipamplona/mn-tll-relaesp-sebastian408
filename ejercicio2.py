import math as mt

c=3e8 #m/s

x1=float(input("Digite la distancia a la que se encuentra el planeta x= "))

v=float(input("Digite la velocidad a la que va la nave como fraccion de c V="))

x=x1*9.461e15

t=x*(1/(v*c))



tpr=(1/(mt.sqrt(1-(v**2))))*(t-((v*x)/c))




~                                             
