import numpy as np
import matplotlib.pyplot as plt 

frecuencia = 100
periodo = 1 / frecuencia
amplitud = 3
theta = 0

frecuencia_muestreo = 30 * frecuencia
periodo_frec_muestreo = 1 / frecuencia_muestreo
ciclos = 4

t = np.arange(0, ciclos * periodo, periodo_frec_muestreo)
x = amplitud * np.cos(2 * np.pi * frecuencia * t + theta)

plt.plot(t,x)
plt.grid('on')
plt.show()
