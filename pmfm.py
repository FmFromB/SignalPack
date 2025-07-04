import numpy as np
import matplotlib.pyplot as plt

# Параметры сигнала
fs = 1000          # Частота дискретизации (Гц)
T = 3             # Длительность сигнала (с)
t = np.arange(0, T, 1/fs)  # Временная ось

# Параметры модуляции
fc = 5            # Частота несущей (Гц)
fm = 1             # Частота модулирующего сигнала (Гц)
Am = 1            # Амплитуда модулирующего сигнала (В)
beta = 7           # Индекс модуляции (для сравнения эффектов)

# Модулирующий сигнал (синусоида)
m_t = Am * np.sin(2 * np.pi * fm * t)
m_t1 = Am * np.sin(2 * np.pi * fc * t)
# Генерация модулированных сигналов
def angle_modulator(mod_type, m_t, fc, beta, fm, t):
    """Универсальный модулятор угловой модуляции"""
    if mod_type == 'FM':
        # Для ЧМ: фаза = интеграл от частоты
        phi = 2 * np.pi * fc * t + 2 * np.pi * beta * fm * np.cumsum(m_t) / fs
    elif mod_type == 'PM':
        # Для ФМ: фаза пропорциональна сигналу
        phi = 2 * np.pi * fc * t + beta * m_t
    return np.cos(phi)

# Генерация сигналов
fm_signal = angle_modulator('FM', m_t, fc, beta, fm, t)
pm_signal = angle_modulator('PM', m_t, fc, beta, fm, t)

# Построение графиков
plt.figure(figsize=(12, 10))

# Модулирующий сигнал
plt.subplot(4, 1, 1)
plt.plot(t, m_t1, 'b')
plt.title('Исходный сигнал (5 Гц)')
plt.ylabel('Амплитуда')
plt.grid(True)

# Модулирующий сигнал
plt.subplot(4, 1, 2)
plt.plot(t, m_t, 'b')
plt.title('Модулирующий сигнал (1 Гц)')
plt.ylabel('Амплитуда')
plt.grid(True)

# Частотная модуляция (ЧМ)
plt.subplot(4, 1, 3)
plt.plot(t, fm_signal, 'g')
plt.title('Частотная модуляция (FM)')
plt.ylabel('Амплитуда')
plt.grid(True)


plt.tight_layout()
plt.show()