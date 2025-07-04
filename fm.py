import numpy as np
import matplotlib.pyplot as plt

fs = 1000         
T = 3             
t = np.arange(0, T, 1/fs)  

fc = 5            
fm = 1             
Am = 1            
beta = 7           

m_t = Am * np.sin(2 * np.pi * fm * t)
m_t1 = Am * np.sin(2 * np.pi * fc * t)

fm_signal = np.cos(2 * np.pi * fc * t + 2 * np.pi * beta * fm * np.cumsum(m_t) / fs)

plt.figure(figsize=(12, 10))

plt.subplot(4, 1, 1)
plt.plot(t, m_t1, 'b')
plt.title('Исходный сигнал (5 Гц)')
plt.ylabel('Амплитуда')
plt.grid(True)

plt.subplot(4, 1, 2)
plt.plot(t, m_t, 'b')
plt.title('Модулирующий сигнал (1 Гц)')
plt.ylabel('Амплитуда')
plt.grid(True)

plt.subplot(4, 1, 3)
plt.plot(t, fm_signal, 'g')
plt.title('Частотная модуляция (FM)')
plt.ylabel('Амплитуда')
plt.grid(True)


plt.tight_layout()
plt.show()