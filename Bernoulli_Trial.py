import random

def BernoulliTrial(n,p):
	BernTrial = []
	for i in range(n):
		if random.random() <= p:
			BernTrial.append(1)
		else:
			BernTrial.append(0)
	
	return BernTrial
	
n = int(input("Pleasure input the number of simulations desired: "))
p = float(input("Please input the theoretical chance of success: "))

print float(sum(BernoulliTrial(n,p)))/n

#This simple notebook outlines a method for simulating a sequence of i.i.d. Bernoulli trials,
#with user specification on the number of trials and on the theoretical rate of success
#governing the Bernoulli distribution.  Quite easy to do the same for any sequence of 
#i.i.d. random variables with discrete underlying distribution. Should consider writing
#a program that has the user input a discrete distribution as a dictionary, and provides 
#the same sort of random sample generation as in this case.