def last_survivor(letters, coords): 
    r = list(letters)
    for i in coords:
        r.pop(i)
    return ''.join(r)