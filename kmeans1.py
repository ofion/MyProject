# K - number of obs
# N - number of clusters
# dim - number of variables
# eucl dist
import numpy as np
import math as ma
import random as ra	
import time  

a = time.clock()
#classification FUNCTION
def clasify(K, N, dim, obs, sampl):    
	clus = np.zeros((K, 1))  # [[0 for x in xrange(1)] for y in xrange(K)]
	bin  = np.zeros((N, K))

#distance matrix 
	dist = np.zeros((K, N), dtype=np.complex128)
		
	for i in range(0, N): 
    
		for j in range(0, K): 
		
		  zero = np.complex128(0)
		  
		  for h in range(0, dim): 
			
			zero += (obs[j, h] - sampl[i, h])**2  
		  
		  dist[j,i] = ma.sqrt(zero)
		  
		
		  
# classification
	for i in range(0, K):
		
		for j in range(0, N):
		
			if dist[i,j] == min(dist[i,]):
				clus[i,0] = j 
				
	return clus   

	
### new centroids
def midds(N, dim, K, clus, obs):
  
	midds = np.zeros((N, dim), dtype=np.complex128)
	
	for j in range(0, dim):  
		for h in range(0, N):
			num = np.complex128(0)
			sum  = np.complex128(0) 
			
			for i in range(0,K): 			
				if clus[i,0] == h:
					num += 1
					sum += obs[i,j]
			if num == 0: 
				num = -1
				
			midds[h,j]	= sum/num
			
	return midds

#########################################################################################
#obs matrix,  
dim  = 4
N    = 3        #
K = 6
obs = np.matrix('-7,-7,-9,-10 ;  -7.3,-7.3,-9.4,-10.1 ;  -10,-10,-10,-3 ;  7,7,7,8 ;  10,13,13,10 ; 13,13,10,10')
# pick random N points 
sampl = obs[ra.sample(range(0,K),N),]
#sampl = np.matrix('-7,-7,-9,-10 ; 13,13,10,10')

# Classification for chosen points
clus = clasify(K, N, dim, obs, sampl)
centroids = midds(N, dim, K, clus, obs)

# calculate new midds
clus2 = clasify(K, N, dim, obs, centroids)
p = 0
vec = np.zeros((K,1))

for i in range(0,K):
	vec[i,0] = clus[i,0] - clus2[i,0]
	if vec[i,0] != 0:
		p = 1
		break

r = 0

while p:
	r+=1
	clus = clus2
	centroids = midds(N, dim, K, clus, obs)
	clus2 = clasify(K, N, dim, obs, centroids)
	p = 0
	for i in range(0,K):
		
		if clus[i,0] - clus2[i,0] != 0:
			p = 1
			break

			
b = time.clock()
print clus2
print "Secs: ", b-a
	






















