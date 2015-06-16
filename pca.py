import numpy as np
#obs matrix,  
obs  = np.matrix('-7,-7,-9,-10 ;  -7.3,-7.3,-9.4,-10.1 ;  -10,-10,-10,-3')
dim  = obs.shape[1]
wier = obs.shape[0]

# _______1_______
#means vector  
means = np.zeros((dim, 1), dtype=np.float64)

for i in range(0,dim):
	means[i] = np.mean(obs.T[i])
	
#________2__________
#Compute the Scatter Matrix
scatt = np.zeros((dim, dim), dtype=np.float64)
	
for k in range(0,dim):

	for w in range(0,wier):
		for i in range(0,dim):	
			scatt[w,k] += (obs[w,k]-means[k,0])*(obs[w,k]-means[k,0])
		
			
#________3____________
#Compute eigenvectors and corresponding eigenvalues
