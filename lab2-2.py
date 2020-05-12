import random
import math
import matplotlib.pyplot as plt
import numpy as np

from copy import copy
from datetime import datetime

harmNumber = 14
dotNumber = 64
omegaMax = 2500
omegaInterval = omegaMax / harmNumber

# ampl = random.randint(1, 10)
ampls = []
for i in range(harmNumber):
    ampls.append(random.randint(1, 10))

# phase = 0
phases = []
for i in range(harmNumber):
    phases.append(random.uniform(0, math.pi))

mainX = []
for i in range(dotNumber):
    currentX = 0
    for j in range(harmNumber):
        currentX += ampls[j] * math.sin(omegaInterval * (j + 1) * i + phases[j])
    mainX.append(currentX)

fft_dot_number = dotNumber // 2

x_real_first = [0 for i in range(fft_dot_number)]
x_real_second = [0 for i in range(fft_dot_number)]
x_imag_first = [0 for i in range(fft_dot_number)]
x_imag_second = [0 for i in range(fft_dot_number)]
x_real = [0 for i in range(dotNumber)]
x_imag = [0 for i in range(dotNumber)]

general_x = [0 for i in range(dotNumber)]

wpm_cos = 0
wpm_sin = 0

wpn_cos = 0
wpn_sin = 0

fft_mainX = copy(mainX)

start = datetime.now()

for i in range(fft_dot_number):
    for j in range(fft_dot_number):
        wpm_cos = math.cos(4 * math.pi * i * j / fft_dot_number)
        wpm_sin = math.sin(4 * math.pi * i * j / fft_dot_number)
        x_real_first[i] += fft_mainX[2 * j + 1] * wpm_cos
        x_imag_first[i] += fft_mainX[2 * j + 1] * wpm_sin
        x_real_second[i] += fft_mainX[2 * j] * wpm_cos
        x_imag_second[i] += fft_mainX[2 * j] * wpm_sin

    wpn_cos = math.cos(2 * math.pi * i / fft_dot_number)
    wpn_sin = math.sin(2 * math.pi * i / fft_dot_number)

    x_real[i] = x_real_second[i] + x_real_first[i] * wpn_cos - x_imag_first[i] * wpn_sin
    x_imag[i] = x_imag_second[i] + x_imag_first[i] * wpn_cos + x_real_first[i] * wpn_sin

    x_real[i + fft_dot_number] = x_real_second[i] - (x_real_first[i] * wpn_cos - x_imag_first[i] * wpn_sin)
    x_imag[i + fft_dot_number] = x_imag_second[i] - (x_imag_first[i] * wpn_cos + x_real_first[i] * wpn_sin)

    general_x[i] = math.sqrt((x_real[i]) ** 2 + (x_imag[i]) ** 2)
    general_x[i + fft_dot_number] = math.sqrt((x_real[i + fft_dot_number]) ** 2 + (x_imag[i + fft_dot_number]) ** 2)

# for_fft_schema = [[0 for i in range(dotNumber)]for j in range(dotNumber)]

finish = datetime.now()
alg_time = finish - start
print(alg_time)

print(general_x)
plt.plot(general_x)
plt.show()
