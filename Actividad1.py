import mesa
import numpy as nup
import random
import time

inicio = time.time()
#celdas = nup.empty((m, n), int)

# taking input from user
m = int(input("Favor de ingresar M: "))
n = int(input("Favor de ingresar N: "))
agentes = int(input("Favor de ingresar el número de agentes: "))
porcentaje = int(input("Favor de ingresar el porcentaje de celdas sucias: "))
tiempoMax = int(input("Favor de ingresar el tiempo máximo de ejecución: "))

randoms = int((porcentaje/100)*(n*m))

print(randoms)

celdas = []

for i in range(m):
    fila = []
    
    for j in range(n):
        fila.append(0)
        
    celdas.append(fila)

x = 0
y = 0

while randoms > 0:
    x = random.choice([0,(m-1)])
    y = random.choice([0,(n-1)])
    
    if(celdas[x][y] == 0):
        celdas[x][y] = 1
        randoms -= 1

print("Lugares sucios")
print(celdas)
x =0
y= 0
z=0
movimientos = 0
while x < m:
    while y < n:
        if celdas[x][y] == 1:
            print("Locacion de la aspiradora,", x, y)
            celdas[x][y] = 0
            print("Limpiado en", x, y)
            movimientos = (x*4) + y+1
            z+=1
        y+=1
    x+=1
    y=0
porcentaje= ((z/(n*m))*100)
print(celdas)
print('porcentaje = ',porcentaje,'%')
final = time.time()
print('Tiempo de ejecución =', (final-inicio), 'segundos')
print('Movimientos =', movimientos)