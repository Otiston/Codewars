def is_prime(n):
    print(n)
    if type(n) == int and n > 1:
        for i in range(2,n):
            if n != i and (n/i)-int(n/i) == 0:
                return False
        return True
    else:
        return False