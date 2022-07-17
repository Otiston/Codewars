import math

def pf(n):
    prime = []
    
    while n % 2 == 0:
        prime.append(2)
        n /= 2
        
    for i in range(3, int(math.sqrt(n))+1, 2):
        while n % i == 0:
            prime.append(int(i))
            n /= i
            
    if n > 2:
        prime.append(int(n))
        
    return prime
    
    
def sum_for_list(lst):
    prime = []
    result = []
    
    for n in lst:
        prime.extend(pf(abs(n)))  
    prime = list(dict.fromkeys(prime))
    prime.sort()

    for n in prime:
        chunk = [0,0]
        for i in lst:
            if i%n == 0:
                chunk[0] = n
                chunk[1] += i
        if chunk[0] != 0:
            result.append(chunk)
           
    return result
