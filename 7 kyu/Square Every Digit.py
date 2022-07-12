def square_digits(num):
    np = []
    for x in list(str(num)):
        np.append(str(int(x)**2))
    return int(''.join(np))