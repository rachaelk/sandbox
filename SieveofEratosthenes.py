import math

#######################################
# FUNCTION: IsPrime
# PARAMETERS: 
# 				n ~ any natural number greater than two
# 
# PURPOSE: 
#	This function tests the primality of n.  
# RETURNS:
#				bool ~ True/False depending upon whether the number is prime/composite.



def IsPrime(n):

	bool = True
	
	if n > 3:
		for i in range(2,int(math.floor(math.sqrt(n)))):
			if (n % i) == 0:
				bool = False
				break
				
	return bool

#######################################
# FUNCTION: PrimeSieve
# PARAMETERS: 
# 				n ~ any natural number greater than two
# 
# PURPOSE: 
#	This function generates a list of all the prime numbers up to, and including, n.  Uses the ancient sieve
#   of Eratosthenes (~200s BC).
# RETURNS:
#				Nums ~ again, a list of all primes up to and including n.

def PrimeSieve(n):

	Nums = range(2,n+1)
	
	for i in Nums:
		if IsPrime(i) == True :
			for j in range(2,n/i + 1):
				if i*j in Nums:
					Nums.remove(i*j)
			#print Nums
			#print "\n\n"
			
	return Nums
	
m = int(input("\nPlease input an n.  The program will test all naturals up til n for primality. "))

print "\n"
print PrimeSieve(m)
