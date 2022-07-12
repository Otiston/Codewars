def points(games):
    r = 0
    for g in games:
        g = g.split(":")
        if g[0] > g[1]: 
            r = r + 3
        elif g[0] == g[1]:
            r = r + 1
    return r
pass 