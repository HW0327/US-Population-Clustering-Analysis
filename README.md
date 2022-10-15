<!--Heaadings-->
# ASTRO 410 Final Project--Haoyu Wang
## Introduction
### For the final project, I did research on US population clustering. I calculated two-point correlation funuction for each population group, and used the cubic natural spline to fit the plots of correlation function graphs. Meanwhile, I calculated correlation function for population of California and Florida state to get the clustering bias.


## Installation
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
```

## Usage
### To get the graph of correlation function for group of below 50,000, go to the file's directory and input the code below in you terminal:
```sh
py filebelow50000.py
```
### To get the graph of correlation function for group of 50,000 to 80,000, go to the file's directory and input the code below in you terminal:
```sh
py file50000to80000.py
```
### To get the graph of correlation function for group of 80,000 to 100,000, go to the file's directory and input the code below in you terminal, <strong> due to the small amount of data, the system may report an error, and the image will come out after a few attempts:</strong>
```sh
py file80000to100000.py
```
### To get the graph of correlation function for group of 100,000 to 200,000, go to the file's directory and input the code below in you terminal. <strong> If the image doesn't look right, please try few more attempts:</strong>
```sh
py file100000to200000.py
```
### To get the graph of correlation function for group of above 200,000, go to the file's directory and input the code below in you terminal. <strong> If the image doesn't look right, please try few more attempts:</strong>
```sh
py fileabove200000.py
```
### To get the graph of correlation function for population of California state and bias, go to the file's directory and input the code below in you terminal. 
```sh
py CA_population.py
```
### To get the graph of correlation function for population of Florida state and bias, go to the file's directory and input the code below in you terminal:
```sh
py FL_population.py
```
