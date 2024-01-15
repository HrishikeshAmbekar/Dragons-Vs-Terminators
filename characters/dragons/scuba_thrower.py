from .dragon import Dragon
from .thrower_dragon import ThrowerDragon

class ScubaThrower(ThrowerDragon):
    is_watersafe=True
    food_cost=6
    name="Scuba"
    implemented=True

    # ADD/OVERRIDE CLASS ATTRIBUTES HERE
    def __init__(self,armor=1):
        Dragon.__init__(self,armor)
    
        
        
