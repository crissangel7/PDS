import random
import matplotlib.pyplot as plt
import numpy as np

#tamaño de las señales
t1 = random.randint(2, 7)
t2 = random.randint(2, 7)

#Centro de cada señal
c1 = random.randint(0, t1)
c2 = random.randint(0, t2)

#Señales aleatorias
senal1 = [random.randint(-10, 10) for _ in range(t1)]
senal2 = [random.randint(-10, 10) for _ in range(t2)]

print("tamaños: ",t1,t2)
print("centros: ",c1,c2)

ventana=[-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6] #13 posiciones, centro en [6]

#s1 = int(6-c1)
#ss1 = int(13-c1)

time1 = ventana[6-c1:13-c1]
time2 = ventana[6-c2:13-c2]

#t1 = ventana[6:8]
print(time1,time2)

# Graficando ambas señales
fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.plot(time1,senal1)
ax1.set_title("Señal 1")
ax2.stem(senal2)
ax2.set_title("Señal 2")

# Ajustar el espacio entre subgráficos
fig.tight_layout()
plt.show()


