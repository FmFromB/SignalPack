import numpy as np
import matplotlib.pyplot as plt

period = 2 * np.pi  # Период волны
A = 1.0             # Амплитуда

# Создаем временную ось
t = np.linspace(-period/2, period/2, 1000)

# Функция идеальной квадратной волны
def square_wave(t):
    return A * np.sign(np.sin(t))

# Функция для расчета ряда Фурье
def fourier_series(t, n_terms):
    result = np.zeros_like(t)
    for k in range(1, n_terms + 1):
        # Только нечетные гармоники
        n = 2 * k - 1
        amplitude = 4 * A / (np.pi * n)
        result += amplitude * np.sin(n * t)
    return result

# Создаем фигуру с тремя подграфиками
plt.figure(figsize=(12, 10))

# Настройки графиков
steps = [4, 32, 128]
colors = ['b', 'b', 'b']

for i, n_terms in enumerate(steps):
    plt.subplot(3, 1, i+1)
    
    # Идеальная квадратная волна
    plt.plot(t, square_wave(t), 'k-', linewidth=3, alpha=0.8)
    
    # Аппроксимация рядом Фурье
    approximation = fourier_series(t, n_terms)
    plt.plot(t, approximation, color=colors[i], linewidth=2.5, 
             label=f'({n_terms} гармоник)')
    
    # Настройки отображения
    plt.ylabel('Амплитуда', fontsize=11)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend(loc='upper right', fontsize=10)
    plt.ylim(-1.3 * A, 1.3 * A)
    plt.xlim(-period/2, period/2)

# Общие настройки
plt.xlabel('Время', fontsize=11)
plt.tight_layout(rect=[0, 0, 1, 0.97])
plt.show()