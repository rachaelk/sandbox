import random
# BernResult = [];
# #BernTrial=0;
# for i in range(100):
# 	BernTrial = random.random()
# 	if BernTrial <= .5:
# 		BernResult.append(1)
# 	if BernTrial > 0.5:
# 		BernResult.append(0)

# print BernResult

def BernTrial(n,p):
	BernResult = []
	for i in range(n):
		if random.random() <= p:
			BernResult.append(1)
		else:
			BernResult.append(0)
	return BernResult

n = int(input('\n\nHI Please input number of trials >> '))
p = float(input('\n\nPlease input success rate >> '))


print float(sum(BernTrial(n,p)))/n
