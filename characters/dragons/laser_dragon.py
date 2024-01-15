from .thrower_dragon import ThrowerDragon


class LaserDragon(ThrowerDragon):
    # This class is optional. Only one test is provided for this class.

    name = 'Laser'
    food_cost=10
    damage=2
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN 4.5
    implemented = True  # Change to True to view in the GUI

    # END 4.5

    def __init__(self, armor=1):
        ThrowerDragon.__init__(self, armor)
        self.fighters_shot = 0

    def fighters_in_front(self, skynet):
        # BEGIN 4.5
        fighter_positions={}
        place=self.place
        for terminator in place.terminators:
            fighter_positions[terminator]=0
        dragon=place.dragon
        if str(dragon.__class__.__name__)=='BodyguardDragon':
            fighter_positions[dragon]=0
        place=place.entrance
        i=1
        while place!=skynet:
            for terminator in place.terminators:
                fighter_positions[terminator]=i
            dragon=place.dragon
            if str(dragon.__class__.__name__)=='BodyguardDragon':
                fighter_positions[dragon]=i
                if dragon.contained_dragon is not None:
                    fighter_positions[dragon.contained_dragon]=i
            elif dragon is not None:
                fighter_positions[dragon]=i
            place=place.entrance
            i+=1
        return fighter_positions
        # END 4.5

    def calculate_damage(self, distance):
        # BEGIN 4.5
        damage=self.damage-(0.2*distance+0.05*self.fighters_shot)
        return damage
        # END 4.5

    def action(self, colony):
        fighters_and_distances = self.fighters_in_front(colony.skynet)
        for fighter, distance in fighters_and_distances.items():
            damage = self.calculate_damage(distance)
            fighter.reduce_armor(damage)
            if damage:
                self.fighters_shot += 1
