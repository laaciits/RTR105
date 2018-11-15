import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')

from numpy import *
x = linspace(0, 7, 70)
y = cos(x)

from matplotlib import pyplot as plt
plt.xlabel('x')
plt.ylabel('f(x)')
plt.plot(x, y, color = "#AE00E4")



from numpy import *

y1 = sin(x)


plt.grid()
plt.ylabel('y')
plt.xlabel('f(x)')
plt.plot(x, y1, color = "#00CDFF")
plt.title('Funkcija $cos(x)$ un sin(x)')
plt.show()

         
