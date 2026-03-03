class Enimy:
    def __init__(
        self,
        type_of_enimy,
        attacking_damage,
        health_points,
    ):
        self.attacking_damage = attacking_damage
        self.health_points = health_points
        self.type_of_enimy = type_of_enimy

    def talk(self):
        print(f"{self.type_of_enimy} closer to you")

    def move_forward(self):
        print(f"{self.type_of_enimy} moves closer to you")

    def attack(self):
        print(f"{self.type_of_enimy} attack to {self.attacking_damage} damage")


class Zombie(Enimy):
    def __init__(
        self,
        attacking_damage,
        health_points,
    ):
        super().__init__(
            type_of_enimy="zombiexs",
            attacking_damage=attacking_damage,
            health_points=health_points,
        )

    def talk(self):
        super().talk()
        print("zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz")  # method over riding

    def desease(self):
        print("desease spreading")
