def is_valid_walk(walk):
    ho, ve = [], []
    for d in walk:
        if d == "n":
            ve.append(1)
        elif d == "s":
            ve.append(-1)
        elif d == "w":
            ho.append(1)
        else:
            ho.append(-1)
    if sum(ho) == 0 and sum(ve) == 0 and len(walk) == 10:
        return True 
    else:
        return False