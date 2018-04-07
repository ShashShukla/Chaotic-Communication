'''
Chaotic Digital Encoding

Author: Shashwat Shukla
Date: 2nd April 2018
'''
# Import libraries
import numpy as np
import matplotlib.pyplot as plt

# Define parameters
m = 8
N = 2**m
k1 = 3
G = 2
k2 = 7
num_iter = 100
a = 2
b = 3

# Circular left-shift
def lcirc(n):
    x = (n + k1) % N
    x = (G * x)
    s = int(x >= N)
    x = x % N
    x = (x + k2 * s) % N
    return x

u = np.zeros(num_iter + 2).astype(int)  # Message sequence

for i in range(num_iter):
    u[i + 2] = i % 10  # Sawtooth function

e1 = np.zeros(num_iter + 2).astype(int)  # Intermittent input sequence
e = np.zeros(num_iter + 2).astype(int)  # Transmitted sequence
e2 = np.zeros(num_iter + 2).astype(int)  # Intermittent output sequence
y = np.zeros(num_iter + 2).astype(int)  # Decoded output sequence

for i in range(2, num_iter + 2):
    e1[i] = (u[i] + e1[i - 1] + lcirc(e1[i - 2])) % N
    e[i] = (e1[i] + a * e1[i - 1] + b * lcirc(e1[i - 2])) % N
    e2[i] = (e[i] - a * e2[i - 1] - b * lcirc(e2[i - 2])) % N
    y[i] = (e2[i] - e2[i - 1] - lcirc(e2[i - 2])) % N

for i in range(num_iter):
    print u[i], y[i]


plt.plot(e)
plt.show()

cor = np.correlate(e - np.mean(e), e - np.mean(e), mode='full')
cor = cor[cor.size / 2:]
plt.plot(cor / cor[0])
plt.show()

plt.plot(u)
plt.show()
