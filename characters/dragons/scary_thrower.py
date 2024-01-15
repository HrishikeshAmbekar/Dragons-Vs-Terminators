from .thrower_dragon import ThrowerDragon
from utils import apply_effect, make_scare

class ScaryThrower(ThrowerDragon):
    """ThrowerDragon that intimidates Terminators, making them back away instead of advancing."""

    name = 'Scary'
    food_cost=6
    # BEGIN 4.4
    implemented = True  # Change to True to view in the GUI

    # END 4.4

    def throw_at(self, target):
        # BEGIN 4.4
        "*** YOUR CODE HERE ***"
        if target:
            if target.scared==False:
                apply_effect(make_scare, target, 2)
        # END 4.4
        
    def action(self,colony):
        self.throw_at(self.nearest_terminator(colony.skynet))
        
