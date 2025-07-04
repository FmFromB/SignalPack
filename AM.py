import numpy as np
import matplotlib.pyplot as plt

# Параметры сигнала
fs = 10000        # Частота дискретизации (Гц)
T = 0.02          # Длительность сигнала (с)
t = np.arange(0, T, 1/fs)  # Временная ось

# Параметры модуляции
fc = 500          # Частота несущей (Гц)
fm = 50           # Частота модулирующего сигнала (Гц)
Am = 1            # Амплитуда модулирующего сигнала
Ac = 1            # Амплитуда несущей
mu = 0.8          # Глубина модуляции (0-1)

# Генерация сигналов
carrier = Ac * np.cos(2 * np.pi * fc * t)          # Несущий сигнал
modulating = Am * np.cos(2 * np.pi * fm * t)       # Модулирующий сигнал

# Амплитудная модуляция
am_signal = (Ac + mu * modulating) * np.cos(2 * np.pi * fc * t)

# Огибающая сигнала
envelope_upper = Ac * (1 + mu * modulating)  # Верхняя огибающая
envelope_lower = Ac * (1 - mu * modulating)  # Нижняя огибающая (инвертированная)

# Построение графиков
plt.figure(figsize=(12, 10))

# 1. Модулирующий сигнал
plt.subplot(3, 1, 1)
plt.plot(t, modulating, 'b', linewidth=1.5)
plt.title('Модулирующий сигнал')
plt.ylabel('Амплитуда')
plt.grid(True)
plt.ylim(-1.5, 1.5)

# 2. Несущий сигнал
plt.subplot(3, 1, 2)
plt.plot(t, carrier, 'g', alpha=0.7)
plt.title('Несущий сигнал')
plt.ylabel('Амплитуда')
plt.grid(True)
plt.ylim(-1.5, 1.5)

# 3. Амплитудно-модулированный сигнал
plt.subplot(3, 1, 3)
plt.plot(t, am_signal, 'r')
plt.title('Амплитудная модуляция ')
plt.ylabel('Амплитуда')
plt.grid(True)
plt.legend()
plt.ylim(-2.2, 2.2)

plt.tight_layout()
plt.show()
