from collections import Counter
from game_of_greed.game_logic import GameLogic, Banker


class Game:
    def __init__(self, roller = None):
        self.roller = roller
        self.dice = ()
        self.rolling_counter = 6
        self.round = 1
        self.bank = Banker()
        self.unbanked =0
        self.bank_account = self.bank.bank()

    
    def quitter1111(self):
        input_dice = input("Enter dice to keep (no spaces), or (q)uit: ")
        return self.continuing(input_dice)


    def roller_function(self):
        print(f"Starting round {self.round}")
        print(f"Rolling {self.rolling_counter} dice...")
        self.dice = self.roller(self.rolling_counter)
        dice_printable = ",".join([str(d) for d in self.dice])
        print(dice_printable)
        unbanked = GameLogic.calculate_score(self.dice)
        if unbanked == 0:
            print("Zilch!!! Round over")
            print(f"You banked {unbanked} points in round {self.round}")
            self.round += 1
            self.rolling_counter = 6
            self.bank_account = self.bank.bank()
            print(f"Total score is {self.bank_account} points")
            self.roller_function()
        else:
            return self.quitter1111()

    def continuing(self, input_dice): 
        if input_dice == "q":
            if self.bank_account != 0 or self.unbanked != 0:
                print(f"Total score is {self.bank_account} points")  
                print(f"Thanks for playing. You earned {self.bank_account} points")
            else:
                print(f"Thanks for playing. You earned {self.bank_account} points")
        else:
            
            input_tuple = tuple([int(x) for x in list(input_dice)])
            ctr1 = Counter(input_tuple)
            dice_input_common= ctr1.most_common()
            
            if_in = True
            for x, val in enumerate(dice_input_common):
                if val[0] not in self.dice:
                    if_in = False
                else:
                    if (input_tuple.count(val[0]) <= self.dice.count(val[0])):
                        if_in = True
                    else:
                        if_in = False

            if if_in == True:
                for i in enumerate([int(x) for x in list(input_dice)]):
                    self.rolling_counter -= 1
                score = GameLogic.calculate_score(input_tuple)
                unbanked = self.bank.shelf(score)
                self.unbanked = unbanked
                print(f"You have {unbanked} unbanked points and {self.rolling_counter} dice remaining")
                user_input_2 = input("(r)oll again, (b)ank your points or (q)uit ")
                if user_input_2 == "q": 
                    print(f"Total score is {self.bank_account} points")  
                    print(f"Thanks for playing. You earned {self.bank_account} points") 
                else:   
                    if user_input_2 == "r":
                        if unbanked == 750 or unbanked == 1500 :
                            print("Rolling 6 dice...")
                            self.dice = self.roller(6)
                            dice_printable = ",".join([str(d) for d in self.dice])
                            print(dice_printable)
                            self.rolling_counter = 6
                            self.quitter1111()
                        else:
                            print(f"Rolling {self.rolling_counter} dice...")
                            self.dice = self.roller(self.rolling_counter)
                            dice_printable = ",".join([str(d) for d in self.dice])
                            print(dice_printable)
                            score1 = GameLogic.calculate_score(self.dice)
                            if score1 == 0:
                                print("Zilch!!! Round over")
                                self.bank.clear_shelf()
                                print(f"You banked {self.bank_account} points in round {self.round}")
                                self.round += 1
                                self.rolling_counter = 6
                                self.bank_account = self.bank.bank()
                                print(f"Total score is {self.bank_account} points")
                                self.roller_function()
                            else:
                                self.quitter1111()
                    elif user_input_2 == "b":
                        print(f"You banked {unbanked} points in round {self.round}")
                        self.round += 1
                        self.rolling_counter = 6
                        self.bank_account = self.bank.bank()
                        print(f"Total score is {self.bank_account} points")
                        self.roller_function()
                        
                    elif user_input_2 == "q":
                            if self.bank_account != 0:
                                print(f"Total score is {self.bank_account} points")  
                                print(f"Thanks for playing. You earned {self.bank_account} points")
                            else:
                                print(f"Thanks for playing. You earned {self.bank_account} points")

                    
            else:
                print("Cheater!!! Or possibly made a typo...")
                dice_printable = ",".join([str(d) for d in self.dice])
                print(dice_printable)
                self.quitter1111()
                
                



    def play(self):
        print("Welcome to Game of Greed")
        user_input = input("Wanna play? ")
        if user_input == "n" :
            print("OK. Maybe another time")
        else:
            self.roller_function()
            
            







if __name__ == "__main__":
    roller = GameLogic.roll_dice
    trial = Game(roller)
    trial.play()
