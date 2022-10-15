import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

file=np.loadtxt("100000to200000.txt")

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
        if abs(a - j) <= 0.3:
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
        if abs(a - j) <= 0.15:
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
        if abs(a - j) <= 0.3:
            nn += 1
    prr.append(nn)

rr = [i / (len(latitude) * (len(latitude) - 1)) for i in prr]

# correlation function
crr = [(dd[i] - 2 * dr[i] + rr[i]) / rr[i] for i in range(len(theta))]

print("correlation", crr)
error = [0.165733996605092, 0.15790476501639655, 0.15834577595154314, 0.15506245405383365, 0.15416158836742118,
         0.15736612414784852, 0.15399061371348807, 0.1367844971845059, 0.11774000014392326, 0.10085161446779001,
         0.10291482690943077, 0.09465803342757192, 0.09649269048657277, 0.09347015186939932, 0.09700485328113063]


plt.errorbar(theta, crr, yerr=error, fmt='.')
f = CubicSpline(theta, crr, bc_type='natural')
x_new = np.linspace(0, 180, 100)
y_new = f(x_new)
plt.plot(x_new, y_new, 'b')
plt.title("Two-Point Correlation Function")
plt.xlabel("\u03F4deg(\u00B0)")
plt.ylabel("\u03BE(\u03F4)")
plt.show()
