class Hero:
    def __init__(self,name,hp=100):
        self.name = name
        self.hp = hp

    def take_damage(self, amount):
        self.hp -= amount
        print("Subtracted", amount,"HP", "from", self.name)
        print("Final HP is:", self.hp)


hero1 = Hero("Arthur")
hero1.take_damage(10)


hero2 = Hero("Morgana")
hero2.take_damage(0)
