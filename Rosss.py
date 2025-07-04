import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

a = 0.2
b = 0.2
c = 5.7

def rossler_system(t, state):
    x, y, z = state
    dxdt = -y - z
    dydt = x + a * y
    dzdt = b + z * (x - c)
    return [dxdt, dydt, dzdt]

initial_state = [0.0, 0.0, 0.0]  
t_span = (0, 100)               
t_eval = np.linspace(0, 100, 50000)  

solution = solve_ivp(
    rossler_system,
    t_span,
    initial_state,
    t_eval=t_eval,
    method='RK45',
    rtol=1e-7
)

x = solution.y[0]
y = solution.y[1]
z = solution.y[2]

plt.figure(figsize=(10, 8))
plt.plot(x, y, 'b-', linewidth=0.2)
plt.xlabel('X', fontsize=12)
plt.ylabel('Y', fontsize=12)
plt.grid(alpha=0.3)
plt.show()