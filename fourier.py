import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

# Параметры сигнала
Fs = 1000  # Частота дискретизации (Гц)
duration = 1.0  # Длительность сигнала (сек)
t = np.linspace(0, duration, int(Fs * duration))  # Временная шкала

# Создание сигнала: две синусоиды
freq1 = 5    # 5 Гц
freq2 = 50   # 50 Гц
signal = 0.7 * np.sin(2 * np.pi * freq1 * t) + np.sin(2 * np.pi * freq2 * t)

# Вычисление преобразования Фурье
N = len(t)
yf = fft(signal)
xf = fftfreq(N, 1/Fs)  # Частотная шкала
amplitude = 2.0/N * np.abs(yf)  # Нормализованная амплитуда

# Фильтрация для положительных частот
positive_freqs = xf > 0
freqs = xf[positive_freqs]
amps = amplitude[positive_freqs]

# Создание фигуры с двумя подграфиками
plt.figure(figsize=(12, 6))

# 1. График исходного сигнала (временная область)
plt.subplot(1, 2, 1)
plt.plot(t, signal, 'b-', linewidth=1.5)
plt.xlabel('Время (с)', fontsize=12)
plt.ylabel('Амплитуда', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.xlim(0, 1.0)
plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)

# 2. График преобразования Фурье (частотная область) - синий цвет
plt.subplot(1, 2, 2)
plt.plot(freqs, amps, 'b-', linewidth=1.5)  # Изменен цвет на синий
plt.xlabel('Частота (Гц)', fontsize=12)
plt.ylabel('Амплитуда', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.xlim(0, 100)

# Подписи пиков (чистые, без дополнительных элементов)
plt.text(freq1, amps[np.where(freqs == freq1)[0][0]] + 0.05, 
         f'{freq1} Гц', fontsize=10, ha='center', color='blue')
plt.text(freq2, amps[np.where(freqs == freq2)[0][0]] + 0.05, 
         f'{freq2} Гц', fontsize=10, ha='center', color='blue')

# Общий заголовок
plt.subplots_adjust(top=0.9)
plt.show()