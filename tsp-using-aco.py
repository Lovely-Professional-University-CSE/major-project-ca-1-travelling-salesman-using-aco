import numpy as np
import math 
import matplotlib.pyplot as plt

cities_list = ['MUMBAI','NEW DELHI','KOLKATA','CHENNAI','BANGLORE','HYDRABAD','JAIPUR','AHMEDABAD','CHANDIGARH','KOCHI']
n = np.random.randint(2,11)      #random function is used to randomly select the cities from the list
cities = cities_list[:n]

x = []   #it stores the coordinates of the cities
y = []

for i in range(n):
    x_axis = np.random.randint(1,100)          #this is used for the random assignment of the coordinates of each city
    y_axis = np.random.randint(1,100)
    x.append(x_axis)         #appending the values of x_axis and y_axis in x,y
    y.append(y_axis)
    
print(x)
print(y)

print()
distance = []         #empty list distance created 

# this code calculates the distance between each city using euclidean distance formula 
for i in range(0,len(cities)):
    for j in range(0,len(cities)):
        distance.append((((x[j]-x[i])**2 + (y[j] - y[i])**2)**0.5))   #euclidean distance formula
distance = np.array(distance)
distance = np.reshape(distance,(n,n))           # reshape is used to create a 2d array and the distances between each cities
print('distance between all the nodes: \n',distance)

pheromene = np.ones((n,n))         #pheromene initialization with function np.ones (np.ones assign 1 to each edges)

sum_pheromene = np.zeros((n,n))

alpha = 1   # alpha is the parameter to control the influence of pheromene
beta = 2    #beta is the paramenter to control the influence of visibility

eta = np.zeros((n,n))    #initization of eta
rho = 0.2     #this is the pheromene evapouration

# Pheromone evaporation coefficient 0 < rho < 1 determines how quick ants can forget found paths 
#and avoid unlimited pheromone accumulation

number_of_ants = 10      

total_distance = []          #this list is used to append the distances travelled by each ant

__ = 1
while(__ <= number_of_ants):
#initial pheromene
#------------------------------------------------probabiltiy--------------------------------------------
#this code is used to calculate the eta(visibility of the edges between the cities)

    for i in range(0,n):
        for j in range(0,n):
            if(distance[i][j] == 0):
                eta[i][j] = 0
            else:
                eta[i][j] = (1/distance[i][j])    #visibility formula is 1/distance between the two cities

    sum_pheromene_eta =  np.sum((((pheromene)**alpha)*((eta)**beta)))

#-------------------------------------------probability of path i,j----------------------------------------
#this function calculcates the probability of choosing the next city from the current city 

    def probability(alpha,beta,i,j):
        prob = (((pheromene[i][j])**alpha)*((eta[i][j])**beta))/(sum_pheromene_eta)
        return prob
        
#-------------------------------------------probability of everynode------------------------------------------        
# this code is used to append the probability of the path

    print()
    prob = []   #list to store the probability of the path
    for i in range(0,n):
        for j in range(0,n):
            temp = 0
            temp = probability(1,2,i,j)
            prob.append(temp)

    prob = np.array(prob)
    prob = prob.reshape(n,n)
    print('probability of all the node: \n',prob)
    
    #as we move from the current node the probability changes as the pheromene is updates between the cities

#------------------------------------------------cumulative probability---------------------------------------------
    temp = 0
    axis = 0 
    
    a = [x[0]]        #a is the list used to append the x coordinates of the next cities travelled by the ant
    b = [y[0]]         #b is the list to append the y coordinates

    axis_list = [0]   #this list stores the position of cities travelled by the salesman
    
    _ = 0               
    while(_ <= n):        #this loop calculates the axis and the coordinates of sequence that the salesman uses to travel from
        temp = 0          #one city to other
        prob1 = []
        for i in range(n):
            temp = temp + prob[(axis+1)-1:(axis+1)][0][i]   #this code is to calculate the probability of each city from the initial city
            prob1.append(temp)                              #temp is used to calaculate the cumulative probability
        random_nno = np.random.uniform(0,np.max(prob1))     #random function is an approach to select the next 
        temp = 0
        for i in range(n):
            if(prob1[i] > random_nno):
                seal_prob = prob1[i]                        #the next bigger value to random number in prob1 will be the next city from the current
                break

        c = np.where(prob1 == seal_prob)                     #c stores the index of the next city
        axis = c[0][0]

        if(np.isin(axis,axis_list) == False):                #append the axis in axis_list only when its not present in axis_list
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
    
    # this code calculates the total distance travelled by the salesman
    temp = 0
    for i in range(1,len(a)):
        temp = temp + ((a[i] - a[i-1])**2 + (b[i] - b[i-1])**2)**0.5    #the distance is calculated using euclidean disance formula

    for i  in range(len(axis_list)):
        print('-',cities[axis_list[i]],end = '')
    print('- MUMBAI')
    print()
    
    total_distance1 = temp
    print('---------------------------total distance-----------------------------',total_distance1)
    total_distance.append(total_distance1)  #the distances travelled by each sales is appended in list total_distance
    
    # this codes plot the graph of the cities travelled by the salesman
    x1_axis = []
    y1_axis = []
    for i in range(len(axis_list)):
        x1_axis.append(x[axis_list[i]])
        y1_axis.append(y[axis_list[i]])
        #print()

        plt.scatter(x1_axis,y1_axis,s = 40)    #display the points of the city 
        plt.text(x[i] ,y[i] ,cities[i],fontsize = 10)   #displays the name of the city 
        plt.plot([x1_axis[i-1],x1_axis[i]],[y1_axis[i-1],y1_axis[i]],linewidth = 0.7);   #connects the edges of the cities 
    
    plt.plot([x1_axis[n-1],x1_axis[0]],[y1_axis[n-1],y1_axis[0]],linewidth = 0.7); 
    plt.xlim(0,100)
    plt.ylim(0,100)
    plt.show()


#this codes updates the pheromene of the edges treavelled by the sales man 
#from city(axis_list[i-1]) to city(axis_lis[i])

    for i in range(1,len(axis_list)):
        
        #sum_pheromene is  the summition of all the pheromenes 
        
        sum_pheromene[axis_list[i-1]][axis_list[i]] = sum_pheromene[axis_list[i-1]][axis_list[i]] 
        + (pheromene[axis_list[i-1]][axis_list[i]]/total_distance)
        
        #the below code updates the pheromene of the edge treavelled by the salesman 

        pheromene[axis_list[i-1]][axis_list[i]] = (1 - rho)*pheromene[axis_list[i-1]][axis_list[i]] 
        + sum_pheromene[axis_list[i-1]][axis_list[i]]

    pheromene[axis_list[n-1]][axis_list[0]] = (1 - rho)*pheromene[axis_list[n-1]][axis_list[0]] + sum_pheromene[axis_list[n-1]][axis_list[0]]

    print(pheromene)

    __ += 1
    
print()
print(total_distance)
print(' the minimum distance is:',np.min(total_distance))  #find the shortest and the most minimal distance travelled by the sales 
                                                           # traversing all the cities
