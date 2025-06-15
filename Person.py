class Person:
    """Класс персонажа"""

    def __init__(
            self,
            name: str,
            health: int,
            base_attack: int,
            base_defense: float,
    ) -> None:
        """Базовый класс персонажа."""
        self.name = name
        self.health = health
        self.base_attack = base_attack
        self.base_defense = base_defense
        self.things = []

    def set_things(self, things: list):
        """Метод, принимающий на вход список вещей."""
        self.things = things

        for thing in self.things:
            self.health += thing.life

    def take_damage(self, attack: int):
        """Метод вычитания жизни на основе входной атаки."""
        total_defense = self.base_defense

        for thing in self.things:
            total_defense += thing.percent_protection

        if total_defense > 1:
            raise Exception('total_defense > 1')
        damage = attack * (1 - total_defense)
        self.health -= int(damage)

        print(f'''{self.name} получил {int(damage)} урона.
            Осталось HP: {self.health}''')

        return self.health > 0

    def calculate_attack(self) -> int:
        """Общая атака с учетом вещей."""
        total_attack = self.base_attack
        for thing in self.things:
            total_attack += thing.attack
        return total_attack

    def __str__(self) -> str:
        """Строковое представление персонажа"""
        return f"{self.name}: HP={self.health}"
