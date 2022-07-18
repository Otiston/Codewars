class PokerHand(object):
    
    RESULT = ["Loss", "Tie", "Win"]

    def __init__(self, hand):
        
        #We put the hand into an array then each card into an array, spliting the value of the card and it's suit
        
        hand = hand.split(" ")
        for i in range(len(hand)):
            hand[i] = [n for n in hand[i]]
            
        #we replace the card value of T and higher by a number and make all the values into int
        
        for i in range(len(hand)):
            match hand[i][0]:
                case "T":
                    hand[i][0] = 10
                case "J":
                    hand[i][0] = 11
                case "Q":
                    hand[i][0] = 12
                case "K":
                    hand[i][0] = 13
                case "A":
                    hand[i][0] = 14
            hand[i][0] = int(hand[i][0])
            
        #we creat 2 array for the sorted value and for the suit
        
        handvalue = [i[0] for i in hand]
        handvalue.sort()
        handsuit = [i[1] for i in hand]
        
        #we check the card combo and define the hand rank
        
        match len(list(dict.fromkeys(handvalue))):
            case 2:
                rank = "fh"
                for i in list(dict.fromkeys(handvalue)):
                    if handvalue.count(i) == 4:
                        rank = "4"
            case 3:
                rank = "dpair"
                for i in list(dict.fromkeys(handvalue)):
                    if handvalue.count(i) == 3:
                        rank = "set"
            case 4: 
                rank = "pair"
            case 5:
                if max(handvalue) - min(handvalue) == 4:
                    if len(list(dict.fromkeys(handsuit))) == 1:
                        rank = "sflush"
                    else:
                        rank = "straight"
                elif len(list(dict.fromkeys(handsuit))) == 1:
                    rank = "flush"
                else:
                    rank = "hc"
        
        #we declare the properti of the object
        
        self.hand = hand
        self.handvalue = handvalue
        self.handsuit = handsuit
        self.rank = rank
        pass
        
    def compare_with(self, other):
        #we define the ranking
        ranking = ["hc","pair","dpair","set","straight","flush","fh","4","sflush"]
        
        #we check the ranking of each hand
        
        if ranking.index(self.rank) > ranking.index(other.rank):
            return "Win"
        elif ranking.index(self.rank) < ranking.index(other.rank):
            return "Loss"
        
         #if they have the same ranking we check for the best kicker
            
        else:
            for _ in range(5):
                if max(self.handvalue) > max(other.handvalue):
                    return "Win"
                elif max(self.handvalue) < max(other.handvalue):
                    return "Loss"
                else:
                    self.handvalue.pop(self.handvalue.index(max(self.handvalue)))
                    other.handvalue.pop(other.handvalue.index(max(other.handvalue)))
                    
        #if they have the ranking and same kicker it's a tie
        
            return "Tie"
        pass
