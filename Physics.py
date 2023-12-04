from math import cos,tan,radians,sin
import numpy as np
import matplotlib.pyplot as plt
xo ,Yo =0 ,0
theta = 45
g = 9.81
vo = 20
x = np.linspace(0, 40, 100)  # Use an array of x values for a smooth curve

y =(-(g((x-xo)**2)))/2(((vo)**2)(cos(theta)**2)) + ((x-xo)(tan(theta)) + Yo)

t_flight=(2*vo*sin(theta))/g
print("The value of t_flight is "+ str(t_flight))
# Creating a simple plot
plt.plot(x, y, marker='o', color="blue")
plt.xlabel('Horizontal distance in meter')
plt.ylabel('Vertical distance in meter')
plt.title('Projectile Motion')
plt.show()