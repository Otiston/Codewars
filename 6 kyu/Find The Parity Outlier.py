def find_outlier(integers):
    pair = []
    impair = []
    for i in integers:
        if i%2 == 0:
            pair.append(i)
        else: 
            impair.append(i)
    if len(pair)>len(impair):
        return impair[0]
    else:
        return pair[0]