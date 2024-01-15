from .dragon import Dragon


class FireDragon(Dragon):
    """FireDragon cooks any Terminator in its Place when it expires."""

    name = 'Fire'
    damage = 3
    food_cost=5
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN 2.2
    implemented = True  # Change to True to view in the GUI

    # END 2.2

    def __init__(self, armor=3):
        """Create a Dragon with a ARMOR quantity."""
        Dragon.__init__(self, armor)

    def reduce_armor(self, amount):
        """Reduce armor by AMOUNT, and remove the FireDragon from its place if it
        has no armor remaining.

        Make sure to damage each terminator in the current place, and apply the bonus
        if the fire dragon dies.
        """
        # BEGIN 2.2
        "*** YOUR CODE HERE ***"
        self.armor-=amount
        copy_terminators=self.place.terminators.copy()
        for terminator in copy_terminators:
            if self.armor>0:
                terminator.reduce_armor(amount)
            else:
                total_damage=amount+self.damage
                terminator.reduce_armor(total_damage)
        if self.armor<=0:
            self.place.remove_fighter(self)
            self.death_callback()
    
            
            
        
        
        
