def findTotal(count , val):
	maxVal = 0
	if count%val == 0 :
		maxVal = count - val
	else:
		maxVal = count - (count%val)

	endVal = maxVal/val

	return val * ((endVal*(endVal+1))/2)

def problemOne(count, *args):
	total = 0
	argCount = len(args)
	common = 1

	for x in range(argCount):
		total += findTotal(count,args[x])
		common *= args[x]

	if common < count:
		total -= findTotal(count, common)
	return total
		
				   

print(problemOne(1000, 3 ,5))
