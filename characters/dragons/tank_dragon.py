from .bodyguard_dragon import BodyguardDragon


class TankDragon(BodyguardDragon):
    """TankDragon provides both offensive and defensive capabilities."""

    name = 'Tank'
    damage = 1
    food_cost=6
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN 3.3
    implemented = True  # Change to True to view in the GUI

    def __init__(self,armor=2):
        BodyguardDragon.__init__(self,armor)

    # END 3.3

    def action(self, colony):
        # BEGIN 3.3
        "*** YOUR CODE HERE ***"
        copy_terminators=self.place.terminators.copy()
        for terminator in copy_terminators:
            terminator.reduce_armor(self.damage)
        if self.contained_dragon is not None:
            self.contained_dragon.action(colony)
        
