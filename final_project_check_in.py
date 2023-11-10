"""survival game"""




def winner(self, playerHealth, computerHealth):
    """Compares the players health to the computer's helth to determine the winner."
    """
    if playerHealth == None:
        if computerHealth == True:
            return "Computer won!"
    if computerHealth == None:
        if playerHealth == True:
            return "Player won!"
        
def human_player_move(self, data):
    """Asks the human player to make their next move.

    Args:
        data (list of str): game progress.

    Raises:
        ValueError: player's input does not match an item in the move_options 
            list.

    Returns:
        move (str): the player's move.
    """
    self.data = data
    move = input(f"{self.name}, select your next move: {self.move_options}")
    if move in self.move_options:
        return move
    else:
        raise ValueError("you must select a valid move")