from game_of_greed.game_logic import GameLogic, Banker


class Game:
    def __init__(self, roller = None):
        self.roller = roller
        self.rolling_counter = 6
        self.round = 1
        self.bank = Banker()

    def roller_function(self):
        print(f"Starting round {self.round}")
        print(f"Rolling 6 dice...")
        dice = self.roller(6)
        dice_printable = ",".join([str(d) for d in dice])
        print(dice_printable)
        input_dice = input("Enter dice to keep (no spaces), or (q)uit: ")
        return input_dice

    def continuing(self, input_dice): 
        if input_dice == "q":
            print(f"Thanks for playing. You earned {self.bank.bank()} points")
        else:
            input_list = [int(x) for x in list(input_dice)]
            # for i in enumerate(input_list):
            # self.rolling_counter -= 1
            score = GameLogic.calculate_score(tuple([int(x) for x in list(input_dice)]))
            unbanked = self.bank.shelf(score)
            print(f"You have {unbanked} unbanked points and 5 dice remaining")
            user_input_2 = input("(r)oll again, (b)ank your points or (q)uit ")
            if user_input_2 == "q":
                x = self.bank.bank()
                print(f"Total score is {x} points")  
                print(f"Thanks for playing. You earned {x} points")      
            if user_input_2 == "r":
                input_dice = self.roller_function()
                self.continuing(input_dice)
            elif user_input_2 == "b":
                bank_score = self.bank.bank()
                print(f"You banked {unbanked} points in round {self.round}")
            self.round += 1
            print(f"Total score is {bank_score} points")
            input_dice = self.roller_function()
            if input_dice == "q":
                x = self.bank.bank()
                print(f"Total score is {x} points")  
                print(f"Thanks for playing. You earned {x} points")  
            else:
                self.continuing(input_dice)
            
            




    def play(self):
        print("Welcome to Game of Greed")
        user_input = input("Wanna play? ")
        if user_input == "n" :
            print("OK. Maybe another time")
        else:
            input_dice = self.roller_function()
            input_dice = self.continuing(input_dice)
            







if __name__ == "__main__":
    roller = GameLogic.roll_dice
    trial = Game(roller)
    trial.play()


