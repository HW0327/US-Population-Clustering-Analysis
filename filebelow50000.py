import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

file=np.loadtxt("below50000.txt")

latitude = file[:, 0]

longitude = file[:, 1]
theta = np.linspace(4.5, 175, 15)

# dataset & dataset

n=0
sep=[[np.arccos(np.cos(latitude[i]) * np.cos(latitude[j]) + np.sin(latitude[i]) * np.sin(latitude[j]) * (
                        np.cos(longitude[i]) * np.cos(longitude[j]) + np.sin(longitude[i]) * np.sin(longitude[j]))) * 180 / np.pi
            if i!=j else 0 for j in range(len(latitude))] for i in range(len(latitude))]
sep = sum(sep, [])
finalsep = list(dict.fromkeys(sep))

pdd=[]
nn=0
for a in theta:
    for j in finalsep:
        if abs(a - j) <= 0.2:
            nn += 1
    pdd.append(nn)

dd = [i / (len(latitude) * (len(latitude) - 1)) for i in pdd]


# dataset & random

randomlong = np.random.uniform(low=-176, high=-65, size=len(latitude))

randomlat = np.random.uniform(low=17, high=71, size=len(latitude))
sep2=[[np.arccos(np.cos(latitude[i]) * np.cos(randomlat[j]) + np.sin(latitude[i]) * np.sin(randomlat[j]) * (
                        np.cos(longitude[i]) * np.cos(randomlong[j]) + np.sin(longitude[i]) * np.sin(randomlong[j]))) * 180 / np.pi
            if i!=j else 0 for j in range(len(latitude))] for i in range(len(latitude))]
sep2 = sum(sep2, [])
finalsep2 = list(dict.fromkeys(sep2))

pdr=[]
nn=0
for a in theta:
    for j in finalsep2:
        if abs(a - j) <= 0.1:
            nn += 1
    pdr.append(nn)

dr = [i / (len(latitude) ** 2) for i in pdr]


# random & random
sep3=[[np.arccos(np.cos(randomlat[i]) * np.cos(randomlat[j]) + np.sin(randomlat[i]) * np.sin(randomlat[j]) * (
                        np.cos(randomlong[i]) * np.cos(randomlong[j]) + np.sin(randomlong[i]) * np.sin(randomlong[j]))) * 180 / np.pi
            if i!=j else 0 for j in range(len(latitude))] for i in range(len(latitude))]
sep3 = sum(sep3, [])
finalsep3 = list(dict.fromkeys(sep3))

prr=[]
nn=0
for a in theta:
    for j in finalsep3:
        if abs(a - j) <= 0.2:
            nn += 1
    prr.append(nn)

rr = [i / (len(latitude) * (len(latitude) - 1)) for i in prr]

# correlation function
crr = [(dd[i] - 2 * dr[i] + rr[i]) / rr[i] for i in range(len(theta))]

print("correlation", crr)
error = [0.13700192407249763, 0.13497888760108809, 0.11201244458531335, 0.1160944325797594, 0.12381937598227592,
         0.13438040734033188, 0.1220633106012544, 0.12232799484077335, 0.1112603888018927, 0.0957861369650432,
         0.08650019586232945, 0.08071675943631047, 0.07810351472617054, 0.07770942628972552, 0.07892636058862758]




plt.errorbar(theta, crr, yerr=error, fmt='.')
f = CubicSpline(theta, crr, bc_type='natural')
x_new = np.linspace(0, 180, 100)
y_new = f(x_new)
plt.plot(x_new, y_new, 'b')
plt.title("Two-Point Correlation Function")
plt.xlabel("\u03F4deg(\u00B0)")
plt.ylabel("\u03BE(\u03F4)")
plt.show()

