class Person:
    """Класс персонажа"""

    def __init__(
            self,
            name: str,
            health: int,
            base_attack: int,
            base_defense: float,
    ) -> None:
        self.name = name
        self.health = health
        self.base_attack = base_attack
        self.base_defense = base_defense
        self.things = []

    def set_things(self, things: list):
        """Метод, принимающий на вход список вещей."""
        self.things = things

    def take_damage(self, attack: int):
        """Метод вычитания жизни на основе входной атаки."""

    def calculate_total_attack(self):
        """Расчет итоговой атаки с учетом вещей"""

    def calculate_total_defense(self):
        """Расчет итоговой защиты с учетом вещей"""

    def is_alive(self):
        """Проверка, жив ли персонаж"""

    def __str__(self) -> str:
        """Строковое представление персонажа"""
        return f"{self.name}: HP={self.health}"
