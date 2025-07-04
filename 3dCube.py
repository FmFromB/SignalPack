import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

step = 0.2
x_red = np.arange(0, 1.01, step)    
y_green = np.arange(0, 1.01, step)  
z_blue = np.arange(0, 1.01, step)   

X, Z_green, Y_blue = np.meshgrid(x_red, y_green, z_blue)

x_coords = X.ravel()         
y_coords = Y_blue.ravel()    
z_coords = Z_green.ravel()   

colors = np.stack([
    x_coords,    
    z_coords,    
    y_coords     
], axis=1)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(
    x_coords, 
    y_coords, 
    z_coords, 
    c=colors, 
    s=40,          
    alpha=0.8,     
    edgecolors='none'
)

ax.set_xlabel('Красный (X)', fontsize=12)
ax.set_ylabel('Синий (Z)', fontsize=12)
ax.set_zlabel('Зелёный (Y)', fontsize=12)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_zlim(0, 1)

ax.view_init(elev=25, azim=225)

plt.tight_layout()
plt.show()