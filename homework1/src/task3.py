#return positive, negative, or zero
def ifCheck(num):
    if num > 0:
        return "positive"
    elif num < 0:
        return "negative"
    else:
        return "zero"

#Return list of first ten prime numbers
def primes():
    primeList = []
    
    for num in range(2, 100):
        #return list when it has 10 elements
        if len(primeList) == 10:
            return primeList

        is_prime = True

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
        
        if is_prime:
            primeList.append(num)
    return primeList

    
#return sum of integers 1-100
def sumWhile():
    n = 0
    sum = 0
    while n <= 100:
        sum += n 
        n += 1
    return sum
    

        
