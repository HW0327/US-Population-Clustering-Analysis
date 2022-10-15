import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

file=np.loadtxt("above200000.txt")

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
        if abs(a - j) <= 0.5:
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
        if abs(a - j) <= 0.25:
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
        if abs(a - j) <= 0.5:
            nn += 1
    prr.append(nn)

rr = [i / (len(latitude) * (len(latitude) - 1)) for i in prr]

# correlation function
crr = [(dd[i] - 2 * dr[i] + rr[i]) / rr[i] for i in range(len(theta))]

print("correlation", crr)
error = [0.1743145169711197, 0.1725728326473308, 0.16282323438197366, 0.157774263356749, 0.15598477119647287,
         0.13712343527436707, 0.13334343449557132, 0.12857873206923634, 0.11424460767845593, 0.09590431949911567,
         0.06544653341423588, 0.09203082369158405, 0.07732729398798673, 0.0855322112023551, 0.08421155398877947]



plt.errorbar(theta, crr, yerr=error, fmt='.')
f = CubicSpline(theta, crr, bc_type='natural')
x_new = np.linspace(0, 180, 100)
y_new = f(x_new)
plt.plot(x_new, y_new, 'b')
plt.title("Two-Point Correlation Function")
plt.xlabel("\u03F4deg(\u00B0)")
plt.ylabel("\u03BE(\u03F4)")
plt.show()
