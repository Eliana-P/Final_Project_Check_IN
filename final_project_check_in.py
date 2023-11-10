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

def winner(playerHealth, computerHealth):
    """Returns the winner of the game.
    
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
