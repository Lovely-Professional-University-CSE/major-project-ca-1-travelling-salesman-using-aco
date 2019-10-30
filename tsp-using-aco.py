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
    
    plt.scatter(x_axis,y_axis,s = 40)
    plt.text(x_axis,y_axis,cities[i],fontsize = 12)
print(x)
print(y)

for i in range(1,5):
    for j in range(1,5):
        plt.plot([x[i-1],x[j]],[y[i-1],y[j]],linewidth = 0.7);
plt.xlim(0,100)
plt.ylim(0,100)
plt.plot([x[0],x[4]],[y[0],y[4]]);

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
number_of_ants = 10

#-----------------------path i,j probability--------------------
for i in range(0,5):
        for j in range(0,5):
            if(distance[i][j] == 0):
                eta[i][j] = 0
            else:
                eta[i][j] = (1/distance[i][j]) 

    sum_pheromene_eta =  np.sum((((pheromene)**alpha)*((eta)**beta)))

def probability(alpha,beta,i,j):
        prob = (((pheromene[i][j])**alpha)*((eta[i][j])**beta))/(sum_pheromene_eta)
        return prob
    
prob = []
    for i in range(0,5):
        for j in range(0,5):
            temp = 0
            temp = probability(1,2,i,j)
            prob.append(temp)

    prob = np.array(prob)
    prob = prob.reshape(5,5)
    print(prob)
    
