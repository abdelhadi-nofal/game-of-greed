import builtins
import re
from abc import abstractmethod
from game_of_greed.game_logic import *
from game_of_greed.game import *

class BasePlayer:
    def __init__(self):
        self.old_print = print
        self.old_input = input 
        builtins.print = self._mock_print # Methods overriding
        builtins.input = self._mock_input # Methods overriding
        self.total_score = 0

    def reset(self):
        builtins.print = self.old_print
        builtins.input = self.old_input
    # The default behaviour
    @abstractmethod
    def _mock_print(self, *args):
       return self.old_print(*args)
    @abstractmethod
    def _mock_input(self, *args):
        return self.old_input(*args)
    @classmethod
    def play(cls, num_games=1):
        mega_total = 0
        for i in range(num_games):
            player = cls()
            game = Game() # doesn't pass a mock roller
            try:
                game.play()
            except SystemExit:
                # in game system exit is fine
                # because that's how they quit.
                pass
            mega_total += game.bank_account
            player.reset()
        print(f"{num_games} games (maybe) played with average score of {game.bank_account // num_games}")

class NervousNellie(BasePlayer):
    def __init__(self):
        super().__init__()
        self.roll = None

    def _mock_print(self, *args):
        first_arg = args[0]
        first_char = first_arg[0]
        if first_char.isdigit():
            self.roll = tuple(int(char) for char in first_arg.split(","))
        elif first_arg.startswith("Thanks for playing."):
            self.total_score = int(re.findall(r"\d+", first_arg)[0])
        self.old_print(first_arg)

    def _mock_input(self, *args):
        prompt = args[0]
        if prompt.startswith("Wanna play?"):
            return "y"
        elif prompt.startswith("Enter dice to keep (no spaces), or (q)uit:"):
            scorers = GameLogic.get_scorers(self.roll)
            keepers = "".join([str(ch) for ch in scorers])
            return keepers
        elif prompt.startswith("(r)oll again, (b)ank your points or (q)uit "):
            return "b"
        else:
            raise ValueError(f"Unrecognized prompt {prompt}")


class ourbot(BasePlayer):
    def __init__(self):
        super().__init__()
        self.roll = None
    def _mock_print(self, *args, **kwargs):
        first_arg = args[0]
        first_char = first_arg[0]
        if first_char.isdigit():
            self.roll = tuple(int(char) for char in first_arg.split(","))
            # self.old_print(self.roll)
        elif first_arg.startswith("Thanks for playing."):
            self.total_score = int(re.findall(r"\d+", first_arg)[0])
        self.old_print(first_arg)
    def _mock_input(self, *args, **kwargs):
        prompt = args[0]
        if prompt.startswith("Wanna play?"):
            # self.old_print(prompt, 'y')
            return "y"
        elif prompt.startswith("Enter dice to keep (no spaces), or (q)uit:"):
            scorers = GameLogic.get_scorers(self.roll)
            keepers = "".join([str(ch) for ch in scorers])
            self.old_print(prompt, keepers)
            return keepers
        elif prompt.startswith("(r)oll again, (b)ank your points or (q)uit "):
            scorers = GameLogic.get_scorers(self.roll)
            keepers = "".join([str(ch) for ch in scorers])
            # self.old_print(scorers)
            if (len(self.roll) - len(keepers))>3 or len(keepers) == 6:
                self.old_print(prompt, 'r')
                return "r"
            else:

                self.old_print(prompt, 'b')
                return "b"
        else:
            raise ValueError(f"Unrecognized prompt {prompt}")



if __name__ == "__main__":
    ourbot.play(100)
    # NervousNellie.play(100)