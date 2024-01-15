from utils import *
from ..fighter import Fighter
from .dragon import Dragon
from .thrower_dragon import ThrowerDragon
from .scuba_thrower import ScubaThrower
from .bodyguard_dragon import BodyguardDragon


class DragonKing(ScubaThrower):  # You should change this line
    # END 4.3
    """The King of the colony. The game is over if a terminator enters his place."""

    name = 'King'
    food_cost=7
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN 4.3
    implemented = True  # Change to True to view in the GUI
    doubled_dragons=[]
    instantiated=False
    # END 4.3

    def __init__(self, armor=1):
        # BEGIN 4.3
        "*** YOUR CODE HERE ***"
        ScubaThrower.__init__(self,armor)
        if self.instantiated==False:
            self.true_dragon_king=True
            DragonKing.instantiated=True
        else:
            self.true_dragon_king=False#impostor
        
        
        # END 4.3

    def action(self, colony):
        """A dragon king throws a stone, but also doubles the damage of dragons
        in his tunnel.

        Impostor kings do only one thing: reduce their own armor to 0.
        """
        # BEGIN 4.3
        "*** YOUR CODE HERE ***"
        if self.true_dragon_king:
            ThrowerDragon.action(self,colony)
            place=self.place.exit
            while place!=None:
                dragon=place.dragon
                if dragon is not None:
                    if not dragon in self.doubled_dragons :
                        dragon.damage=dragon.damage*2
                        self.doubled_dragons.append(dragon)
                        if isinstance(dragon,BodyguardDragon):
                            dragon=dragon.contained_dragon
                            if dragon is not None:
                                if not dragon in self.doubled_dragons :
                                    dragon.damage=dragon.damage*2
                                    self.doubled_dragons.append(dragon)
                    else:
                        if isinstance(dragon,BodyguardDragon):
                            dragon=dragon.contained_dragon
                            if dragon is not None:
                                if not dragon in self.doubled_dragons :
                                    dragon.damage=dragon.damage*2
                                    self.doubled_dragons.append(dragon)
                place=place.exit
        else:
            self.reduce_armor(self.armor)
                
            
            
        # END 4.3

    def reduce_armor(self, amount):
        """Reduce armor by AMOUNT, and if the True DragonKing has no armor
        remaining, signal the end of the game.
        """
        # BEGIN 4.3
        "*** YOUR CODE HERE ***"
        if not self.true_dragon_king:
            Fighter.reduce_armor(self,amount)
        if self.true_dragon_king:
            self.armor-=amount
            terminators_win()
        
