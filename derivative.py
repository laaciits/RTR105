#print(vars())

def mana_funkcija(x):
    return sin(x)

import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')

from numpy import sin, linspace
from matplotlib import pyplot as plt

x = linspace(0,4,11)
#print(vars())
y = mana_funkcija(x)

plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.title('F-cija un tas atvasinaajums')
plt.plot(x,y)
plt.plot(x,y,'ro')
#plt.legend(['f-cija ar starpvertibam', 'f-cija dažas veertiibas'])
#plt.show()

# atvasinaajuma apreekjins, izmantojott funkcijas aprekjinu

N = len(x)
delta_x = x[1] - x[0]
derivative = []
print(derivative)
for i in range(N):
    temp = (mana_funkcija (x[i] + delta_x) - mana_funkcija(x[i])) / delta_x
    derivative.append(temp)
    print(derivative)

plt.plot(x,derivative)
plt.plot(x,derivative,'go')
legend = []
legend.append('f-cija ar starpvertibam')
legend.append('f-cija dažas veertiibas')
legend.append('atvasinajums ar starpverrtibam')
legend.append('atvasinajuma dazhas vertibas')

#plt.legend(legend)
#plt.show()

#atvasinaajums_caur_masiivu = []
derivative_trough_array = []
for i in range(N-1):
    temp = (y[i+1] - y[i]) / (x[i+1] - x[i])
    derivative_trough_array.append(temp)

plt.plot(x[0:N-1],derivative_trough_array)
plt.plot(x[0:N-1],derivative_trough_array,'bo')

legend.append('atvasinaajums ar starpvertibam (aprekins, izmantojot massiva vertibas)')
legend.append('atvasinajuma dazhas vertibas (aprekins, izmamntojo masiva verbias)')

#plt.legend(legend)
plt.legend(legend, loc=3)
plt.show()


