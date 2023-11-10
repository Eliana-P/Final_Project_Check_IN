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




def winner(self, playerHealth, computerHealth):
    """Compares the players health to the computer's helth to determine the winner."
    """
    if playerHealth == None:
        if computerHealth == True:
            return "Computer won!"
    if computerHealth == None:
        if playerHealth == True:
            return "Player won!"