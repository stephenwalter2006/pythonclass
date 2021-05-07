def problemOne(count):
    sum = 0
    for x in range(count):
        if(x%3 == 0 or x%5 == 0):
            sum += x
    return sum


print(problemOne(10))
