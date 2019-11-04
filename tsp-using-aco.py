import numpy as np
import math 
import matplotlib.pyplot as plt

cities_list = ['MUMBAI','NEW DELHI','KOLKATA','CHENNAI','BANGLORE','HYDRABAD','JAIPUR','AHMEDABAD','CHANDIGARH','KOCHI']
n = np.random.randint(2,11)
cities = cities_list[:n]

x = []
y = []

for i in range(n):
    x_axis = np.random.randint(1,100)
    y_axis = np.random.randint(1,100)
    x.append(x_axis)
    y.append(y_axis)
    
print(x)
print(y)

print()
distance = []
for i in range(0,len(cities)):
    for j in range(0,len(cities)):
        distance.append((((x[j]-x[i])**2 + (y[j] - y[i])**2)**0.5))
distance = np.array(distance)
distance = np.reshape(distance,(n,n))
print('distance between all the nodes: \n',distance)

pheromene = np.ones((n,n))

sum_pheromene = np.zeros((n,n))
epoch = 100
alpha = 1
beta = 2

eta = np.zeros((n,n))
rho = 0.2
cumulative_lst = []

a = [x[0]]
b = [y[0]]

axis_list = [0]
number_of_ants = 10

total_distance = []

__ = 1
while(__ <= number_of_ants):
#initial pheromene
#------------------------------------------------probabiltiy--------------------------------------------

    for i in range(0,n):
        for j in range(0,n):
            if(distance[i][j] == 0):
                eta[i][j] = 0
            else:
                eta[i][j] = (1/distance[i][j]) 

    sum_pheromene_eta =  np.sum((((pheromene)**alpha)*((eta)**beta)))

#-------------------------------------------probability of path i,j----------------------------------------
    def probability(alpha,beta,i,j):
        prob = (((pheromene[i][j])**alpha)*((eta[i][j])**beta))/(sum_pheromene_eta)
        return prob
        
#-------------------------------------------probability of everynode------------------------------------------        
    print()
    prob = []
    for i in range(0,n):
        for j in range(0,n):
            temp = 0
            temp = probability(1,2,i,j)
            prob.append(temp)

    prob = np.array(prob)
    prob = prob.reshape(n,n)
    print('probability of all the node: \n',prob)

#------------------------------------------------cumulative probability---------------------------------------------
    temp = 0
    axis = 0 
    
    cumulative_lst = []
    
    a = [x[0]]
    b = [y[0]]

    axis_list = [0]
    
    _ = 0
    while(_ <= n):
        temp = 0
        prob1 = []
        for i in range(n):
            temp = temp + prob[(axis+1)-1:(axis+1)][0][i]
            prob1.append(temp)   
        random_nno = np.random.uniform(0,np.max(prob1))
        temp = 0
        for i in range(n):
            if(prob1[i] > random_nno):
                seal_prob = prob1[i]
                break

        c = np.where(prob1 == seal_prob)
        axis = c[0][0]

        if(np.isin(axis,axis_list) == False):
            axis_list.append(axis)
            a.append(x[axis])
            b.append(y[axis])
            _ += 1

            if(len(axis_list) == n):
                break
        else:
            continue
    print('x axis value',a)
    print('y axis value',b)

# ---------------------------------------total path distance---------------------------------------------
    temp = 0
    for i in range(1,len(a)):
        temp = temp + ((a[i] - a[i-1])**2 + (b[i] - b[i-1])**2)**0.5

    for i  in range(len(axis_list)):
        print('-',axis_list[i],end = '')
    print()
    total_distance1 = temp
    print('---------------------------total distance-----------------------------',total_distance1)
    total_distance.append(total_distance1)
    
    
    x1_axis = []
    y1_axis = []
    for i in range(len(axis_list)):
        x1_axis.append(x[axis_list[i]])
        y1_axis.append(y[axis_list[i]])
        #print()

        plt.scatter(x1_axis,y1_axis,s = 40)
        plt.text(x[i] ,y[i] ,cities[i],fontsize = 10)
        plt.plot([x1_axis[i-1],x1_axis[i]],[y1_axis[i-1],y1_axis[i]],linewidth = 0.7);
    
    plt.plot([x1_axis[n-1],x1_axis[0]],[y1_axis[n-1],y1_axis[0]],linewidth = 0.7); 
    plt.xlim(0,100)
    plt.ylim(0,100)
    plt.show()


    for i in range(1,len(axis_list)):
        sum_pheromene[axis_list[i-1]][axis_list[i]] = sum_pheromene[axis_list[i-1]][axis_list[i]] 
        + (pheromene[axis_list[i-1]][axis_list[i]]/total_distance)

        pheromene[axis_list[i-1]][axis_list[i]] = (1 - rho)*pheromene[axis_list[i-1]][axis_list[i]] 
        + sum_pheromene[axis_list[i-1]][axis_list[i]]

    pheromene[axis_list[n-1]][axis_list[0]] = (1 - rho)*pheromene[axis_list[n-1]][axis_list[0]] + sum_pheromene[axis_list[n-1]][axis_list[0]]

    print(pheromene)

    __ += 1
    
print()
print(total_distance)
print(' the minimum distance is:',np.min(total_distance))
