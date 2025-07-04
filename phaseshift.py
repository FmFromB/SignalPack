import numpy as np
import matplotlib.pyplot as plt

def generate_sine_wave(t, freq, amplitude=1.0, phase=0.0):
    return amplitude * np.sin(2 * np.pi * freq * t + phase)

frequency = 1.0           
duration = 5.0            
amplitude = 1.0         
phase_shift_degrees = 180
period = 3 

phase_shift = np.deg2rad(phase_shift_degrees)

t = np.linspace(0, duration, int(44100 * duration), endpoint=False)

wave1 = generate_sine_wave(t, frequency, amplitude, phase=0)
wave2 = generate_sine_wave(t, frequency, amplitude, phase=phase_shift)
wave_sum = wave1 + wave2

plt.figure(figsize=(10, 6))
t_zoom = period/frequency 

plt.subplot(3, 1, 1)
plt.plot(t, wave1, color='blue', label=f'Волна 1 (Фаза: 0°)')
plt.xlim(0, t_zoom)
plt.ylim(-2.1, 2.1)
plt.grid(True)
plt.ylabel('Амплитуда')
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(t, wave2, color='red', label=f'Волна 2 (Фаза: {phase_shift_degrees}°)')
plt.xlim(0, t_zoom)
plt.ylim(-2.1, 2.1)
plt.grid(True)
plt.ylabel('Амплитуда')
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(t, wave_sum, color='green', label='Сумма')
plt.xlim(0, t_zoom)
plt.ylim(-2.1, 2.1)
plt.grid(True)
plt.xlabel('Время (с)')
plt.ylabel('Амплитуда')
plt.legend()

plt.tight_layout()
plt.show()