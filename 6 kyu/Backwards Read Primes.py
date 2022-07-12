from gmpy2 import is_prime
    
def backwards_prime(start, stop):
    ans = []
    print(start,stop)
    for i in range(start,stop+1):
        re = int(str(i)[::-1])
        if is_prime(i) == True and is_prime(re) == True and i != re:
            ans.append(i)
    return ans