import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')

from numpy import *
x = linspace(0, 4, 11)
y = sin(x)

from matplotlib import pyplot as plt
plt.grid()
plt.ylabel('x')
plt.xlabel('f(x)')
plt.title('Funkcija $sin(x)$')
plt.plot(x, y, color = "#AE00E4")

y1 = x
y2 = x-x*x*x/(1*2*3)
y3 = y2+x**5/(1*2*3*4*5)
y4 = y3-x**7/(1*2*3*4*5*6*7)

plt.plot(x, y1, color="#00FF00")
plt.plot(x, y2, color="#0000FF")
plt.plot(x, y3, color="#FFFF00")
plt.plot(x, y4, color="#00FFFF")
plt.show()
