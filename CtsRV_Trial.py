import random
import math

#Yesterday created a Bernoulli trial simulation, whereby the user could input the Bernoulli parameter
#and generate any number of realizations of i.i.d. random variables having this common distribution.
#Clearly the method employed generalizes to any discrete distribution...simple to write a program
#generating an i.i.d. sequence of such r.v.'s. 

#For other sorts of random variables, e.g. continuous r.v., doesn't seem as easy to convert from 
#U ~ Unif(0.1) to find i.i.d. sequence realizations.  Trick is to recognize that, given a distribution
#function F, the pullback X = F^{-1}(U), regarded as a random variable X: (0,1) -> R, has distribution
#F, as F_{X}(a) = P{x: X(x) <= a} = P{x: F^{-1}(U(x)) <= a} = P{x: F^{-1}(x) <= a} = P{x: x <= F(a)}
# = F(a), where we used monotonicity of the cdf.

#In the case considered above, the exponential, we have F(x) = 1 - e^{-param*x}, so that F^{-1}(x) =
# ln(1-x)/(-param).  As U ~ Unif(0,1) gives 1-U of the same distribution, we simplify this a bit.
#Again, same game.  User inputs number of trials and a decay parameter, and is able to view the 
#resulting sample.

def ExponentialTrial(n, param):
	ExpTrial = []
	for i in range(n):
		ExpTrial.append(math.log(random.random())/(-param))
	return ExpTrial
	
n = int(input("Please input the desired number of trials: "))
param = float(input("Please input the theoretic decay parameter, lambda, governing the distribution: "))

print sum(ExponentialTrial(n,param))/len(ExponentialTrial(n,param))

#Function outputs the entire sample random vector, while providing the experimental mean.  Note that, given
#a decay parameter lambda, the mean ought to be 1/lambda.

#Gaussian/normal oughyt to be a bit more difficult...the cdf is not obvious whatsoever.  The trick is to 
#consider a pair (X,Y) ~ Norm(0,1), and study the distributions of their polar expression (R^2,theta)
#Clearly the polar random variables are independent; even more, theta ~ Unif(0,2pi).  It turns out that 
#R^2 = X^2 + Y^2 has Chi-squared(2) distribution, which is just Exp(1/2).  So, we simulate a pair of 
#Unif(0,1) random variables, and convert them into Exp(1/2), Unif(0,2pi), then convert from polar to rectangular
#to rectangular to retrieve our pair of independent, Normal(0,1) random variables.  Conversion to 
#Normal(mu, sigma^2) is straightforward; namely, if X ~ Normal(0,1), then Y = aX + b ~ Normal(b, a^2).



def NormalTrial(m,mu,sigma):

	NormTrial = []
	
	for i in range(m):
			r_squared = -2*math.log(random.random())
			theta = 2*math.pi*random.random()
			
			NormTrial.append(sigma*math.sqrt(r_squared)*math.cos(theta) + mu)
			NormTrial.append(sigma*math.sqrt(r_squared)*math.sin(theta) + mu)
			
	return NormTrial
		

m = int(input("Please input the desired number of trials: "))
mu = float(input("Please input the theoretic mean, mu, governing the distribution: "))		
sigma = float(input("Please input the theoretic stdev, sigma, governing the distribution: "))	

print NormalTrial(m,mu,sigma)
print "\n \n"
print sum(NormalTrial(m,mu, sigma))/len(NormalTrial(m,mu, sigma))


#Should compare the performance of these functions with those built in to the random module.

			