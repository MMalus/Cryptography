#generates a list of primes between two user input numbers

primeList = []

def isPrime(x):
    if x==1:
        return False
    
    for i in range(2,int(x/2)):
        if(x%i == 0):
            return False
    
    return True
    
def primeRange(x, y):
    for i in range(x, y+1):
        if(isPrime(i)):
            primeList.append(i)