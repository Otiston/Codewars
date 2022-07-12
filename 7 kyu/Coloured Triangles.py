def triangle(row):
    if len(row) == 1:
        return row
    r = row
    for i in range(0,len(row)-1):
        r = loop(r)
    return r[0]
    
def loop(row):
    nr = []
    for i in range(0,len(row)-1):
        d = [row[i],row[i+1]]
        if ''.join(d) == "RR" or ''.join(d) == "GB" or ''.join(d) == "BG":
            nr.append("R")
        elif ''.join(d) == "GG" or ''.join(d) == "BR" or ''.join(d) == "RB":
            nr.append("G")
        elif ''.join(d) == "BB" or ''.join(d) == "GR" or ''.join(d) == "RG":
            nr.append("B")
    return nr