def beeramid(bonus, price):
    totalbeer = bonus/price
    pyramidlvl = 0
    
    while totalbeer >= (pyramidlvl+1)**2:
        totalbeer -= (pyramidlvl+1)**2
        pyramidlvl +=1
    
    return pyramidlvl
