import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from tabulate import tabulate

A = 1.0         
f = 1         
fs = 20     
t_duration = 1
n_bits = 3  
quant_levels = 2 ** n_bits 

t_analog = np.linspace(0, t_duration, 1000)
analog_signal = A * np.sin(2 * np.pi * f * t_analog)
t_samples = np.arange(0, t_duration, 1/fs)
sampled_signal = A * np.sin(2 * np.pi * f * t_samples)

quant_step = 2 * A / quant_levels
quantized_signal = np.round(sampled_signal / quant_step) * quant_step

quant_indices = []
for value in sampled_signal:
    level_index = int(np.round((value + A) / quant_step))
    level_index = np.clip(level_index, 0, quant_levels - 1)
    quant_indices.append(level_index)

binary_codes = []
for index in quant_indices:
    binary_codes.append(format(index, f'0{n_bits}b'))

table_data = []
for level in range(quant_levels):
    min_amp = -A + level * quant_step
    max_amp = -A + (level + 1) * quant_step
    binary_code = format(level, f'0{n_bits}b')
    table_data.append([
        level,
        binary_code,
    ])

print("\n" + "="*80)
print(f"Таблица соответствия уровней квантования и двоичных кодов ({n_bits}-битное квантование)")
print("="*80)
print(tabulate(table_data, headers=["Уровень", "Двоичный код"], tablefmt="grid"))
print("="*80)

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 10))

ax1.plot(t_analog, analog_signal, 'b-', label='Аналоговый сигнал')
ax1.stem(t_samples, sampled_signal, 'ro', basefmt=' ', linefmt='r-', markerfmt='ro')
ax1.set_title('1. Дискретизация сигнала')
ax1.set_ylabel('Амплитуда')
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.legend(loc='upper right')
ax1.set_ylim(-A*1.2, A*1.2)

ax2.set_title('2. Квантование сигнала')
ax2.set_ylabel('Уровень квантования')
ax2.set_xlim(0, t_duration)
ax2.set_ylim(-0.5, quant_levels - 0.5)
ax2.grid(True, linestyle='--', alpha=0.7)

ax2.step(t_samples, quant_indices, 'g-', where='post', linewidth=2, label='Квантованный индекс')
ax2.plot(t_samples, quant_indices, 'ro', markersize=6, label='Отсчёты')

for level in range(quant_levels):
    ax2.axhline(y=level, color='gray', linestyle='--', alpha=0.4)

ax3.set_title('3. Двоичное представление сигнала')
ax3.set_xlabel('Время (сек)')
ax3.set_ylabel('Уровень напряжения')
ax3.set_xlim(0, t_duration)
ax3.set_ylim(-0.1, 1.5)
ax3.grid(True, linestyle='--', alpha=0.7)

bit_duration = 1/fs / n_bits  
high_level = 1.0  
low_level = 0.0   

nrz_time = []
nrz_value = []

for i, (t, code) in enumerate(zip(t_samples, binary_codes)):
    for bit_pos, bit in enumerate(code):
        start_time = t + bit_pos * bit_duration
        bit_value = high_level if bit == '1' else low_level
        nrz_time.append(start_time)
        nrz_value.append(bit_value)
        nrz_time.append(start_time + bit_duration)
        nrz_value.append(bit_value)

ax3.plot(nrz_time, nrz_value, 'b-', linewidth=2)

for t in t_samples:
    ax3.axvline(x=t, color='purple', linestyle='--', alpha=0.5, linewidth=1.5)

for i, t in enumerate(t_samples):
    for bit_pos in range(1, n_bits):
        divider = t + bit_pos * bit_duration
        ax3.axvline(x=divider, color='gray', linestyle=':', alpha=0.3)

ax3.xaxis.set_major_locator(MultipleLocator(0.1))
ax3.xaxis.set_minor_locator(MultipleLocator(0.025))
print(binary_codes)
print(*quant_indices)

plt.tight_layout()
plt.subplots_adjust(top=0.93, hspace=0.35)
plt.show()