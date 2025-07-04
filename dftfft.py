import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

# Создаем диапазон значений n (степени двойки для FFT)
n = np.arange(1, 513)  # От 1 до 512

# Рассчитываем сложности
dft_complexity = n**2
fft_complexity = n * np.log2(np.where(n > 1, n, 2))  # Избегаем log(1)=0
n32_complexity = n**1.5  # O(n^{3/2})

# Нормализуем значения для сравнения
max_dft = np.max(dft_complexity)
dft_norm = dft_complexity / max_dft
fft_norm = fft_complexity / max_dft
n32_norm = n32_complexity / max_dft

# Создаем фигуру
plt.figure(figsize=(12, 7))

# Строим нормализованные кривые
plt.plot(n, dft_norm, 'r-', linewidth=3, label='ДПФ: O(n²)')
plt.plot(n, n32_norm, 'g-', linewidth=3, label='НЕ ОПТИМИЗИРОВАННОЕ БПФ: O(3/2)')
plt.plot(n, fft_norm, 'b-', linewidth=3, label='БПФ: O(n log n)')

# Настройка оформления
plt.xlabel('Размер входных данных (n)', fontsize=14)
plt.ylabel('Относительная сложность', fontsize=14)
plt.grid(alpha=0.2, linestyle='--')
plt.legend(fontsize=12, loc='upper left')

plt.xlim(1, 512)
plt.ylim(0, 1.05)
plt.tight_layout()
plt.show()