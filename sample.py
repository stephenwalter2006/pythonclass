def findTotal(count , val):
	maxVal = 0
	if count%val == 0 :
		maxVal = count - val
	else:
		maxVal = count - (count%val)

	endVal = maxVal/val

	return val * ((endVal*(endVal+1))/2)

def eulerProblemOne(count, *args):
	total = 0
	argCount = len(args)
	common = 1

	for x in range(argCount):
		total += findTotal(count,args[x])
		common *= args[x]

	if common < count:
		total -= findTotal(count, common)
	return total
		
def eulerProblemTen(limit):
	array = [True for i in range(limit +1)]
	array[0] = False
	array[1] = False
	j = 2
	while(j*j < limit ):
		if array[j] == True:
			for k in range(j*j , limit +1 , j):
				array[k] = False
		j += 1
	total = 0
	for num in range(2, limit+1):
		if(array[num] == True):
			total += num

	return total
	
				   

print(eulerProblemOne(1000, 3 ,5))
print(eulerProblemTen(2000000))
