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

turning_coefs_real = [[0 for j in range(dotNumber)] for i in range(dotNumber)]
turning_coefs_imag = [[0 for j in range(dotNumber)] for i in range(dotNumber)]

start = datetime.now()
for i in range(dotNumber):
    for j in range(dotNumber):
        turning_coefs_real[i][j] = round(math.cos((2 * math.pi / dotNumber) * ((i * j) % dotNumber)))
        turning_coefs_imag[i][j] = round(- math.sin((2 * math.pi / dotNumber) * ((i * j) % dotNumber)))

print(turning_coefs_real)
print(turning_coefs_imag)

turning_coefs_real = np.array(turning_coefs_real)
turning_coefs_imag = np.array(turning_coefs_imag)

fft_mainX = copy(mainX)

mainX = np.array(mainX)

mainX = np.transpose(mainX)

dft_magnitude_real = turning_coefs_real.dot(mainX)
dft_magnitude_imag = turning_coefs_imag.dot(mainX)

# print(dft_magnitude_real)
# print(dft_magnitude_imag)

for_schema = [math.sqrt(dft_magnitude_imag[i] ** 2 + dft_magnitude_real[i] ** 2) for i in range(dotNumber)]

finish = datetime.now()
alg_time = finish - start
print(alg_time)
# print(for_schema)
# print(turning_coefs_real)
# print(turning_coefs_imag)

plt.plot(for_schema)
plt.show()