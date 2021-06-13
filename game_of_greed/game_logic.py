import random 
from collections import Counter

#hamza-----------------------------------------
class GameLogic :
    
    @staticmethod 
    def calculate_score (tupe):
        score =0  
        ctr = Counter(tupe)
        dice_common= ctr.most_common()


        if len(dice_common)== 6 :
            score=1500
            return score
        if len(dice_common)==3: 
            if dice_common[0][1]==2 and  dice_common[1][1]==2 and  dice_common[2][1]==2: 
                score = 750 
                return score


        for i in dice_common: 

            if i[1] < 3 : 
                if i[0] == 1 :
                    score +=(i[1]*100)
                if i[0]==5: 
                    score+= (i[1]*50)
            
#basel ---------------------------
            if i[1] ==3:
                if i[0] == 1:
                    score+=1000
                if i[0] == 2:
                    score+=200
                if i[0] == 3:
                    score+=300
                if i[0] == 4:
                    score+=400
                if i[0] == 5:
                    score+=500
                if i[0] == 6:
                    score+=600
            if i[1] ==4:
                if i[0] == 1:
                    score+=2000
                if i[0] == 2:
                    score+=400
                if i[0] == 3:
                    score+=600
                if i[0] == 4:
                    score+=800
                if i[0] == 5:
                    score+=1000
                if i[0] == 6:
                    score+=1200  

# Suhib----------------------
            if i[1] ==5:
                if i[0] == 1:
                    score+=3000
                if i[0] == 2:
                    score+=600
                if i[0] == 3:
                    score+=900
                if i[0] == 4:
                    score+=1200
                if i[0] == 5:
                    score+=1500
                if i[0] == 6:
                    score+=1800  
            if i[1] ==6:
                if i[0] == 1:
                    score+=4000
                if i[0] == 2:
                    score+=800
                if i[0] == 3:
                    score+=1200
                if i[0] == 4:
                    score+=1600
                if i[0] == 5:
                    score+=2000
                if i[0] == 6:
                    score+=2400  
        return score

# Nofal---------------------------------
   #output : an integer representing the roll's score according to rules of game.
    @staticmethod
    def  roll_dice (n):
        randomlist = []
        for i in range(1,n+1):
            num = random.randint(1,6)
            randomlist.append(num) 
        return tuple(randomlist)   
class Banker:
    def __init__ (self):
        self.shelved=0
        self.balance=0
    def shelf (self,points):
        self.shelved=points 
        return self.shelved
    def bank (self):
        self.balance=0
        self.balance+=self.shelved
        self.shelved=0
        return self.balance
    def clear_shelf (self):
        self.shelved=0      

    



