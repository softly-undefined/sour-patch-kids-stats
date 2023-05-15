import numpy as np
import matplotlib.pyplot as plt
import math

def equation(x):
    return ((x * (math.e ** (-x/2)))/4)

x = np.linspace(-10,175,1000)

y = equation(x)

plt.plot(x, y, linewidth=2.5)
plt.xlabel('$X^2$')
plt.ylabel('pdf($X^2$)')
plt.title('$X^2$ Distribution Graph')

x_value = 9.02  
plt.axvline(x=x_value, color='r', linestyle='--', linewidth=2.5, label='Critical Value')

x_value = 140.7889
plt.axvline(x=x_value, color='b', linestyle='--', linewidth=2.5, label='$X^2$ Statistic')

plt.legend()
plt.grid(True)

plt.xlim(0, 150)
plt.ylim(0, 0.25)

plt.show()




