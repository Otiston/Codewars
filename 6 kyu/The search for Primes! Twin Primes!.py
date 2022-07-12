def twin_prime(n):
    tp = 0
    if n > 2:
        for i in range (2,n+1):
            if (i-1) > 1 and prime(i-1) == True and prime(i+1) == True:
                tp+=1
    return tp

            
def prime(p):
    for i in range(2,p-1):
        if (p/i)-int(p/i) == 0:
            return False
    return True