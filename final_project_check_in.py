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
        while True:
            user_input = input(f"\n{self.name}, select your next move: {self.options}: ")
            
            if user_input.lower() == "exit":
                print("Exiting the game.")
                exit()

            if user_input in self.options:
                return user_input
            else:
                print("Invalid input - Please choose a valid move!")

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
        self.advanced_to_level_2 = False #controls level 2 lol

    def run(self):
        print("\n\nS A W  0\n\n")
        print("You find yourself in a dark room. Your goal is to survive the challenges and find the tape recorder.")
    
        narration1 = input("Would you like to read the narration before the game commences? [y/n]: ")
        if narration1.lower() == "y" or narration1.lower() == "yes":
            with open("saw0_l1_story.txt", "r", encoding="utf-8") as f:
                for line in f:
                    print(line.strip())
    
        while not self.game_over:
            if self.level == 1:
                # check if the level 1 is completed
                if self.level_1():
                    break
                if not self.game_over and self.level == 2:
                    self.level_2()
                '''
                narration2 = input("Would you like to read the narration before the game commences? [y/n]: ")
                if narration2.lower() == "y":
                    with open("saw0_l2_story.txt", "r", encoding="utf-8") as f:
                        for line in f:
                            print(line.strip())
                '''
        if not self.advanced_to_level_2:
            play_again = input("Would you like to play again? [y/n]: ")
            if play_again.lower() == "y" or play_again.lower() == "yes":
                self.reset_game()
                self.run()
        '''
        play_again = input("Would you like to play again? [y/n]: ")
        if play_again.lower() == "y" or play_again.lower() == "yes":
            self.reset_game()
            self.run()
        '''
    def level_1(self):
        human_move = self.human_player.move()
        computer_move = random.choice(self.computer_player.options)

        self.handle_move(self.human_player, human_move, self.computer_player, computer_move)

        if self.winner() == f"{self.human_player.name}" and self.level == 1:
            self.level += 1
            self.human_player.health = 100
            self.computer_player.health = 100
            print(f"{self.human_player.name} found the tape recorder and advances to Level 2!")
            self.advanced_to_level_2 = True

            # ends the function and breaks out of the loop
            return True

        # computer's move only if the game is not over
        if not self.game_over and self.level == 2:
            self.level_2()

        # return False if the game is not over or advanced to level 2
        return False

    def level_2(self):
        human_move = self.human_player.move()
        monster_move = random.choice(["attack", "defend", "tape"])

        pighead_name = "Pighead"
        pighead = ComputerPlayer(name = pighead_name, options = ["attack", "defend", "tape"])

        self.handle_move(self.human_player, human_move, pighead, monster_move)
        #self.handle_move(self.computer_player, monster_move, self.human_player, human_move)

        self.game_over = True if self.winner() else False

    def winner(self):
        if self.human_player.health <= 0:
            print(f"Game Over! {self.computer_player.name} wins! {self.human_player.name} loses!")  
            print("Winners stats:")
            print(str(self.computer_player))
            self.game_over = True
            return True

        elif self.human_player.options[-1] == "tape" and random.random() < 0.10:
            print(f"{self.human_player.name} found the tape recorder and advances to Level 2!")
            self.level += 1
            self.computer_player.health = 100

        elif self.computer_player.health <= 0:
            print(f"Congratulations! {self.human_player.name} wins the game!")
            print("Winners stats:")
            print(str(self.human_player))  # human player stats
            self.game_over = True
            return True

        elif self.computer_player.options[-1] == "tape" and random.random() < 0.05:
            print(f"{self.computer_player.name} found the tape recorder! {self.human_player.name} loses!")
            print("Winners stats:")
            print(str(self.computer_player))
            self.game_over = True
            return True

        return False

    def handle_move(self, attacker, attacker_move, defender, defender_move):
        damage = random.randint(10, 20)

        if attacker_move == "attack":
            print(f"\n{attacker.name} attacked!")
            if defender_move == "defend":
                print(f"{defender.name} defended!")
            elif defender_move == "tape":
                print(f"{defender.name} was looking for the tape!")
                self.computer_player.health -= damage
            elif defender_move == "attack":
                print(f"{defender.name} attacked!")
                self.human_player.health -= damage
                self.computer_player.health -= damage
        elif attacker_move == "defend":
            print(f"{attacker.name} defended!")
            if defender_move == "attack":
                print(f"{defender.name} attacked!")
            elif defender_move == "tape":
                print(f"{defender.name} was looking for the tape!")
            elif defender_move == "defend":
                print(f"{defender.name} defended!")
        elif attacker_move == "tape":
            print(f"{attacker.name} was looking for the tape!")
            if defender_move == "attack":
                print(f"{defender.name} attacked!")
                self.human_player.health -= damage
            elif defender_move == "tape":
                print(f"{defender.name} was looking for the tape!")
            elif defender_move == "defend":
                print(f"{defender.name} defended!")

        print(f"{self.human_player.name}'s health: {self.human_player.health}")
        print(f"{self.computer_player.name}'s health: {self.computer_player.health}")

    def reset_game(self):
        self.level = 1
        self.human_player.health = 100
        self.computer_player.health = 100
        self.game_over = False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Horror Survival Game")
    parser.add_argument("--player", type = str, help = "Name of the human player")
    parser.add_argument("--computer", type = str, help = "Name of the computer player")

    args = parser.parse_args()

    if args.player and args.computer:
        game = HorrorGame(human_name = args.player, computer_name = args.computer)  #keyword argument
        game.run()
    else:
        print("Please provide names for both players using --player and --computer.")
