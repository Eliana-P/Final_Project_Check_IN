import argparse
import random

class HumanPlayer:        
    """Represents a human player.  
    
    Attributes:  
        name (str): player's name.  
        options (list of str): the player's move options.  
        health (int): player's current health.  
        move (str): player's current move  
    """
    def __init__(self, name, options, move):  
        """Populates attributes.  
        Primary Author: Tiara
        
        Args:  
            name (str): player's name.  
            options (list of str): player's move options.  
            move (str): player's move.  
            
        Side effects:  
            Populates attributes.  
        """  
        self.name = name  
        self.options = options  
        self.move = move  
        self.health = 100  
    
    
    def __str__(self):
        """Returns the player stats after saying the player won the game.
        Primary Author: Eliana

        Returns: 
            Returns (str): Returns the players stats. 
        """
        return (f"\t name: {self.name}\n\t health: {self.health}")  #magic method
        
        
    def make_move(self):  
        """Asks the human player to make their next move.   
        Primary Author: Tiara
        
         Side effects:  
            print (str): prints a string saying the user has exited the game.  
            print (str): prints string telling the user it was a invalid input and to choose a new move.  
        """
        user_input = input(f"\n{self.name}, select your next move: {self.options}. You can also select 'exit' to exit the game: ")  
            
        if user_input.lower() == "exit":  
            print("Exiting the game.")  
            exit()  

        elif user_input.lower() in self.options:  
            self.move = user_input  
            
        else:  
            print("Invalid input - Please choose a valid move!")  


class ComputerPlayer(HumanPlayer):  
    """Subclass of HumanPlayer class. Represents a computer player.  
    Primary Author: Tiara
    
    Attributes:  
        name (str): player's name.  
        options (list of str): the player's move options.  
        health (int): player's current health.   
        move (str): player's current move.  
    """
    def __init__(self, name, options, move):  
        """Populates attributes.  
        
        Args:  
            name (str): the player's name name.  
            options (list of str): the player's move options.  
            move (str): player's move.  
        """
        super().__init__(name, options, move)   
        
