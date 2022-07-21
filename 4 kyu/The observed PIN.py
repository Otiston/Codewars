from itertools import combinations

def get_pins(o):
    p1,p2,p3,p4,p5,p6,p7,p8,p9,p0 = "124","1235","236","1457","24568","3569","478","57890","689","80"
    pin = locals()
    comb = []
    for i in o:
        comb += pin.get('p' + str(i)) 
    
    result = list(combinations(comb,len(o)))
        
    for i in range(len(result)):
        result[i] = ''.join(list(result[i]))
    
    result = list(dict.fromkeys(result))
    fresult = [i for i in result]
    
    for i in result:
        for n in range(len(i)): 
            if i[n] not in pin.get('p' + str(o[n])):
                fresult.remove(i)
                break
    
    return fresult
