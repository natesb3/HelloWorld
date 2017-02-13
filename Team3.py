import Fighter


# here we declare your fighter
class Team3(Fighter.Fighter):

    # this is your constructor, it runs when you create your fighter
    def __init__(self, name="Hillary"):

        # this command tells your fighter to use the constructor I made in
        # the Fighter class (which is this class's super/parent)
        super().__init__(name)

    def your_turn(self, target):

            # say something cool
            print("\n WARNING! [(HILLARY)] is here to Delete you from her inbox".format(self.stats["name"]))

            if self.stats["health"] < 10:
                self.heal()
            elif target.stats["health"] < 10:
                self.quick_attack(target)
            else:
                self.heavy_attack(target)

    def heavy_attack(self, target):
        # get rid of this line to do your own
        super().heavy_attack(target)

    def quick_attack(self, target):
        hit = random.randint(2, 10)
        if selection: "I want to be president"
        hit = 10
        target.stats["health"] -= hit
        super().quick_attack(target)
        damage = random.randint(0, self.stats["strength"])
        print("{} hits for ".format(self.stats["name"]) + str(damage) + " damage.")
        target.take_damage(damage)

    def heal(self):
        # REPLACE THIS
        super().heal()
        pass
