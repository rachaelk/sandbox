import random
import matplotlib.pyplot as plt
import math

###   Creates a Brownian sample path on the interval [0,1].   ###
###   Input: natural n, giving the partition of [0,1] into n equally sized buckets.   ###
###   Return: a list encoding the sample path evaluated at each of the n partition points.   ###

def BrownianPath(n):
	realization = [0]
	
	for i in range(n):
		realization.append(realization[i]+random.normalvariate(0,math.sqrt(1/float(n))))
		
	return realization
	
###   Numerically integrates the function f(t) = t against an input integrator, on the interval [0,1].   ###
###   Input: list A, thought of as evaluations of the integrator at partition points mentioned above.   ###
###   Return: total integral.  ###

###   Using left-handed evaluation points for f; this becomes quite important for random integrands.   ###

	
def NumInt(A):
	
	total = 0
	
	for i in range(len(A)-1):
		total = total + (i/float(len(A)-1))*(A[i+1] - A[i])
		
	return total
	
	
m = 1000

### Just a quick plot of Brownian sample paths, to check for obvious semantic errors. ###

LOMO = range(m+1)
partition = [x/float(m) for x in LOMO]

plt.plot(partition,BrownianPath(m), '--', partition, BrownianPath(m), 'k', partition, BrownianPath(m))
plt.show()

### Compute a bunch of sample integrals, collected into outcomes list. ###

outcomes = []
for i in range(1000):
	outcomes.append(NumInt(BrownianPath(m)))
	
#print outcomes

### Wiener integral should produce a normal random variable, with mean 0 and standard deviation the L^2 norm. ###
### In our example, f(t) = t, ought to obtain a Normal(0, 1/sqrt(3)) random variable. ###

plt.hist(outcomes, 50)
plt.show()











	
	