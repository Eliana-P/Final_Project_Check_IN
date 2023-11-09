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