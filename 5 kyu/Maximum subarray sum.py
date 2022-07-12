def max_sequence(li):
    meilleur = 0
    im = -1
    jm = -1
    for i in range (0, len(li)):
        s = 0
        for j in range(i, len(li)):
            s += li[j]
            if s > meilleur:
                meilleur = s
                im, jm = i, j+1
    return sum(li[im:jm])