import numpy as np
import matplotlib.pyplot as plt


frequency = 1.0  
sampling_rate = 10  
bits = 2  
duration = 2  

t_continuous = np.linspace(0, duration, 1000)  
t_sampled = np.arange(0, duration, 1/sampling_rate)  

signal_continuous = np.sin(2 * np.pi * frequency * t_continuous)
signal_sampled = np.sin(2 * np.pi * frequency * t_sampled)

def quantize(signal, bit_depth):
    max_val = 2**(bit_depth - 1) - 1  
    return np.round(signal * max_val) / max_val  

signal_quantized = quantize(signal_sampled, bits)

plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(t_continuous, signal_continuous, 'b-', label='Непрерывный сигнал')
plt.stem(t_sampled, signal_sampled, 'r-', markerfmt='ro', basefmt=" ", linefmt='r--', label='Дискретные отсчёты')
plt.title('Дискретизация сигнала')
plt.xlabel('Время (X)')
plt.ylabel('Амплитуда (Y)')
plt.grid(True)
plt.legend()

plt.subplot(2, 1, 2)
plt.step(t_sampled, signal_quantized, 'g-', where='post', label='Квантованный сигнал')
plt.plot(t_continuous, signal_continuous, 'b--', alpha=0.3, label='Исходный сигнал')
plt.title(f'Квантование ({bits}-бит)')
plt.xlabel('Время (X)')
plt.ylabel('Амплитуда (Y)')

for level in np.unique(signal_quantized):
    plt.axhline(y=level, color='gray', linestyle=':', alpha=0.5)

plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()