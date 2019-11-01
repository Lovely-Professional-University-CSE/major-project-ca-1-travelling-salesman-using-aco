# major-project-ca-1-travelling-salesman-using-aco
major-project-ca-1-travelling-salesman-using-aco created by GitHub Classroom

Travelling salesman problem (TSP) consists of finding the shortest route in complete weighted graph G with n nodes 
and n(n-1) edges, so that the start node and the end node are identical and all other nodes in this tour are visited exactly once. 

The most popular practical application of TSP are:
regular distribution of goods or resources, finding of the shortest of costumer servicing route, planning bus lines etc., 
but also in the areas that have nothing to do with travel routes.

The Travelling Salesman Problem is one of the best known NP-hard problems, which means that there is no exact algorithm 
to solve it in polynomial time. The minimal expected time to obtain optimal solution is exponential. So, for that reason, we
usually use heuristics to help us to obtain a “good” solution. Many algorithms were applied to solve TSP with more or less success.
There are various ways to classify algorithms, each with its own merits. The basic characteristic is the ability to reach optimal 
solution: exact algorithms or heuristics.

--------------------PROBABILITY OF AN ANT TO FOLLOW A PATH IS:

probability(i,j) = ( (tau(i,j))^alpha * (eta(i,j))^beta )/sigma((tau(i,j))^alpha * (eta(i,j))^beta)

(in the code):

sum_pheromene_eta =  np.sum((((pheromene)**alpha)*((eta)**beta)))

prob = (((pheromene[i][j])**alpha)*((eta[i][j])**beta))/(sum_pheromene_eta)

tau(i,j) is the pheromene on the node (i,j)

eta(i,j) is the viibility or desirability on the the node(i,j) which is equal to (1/distance(i,j))

alpha is the parameter to control the influence of tau(i,j)

beta is is a parameter to control the influence of eta(i,j)

--------------------PHEROMENE UPDATION ON THE NODE:

tau(i,j) = (1-rho)*tau(i,j) + sigma(delta(tau(i,j)))

(in the code)
 sum_pheromene[axis_list[i-1]][axis_list[i]] = sum_pheromene[axis_list[i-1]][axis_list[i]] 
        + (pheromene[axis_list[i-1]][axis_list[i]]/total_distance)
 
 pheromene[axis_list[i-1]][axis_list[i]] = (1 - rho)*pheromene[axis_list[i-1]][axis_list[i]] 
        + sum_pheromene[axis_list[i-1]][axis_list[i]]       
        
rho is the pheromene evapouration on the node travelled by the ant

During pheromone update step, pheromone is evaporated and then deposited. Pheromone evaporation coefficient
0 < rho < 1 determines how quick ants can forget found paths and avoid unlimited pheromone accumulation
 

