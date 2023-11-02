import matplotlib.pyplot as plt
import numpy as np

#Points
p1 = [0, 0]
p2 = [6, 6]

#Function to draw curved line
def draw_curve(p1, p2):
    
    a = (p2[1] - p1[1])/ (np.cosh(p2[0]) - np.cosh(p1[0]))
    b = p1[1] - a * np.cosh(p1[0])
    x = np.linspace(p1[0], p2[0], 8)
    y = a * np.cosh(x) + b
    
    return x, y


#Curved line
x, negy = draw_curve(p1, p2)
blue_y = np.linspace(p1[1], p2[1], 8)

filt1 = [int(i) for i in x]
filt2 = [int(i) for i in ]
plt.plot(x, blue_y+(blue_y-negy)[::-1], linewidth = 5, label = "mirror", color = "red")

plt.legend()
plt.show()