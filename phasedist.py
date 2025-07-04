import numpy as np
from scipy import signal 
import matplotlib.pyplot as plt

base_freq = 5.0        
mod_freq = 1.0          
mod_depth = 2*np.pi     
duration = 3.0          

t = np.linspace(0, duration, int(44100 * duration))

original = np.sin(2 * np.pi * base_freq * t)                
phase_modulation = mod_depth * np.sin(2 * np.pi * mod_freq * t)  
modulated = np.sin(2 * np.pi * base_freq * t + phase_modulation) 

plt.figure(figsize=(12, 9))

plt.subplot(3, 1, 1)
plt.plot(t, original, color='blue', linewidth=1.5)
plt.title(f'Исходный сигнал {base_freq} Гц')
plt.xlim(0, 3) 
plt.ylim(-1.1, 1.1)
plt.grid(True)
plt.ylabel('Амплитуда')

plt.subplot(3, 1, 2)
plt.plot(t, phase_modulation, color='orange', linewidth=1.5)
plt.title(f'Модулирующий сигнал {mod_freq} Гц')
plt.xlim(0, 3)
plt.ylim(-mod_depth*1.1, mod_depth*1.1)
plt.grid(True)
plt.ylabel('Амплитуда')

plt.subplot(3, 1, 3)
plt.plot(t, modulated, color='red', linewidth=1.5)
plt.title('Фазо-модулированный сигнал')
plt.xlim(0, 3)
plt.ylim(-1.1, 1.1)
plt.grid(True)
plt.xlabel('Время (с)')
plt.ylabel('Амплитуда')

plt.tight_layout()
plt.show()