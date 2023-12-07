import argparse
import random

class HumanPlayer:
    """Represents a human player.
    
    Attributes:
        name (str): player's name.
        options (list of str): the player's move options.
        health (int): player's current health.
    """
    def __init__(self, name, options):
        """Populates attributes.

        Args:
            name (str): player's name.
            options (list of str): player's move options.
            
        Side effects:
            Populates attributes.
        """
        self.name = name
        self.options = options
        self.health = 100
    
    def __str__(self):
        """
        prints the players stats after saying the player won the game. 
        """
        return (f"\t name: {self.name}\n\t health: {self.health}")  #magic method
        
    def move(self):
        """Asks the human player to make their next move.
        
        Raises:
            
        Returns:
            player input (str): player's input to select their move. 
        """
        return input(f"{self.name}, select your next move: {self.options}: ")

class ComputerPlayer(HumanPlayer):
    """Subclass of HumanPlayer class. Represents a computer player.
    
    Attributes:
        name (str): player's name.
        options (list of str): the player's move options.
        health (int): player's current health.
    """
    def __init__(self, name, options):
        """Populates attributes.
        
        Args:
            name (str): the player's name name.
            options (list of str): the player's move options.
        """
        super().__init__(name, options) # this super should work
        
class HorrorGame:
    def __init__(self, human_name, computer_name):
        self.human_player = HumanPlayer(name=human_name, options = ["attack", "defend", "tape"])  #keyword argument
        self.computer_player = ComputerPlayer(name = computer_name, options= ["attack", "defend", "tape"])
        self.level = 1
        self.game_over = False  # controls game loop

    def run(self):
        print("Welcome to the Horror Survival Game!")
        print("You find yourself in a dark room. Your goal is to survive the challenges and find the tape recorder.")
        
        while not self.game_over:
            if self.level == 1:
                self.level_1()
            elif self.level == 2:
                self.level_2()

        play_again = input("Would you like to play again? [y/n]: ")
        if play_again.lower() == "y":
            self.reset_game()
            self.run()

    def level_1(self):
        #with open("saw0_story.txt", "r", encoding="utf-8") as f:
            #for line in f:
                #if "Level 1 Narration" in line:
                    #print(line.strip())
        human_move = self.human_player.move()
        computer_move = random.choice(self.computer_player.options)

        self.handle_move(self.human_player, human_move, self.computer_player, computer_move)
        self.handle_move(self.computer_player, computer_move, self.human_player, human_move)

        self.game_over = True if self.winner() else False


    def level_2(self):
        #with open("saw0_story.txt", "r", encoding="utf-8") as f:
            #for line in f:
                #if "Level 2 Narration" in line:
                    #print(line.strip())
        monster_move = random.choice(self.computer_player.options)
        human_move = self.human_player.move()

        self.handle_move(self.human_player, human_move, self.computer_player, monster_move)
        self.handle_move(self.computer_player, monster_move, self.human_player, human_move)

        self.game_over = True if self.winner() else False


    def winner(self):
        if self.human_player.health <= 0:
            print(f"Game Over! {self.computer_player.name} wins! {self.human_player.name} loses!")  
            print("Winners stats:")
            print(str(self.computer_player))
            return True
        elif self.computer_player.health <= 0:
            if self.level == 1:
                self.level += 1
                self.computer_player.health = 100
                print(f"{self.human_player.name} found the tape recorder and advances to Level 2!")
            elif self.level == 2:
                print(f"Congratulations! {self.human_player.name} wins the game!")
                print("Winners stats:")
                print(str(self.human_player)) #human player stats
            return True
        elif self.computer_player.options[-1] == "tape" and random.random() < 0.05:
            print(f"{self.computer_player.name} found the tape recorder! {self.human_player.name} loses!")
            print("Winners stats:")
            print(str(self.computer_player))
            return True
        return False

    def handle_move(self, attacker, attacker_move, defender, defender_move):
        damage = random.randint(10, 20)

        if attacker_move == "attack":
            print(f"{attacker.name} attacked!")
            if defender_move == "defend":
                print(f"{defender.name} was looking for the tape!")
            elif defender_move == "tape":
                print(f"{defender.name} defended!")
            defender.health -= damage
        elif attacker_move == "defend":
            print(f"{attacker.name} defended!")
            if defender_move == "attack":
                print(f"{defender.name} was looking for the tape!")
            elif defender_move == "tape":
                print(f"{defender.name} attacked!")
        elif attacker_move == "tape":
            print(f"{attacker.name} found the tape recorder!")

        print(f"{self.human_player.name}'s health: {self.human_player.health}")
        print(f"{self.computer_player.name}'s health: {self.computer_player.health}")

    def reset_game(self):
        self.level = 1
        self.computer_player.health = 100
        self.game_over = False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Horror Survival Game")
    parser.add_argument("--player", type=str, help="Name of the human player")
    parser.add_argument("--computer", type=str, help="Name of the computer player")

    args = parser.parse_args()

    if args.player and args.computer:
        game = HorrorGame(human_name=args.player, computer_name=args.computer)  #keyword argument
        game.run()
    else:
        print("Please provide names for both players using --player and --computer.")
