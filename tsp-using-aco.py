import numpy as np
import math 
import matplotlib.pyplot as plt

cities = np.array(['A','B','C','D','E'])
n = np.random.choice(cities)

#---------------------------------distance calculation of every node----------------------------
x = []
y = []

for i in range(5):
    x_axis = np.random.randint(1,100)
    y_axis = np.random.randint(1,100)
    x.append(x_axis)
    y.append(y_axis)
    
print(x)
print(y)

print()
distance = []
for i in range(0,5):
    for j in range(0,5):
        distance.append((((x[j]-x[i])**2 + (y[j] - y[i])**2)**0.5))
distance = np.array(distance)
distance = np.reshape(distance,(5,5))
print(distance)

#----------------value initialisation-------------------------
pheromene = np.ones((5,5))
sum_pheromene = np.zeros((5,5))
epoch = 100
alpha = 1
beta = 2

eta = np.zeros((5,5))
rho = 0.2
cumulative_lst = []

a = [x[0]]
b = [y[0]]

axis_list = [0]
total_distance = []
number_of_ants = 10

