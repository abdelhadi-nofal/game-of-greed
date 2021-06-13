import random 
from collections import Counter

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
            

#hamza-----------------------------------------


        

    



