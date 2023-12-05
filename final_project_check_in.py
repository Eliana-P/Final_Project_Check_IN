import argparse
import random

"""survival game"""
def playerHealth(damage, healthstatus):
    """Looks at the user's health status and how much damage they have taken. Player starts at 100
    
    Attributes:
    damage(int): the level of damage the player has
    healthstatus(int): the health status of the player with/without damage
    
    Returns:
    a string identifying the health level
    
    """

    if healthstatus == 100:
        return "Perfect health!"
    elif healthstatus - damage >= 80:
        return "Great health!"
    elif healthstatus - damage >= 70:
        return "Decent Health"
    elif healthstatus - damage >= 50:
        return "Average health"
    elif healthstatus - damage >= 30:
        return "Low health"
    elif healthstatus - damage >= 20:
        return "Emergency health"
    
def computerHealth(damage, healthstatus):
    """Looks at the computer's health status and how much damage they have taken. Computer starts at 100
    
    Attributes:
    damage(int): the level of damage the computer has
    healthstatus(int): the health status of the computer with/without damage
    
    Returns:
    a string identifying the health level
    
    """

    if healthstatus == 100:
        return "Perfect health!"
    elif healthstatus - damage >= 80:
        return "Great health!"
    elif healthstatus - damage >= 70:
        return "Decent Health"
    elif healthstatus - damage >= 50:
        return "Average health"
    elif healthstatus - damage >= 30:
        return "Low health"
    elif healthstatus - damage >= 20:
        return "Emergency health"
    elif healthstatus - damage == 0:
        return "No health"

def winner(playerHealth, computerHealth):
    """Returns the winner of the game based on health.
    Returns: 
        Returns a string stating that computer won. 
        Returns a string stating that player won. 
    """
    if playerHealth == 0:
        if computerHealth > 0:
            return "Computer won!"
    if computerHealth == 0:
        if playerHealth > 0:
            return "Player won!"

def monster():
    """An attack by a monster
    
    Returns:
        damage (int): the damage that has been recieved by the monster
    """
    m_damage = random.randint(5,50)
    return m_damage


class HumanPlayer:
    def __init__(self, name, choice):
        self.name = name
        self.choice = choice
        
    def move(self, data):
        """Asks the human player to make their next move.
        Args:
            data (list of str): tracks game progress.
        Raises:
            ValueError: player's input does not match an item in the move_options 
                list.
        Returns:
            move (str): the player's move.
        """
        self.data = data
        print(data)
        human_player_move = input(f"{self.name}, select a move: {self.choice}")
        
        if human_player_move in self.options:
            return human_player_move
        else:
            raise ValueError("you must select a valid move")

class ComputerPlayer (HumanPlayer):   
    def move(self, data):
        self.data = data
        computer_player_move = random.choice(self.options)
        return computer_player_move
        # VS Code tells me this is unreachable, I don't know if that's true but can someone check
        super().move(data)

class HorrorGame():
    def __init__(self, human_name, computer_name):
        self.human_player = HumanPlayer(human_name, ["attack", "defend yourself"])
        self.computer_player = ComputerPlayer(computer_name, ["attack", "defend yourself"])
        self.level = 1
        self.human_health = 100
        self.computer_health = 100
        self.game_over = False
    
    def run(self):
        #I'm going to leave basic print statements for the text, narration part of the game
        #Can someone please change these to match the story lore

        print("Welcome to this Survival Game")
        print("You wake up in a dark, locked room...")

        while not self.game_over:
            if self.level == 1:
                self.level_1()
            if self.level == 2:
                self.level_2()
        
        self.the_winner()
    
    def level_1(self):
        # might not access the values I thought it would
        print("This is Level 1, {self.human_player.name} vs the {self.computer_player.name}")
        while self.human_health > 0 and self.computer_health > 0:
            self.human.move()
            self.computer.move()
        # conditional expression
        self.game_over = True if self.human_health <= 0 or self.computer_health <= 0 else False
        if self.game_over is True:
            print("The game ended, one the players did not survive")
            break

        #this conditional expressionmight not work, rewrite potentially
        self.level = 2 if self.human_health > 0 and self.computer_health > 0 else self.level

    #make sure to incorporate the monster method if the user makes it to level2
    def level_2(self):
        print("Welcome to level 2!")
        while self.human_player > 0 and self.computer_health >0:
            self.human_player_move()
            self.computer.move()
            
            m_damage=monster()
            self.human_health=self.human_health-m_damage
            print(f"An attack by a monster! Your current health status remains at: {playerHealth}")
            if self.human_health ==0 and self.game_over is True:
                print("Game over")
            if self.computer_health==0 and self.game_over is True:
                print("Good job! Continue onto next level")
        
        
        #Notes:    
        #Use f strings
        #human vs the monster
        #while human_health >0 then the human will keep moving
        #keep generating the monster damage
        #
        
        pass

    #if the human attacks computer, print computer health, if the human defends, print that we defended
    def human_move(self):
        pass

    #if the computer attacks human, print human health and if the computer defends, print that it defended
    def computer_move():
        pass

    def the_winner(self):
        who_won = winner(self.human_health, self.computer_health)
        if who_won:
            print(who_won)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "A Horror Game")
    parser.add_argument("--player", help = "Name of the human player", required = True)
    parser.add_argument("--computer", help = "Name of the computer player", default = "Computer Player")
    
    args = parser.parse_args()
    game = HorrorGame(args.player, args.computer)
    game.run()