class HorrorGame:
    def __init__(self, human_name, computer_name):
        """Initializes attributes.
        Primary Author: Eliana

        Args:
            human_name(str): the human's name.
            computer_name(str): the computer's name.
        """
        self.human_player = HumanPlayer(name=human_name, move="", options = ["attack", "defend", "tape"])  #keyword argument   
        self.computer_player = ComputerPlayer(name = computer_name, move="", options= ["attack", "defend", "tape"])   
        self.level = 1    
        self.game_over = False   
        self.advanced_to_level_2 = False      
        self.weapon_status = False   
        
    def run(self):  
        """Runs the narration, determines if user has already been asked to read narration for level 2
        Primary Author: Laraib Leghari

        Side effects:
        print (str): prints the format of SAW 0 
        print (str): prints the introduction
        with open: opens the narration from the text file
        
        """ 
        narration2 = "empty"  
        print("\n\nS A W  0\n\n")  
        print("You find yourself in a dark room. Your goal is to survive the challenges and find the tape recorders.")  
    
        narration1 = input("\nWould you like to read the narration before the game commences? [y/n]: ")  
        if narration1.lower() == "y" or narration1.lower() == "yes":  
            with open("saw0_l1_story.txt", "r", encoding="utf-8") as f:  
                for line in f:  
                    story = f.readlines()[0:]  
                    print("\n")  
                    for line in story:  
                        print(line.strip())  
            
        while not self.game_over: 
            if self.level == 1: 
                # check if the level 1 is completed 
                self.level_1() 
            # If the current level is 2 and the reader hasn't been asked to read the narration for level 2 yet 
            if self.level == 2 and narration2 == "empty": 
                narration2 = input("Would you like to read the narration before the game commences? [y/n]: ") 
                if narration2.lower() == "y" or narration2.lower() == "yes": 
                    with open("saw0_l2_story.txt", "r", encoding="utf-8") as f: 
                        story = f.readlines()[1:] 
                        print("\n") 
                    for line in story: 
                            print(line.strip()) 
                    self.level_2() 
            # If the current level is 2 and the reader has already been asked to read narration 2 
            # Before, it kept asking the user before each move 
            elif self.level == 2 and narration2 != "empty": 
                self.level_2() 
                        
        if self.level != 2: 
            play_again = input("Would you like to play again? [y/n]: ") 
            if play_again.lower() == "y" or play_again.lower() == "yes": 
                self.reset_game() 
                self.run() 

    def level_1(self):
        """Level 1 of the game, user makes a move and computer responds a with random move
        Primary author: Nithya
        
        Returns:
            bool: it is True if the player goes to level 2, else it is False 
        
        """
        self.human_player.make_move()
        computer_move = random.choice(self.computer_player.options)

        self.handle_move(self.human_player, self.computer_player, computer_move)

        if self.winner() and self.level == 1:
            self.level += 1
            self.human_player.health = 100
            self.computer_player.health = 100
            self.advanced_to_level_2 = True

            # ends the function and breaks out of the loop
            pighead_name = "Pighead"
            pighead = ComputerPlayer(name = pighead_name, options = ["attack", "defend", "tape"], move="")
            self.computer_player = pighead
            return True
                
        # return False if the game is not over or advanced to level 2
        return False


    def level_2(self): 
        """Level 2 of the game, the user makes a move, the computer responds a with random move, and the monster attacks
        Primary Author: Laraib Leghari

        Side effects:
        The human player makes a move with self.human_player.make_move(): 
        A move is chosen at random with random.choice()
        Whether or not the game is over and if there is a winner is determined
        """
        self.human_player.make_move()  
        monster_move = random.choice(["attack", "defend", "tape"])  

        self.handle_move(self.human_player, self.computer_player, monster_move)  
        
        self.game_over = True if self.winner() else False  

    
    def weapon(self):  
        """Generates a weapon that the human player may find.  
        Primary Author: Tiara
        """  
        luck = random.randint(1, 3)  
        weapons = {1 : {"Machette" : 35},  
                2 : {"Rusty Pipe" : 25},  
                3 : {"Knife" : 30}}  
        if luck in weapons.keys():  
            player_weapon = weapons[luck]  
            for key, value in player_weapon.items():  
                self.item, self.w_damage = key, value  


    def winner(self):
        """Determines the winner of the game.
        Primary Author: Eliana

        Returns: 
            Returns (bool): Returns True depending on winner status, false if nothing happens.

        Side effects:
            Prints (str): prints string that explains final status of the game, or if it's advancing to another level.
        """
        if self.human_player.health <= 0 and self.computer_player.health > 0: 
            print(f"Game Over! {self.computer_player.name} wins! {self.human_player.name} loses!")    
            print("Winners stats:")    
            print(str(self.computer_player))   
            self.game_over = True    
            return True    
        
        elif self.computer_player.health <= 0 and self.human_player.health > 0:   
            print(f"Congratulations! {self.human_player.name} wins the game! Advancing to level {self.level + 1}!")   
            print("Winners stats:")    
            print(str(self.human_player))  # human player stats   
            return True   

        elif self.human_player.health <=0 and self.computer_player.health <=0:   
            print("Game over! Both players have died!")  
            
        elif self.human_player.move == "tape" and random.random() < 0.10:   
            print(f"{self.human_player.name} found the tape recorder and advances to Level {self.level + 1}!")   
            return True  

        elif self.computer_player.move == "tape" and random.random() < 0.05:   
            print(f"{self.computer_player.name} found the tape recorder! {self.human_player.name} loses!")   
            print("Winners stats:")   
            print(str(self.computer_player))   
            self.game_over = True    
            return True   
        
        return False   


    def handle_move(self, attacker, defender, defender_move):
        """The moves between the attacker and defender in the game, determines the outcome
        Primary author: Nithya
        
        Args:
            attacker (Player): The player that is making the move
            defender (Player): the player that is getting attacked or is defending
            defender_move (str): the defender's chosen move
        
        Side effects:
            Updates health of the attacker and the defender
            Prints the according information of the player's move
        """
        damage = random.randint(10, 20)
           
        if attacker.move == "tape" and random.random() > .50:
                self.weapon()
                self.weapon_status = True
                print(f"\n{attacker.name} found a {self.item} with {self.w_damage} damage while looking for the tape!")
                if defender_move == "attack":
                    print(f"{defender.name} attacked!")
                    self.human_player.health -= damage
                elif defender_move == "tape":
                    print(f"{defender.name} was looking for the tape!")
                elif defender_move == "defend":
                    print(f"{defender.name} defended!")
                             
        elif attacker.move == "tape" and random.random() <= .50:
            print(f"\n{attacker.name} was looking for the tape!")
            if defender_move == "attack":
                print(f"{defender.name} attacked!")
                self.human_player.health -= damage
            elif defender_move == "tape":
                print(f"{defender.name} was looking for the tape!")
            elif defender_move == "defend":
                print(f"{defender.name} defended!")
        
        elif attacker.move == "attack":
            print(f"\n{attacker.name} attacked!")
            if defender_move == "defend":
                print(f"{defender.name} defended!")
            elif defender_move == "tape":
                print(f"{defender.name} was looking for the tape!")
                if self.weapon_status == True:
                    self.computer_player.health -= int(self.w_damage)
                else:
                    self.computer_player.health -= damage
            elif defender_move == "attack":
                print(f"{defender.name} attacked!")
                self.human_player.health -= damage
                if self.weapon_status == True:
                    self.computer_player.health -= int(self.w_damage)
                else:
                    self.computer_player.health -= damage
                    
        elif attacker.move == "defend":
            print(f"\n{attacker.name} defended!")
            if defender_move == "attack":
                print(f"{defender.name} attacked!")
            elif defender_move == "tape":
                print(f"{defender.name} was looking for the tape!")
            elif defender_move == "defend":
                print(f"{defender.name} defended!")
                
        print(f"{self.human_player.name}'s health: {self.human_player.health}")
        print(f"{self.computer_player.name}'s health: {self.computer_player.health}")
        
    def reset_game(self):
        """Resets the game to its original state
        Primary author: Nithya
        
        Side effects:
            Puts the game level back to 1, health go back to 100, and game over is False
        """
        
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
