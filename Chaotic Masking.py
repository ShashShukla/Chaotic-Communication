'''
Chaotic Binary Shift Keying

Author: Shashwat Shukla
Date: 28th March 2018
'''
# Import libraries
import numpy as np
import scipy.integrate as integrate
import scipy.signal as signal
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# The message signal being sent
def m(t):
    # return (t > 10) * 1e-3 * signal.square(100 * t)
    return (t > 10) * 1e-3 * np.sin(100 * t)

# The Difference Equations governing the operation of the circuit
def dH_dt(H, t=0):
    return np.array([16 * (H[1] - H[0]), 45.6 * H[0] - H[1] - 20.0 * H[0] * H[2], 5 * H[0] * H[1] - 4 * H[2],
                     16 * (H[4] - H[3]), 45.6 * (H[0] + m(t)) - H[4] - 20.0 * (H[0] + m(t)) * H[5], 5 * (H[0] + m(t)) * H[4] - 4 * H[5]])

# Simulation Time Steps
T = 20
t = np.linspace(0, T, 1000 * T)

# Initial conditions
H0 = [3, 0.2, 0.3, 3, 0.0, 0.0]

# Simulate the set of difference equations
H, infodict = integrate.odeint(dH_dt, H0, t, full_output=True)

# print infodict['message'] # Print info about simulation

# Trajectory of the transmitter vector
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(H[:, 0], H[:, 1], H[:, 2])
# plt.show()

# Trajectory of the error vector
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(H[:, 3] - H[:, 0], H[:, 4] - H[:, 1], H[:, 5] - H[:, 2])
plt.show()

# The transmitted signal
plt.plot(t[12e3:14e3], m(t[12e3:14e3]))
plt.show()

# The recovered signal
plt.plot(t[12e3:14e3], (m(t[12e3:14e3]) + H[12e3:14e3, 0] - H[12e3:14e3, 3]))
plt.show()
