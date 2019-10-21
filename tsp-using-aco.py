import numpy as np
import math 
import matplotlib.pyplot as plt

cities = np.array(['A','B','C','D','E'])
n = np.random.choice(cities)

x = []
y = []

for i in range(5):
    x_axis = np.random.randint(1,100)
    y_axis = np.random.randint(1,100)
    x.append(x_axis)
    y.append(y_axis)
    
    plt.scatter(x_axis,y_axis,s = 40)
    plt.text(x_axis,y_axis,cities[i],fontsize = 12)
    #plt.annotate(cities,plt.scatter(x_axis,y_axis,s = 1
#plt.xlim(0,10)
#plt.ylim(0,10)
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
        #if((i) == (j)):
            #continue
        #else:
        distance.append((((x[j]-x[i])**2 + (y[j] - y[i])**2)**0.5))
distance = np.array(distance)
distance = np.reshape(distance,(5,5))
distance
#print(count)
#for j in range(1,len(cities)):
#        b.append((((x[j]-x[0])**2 + (y[j] - y[0])**2)**0.5))
#print(b)
