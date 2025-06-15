from random import choice, uniform

from thing_type import ThingType
from thing import Thing, generate_item

_names = (
    "Алариэль",
    "Селестинара",
    "Элариондар",
    "Лираэльна",
    "Брандарсон",
    "Ариаднара",
    "Кэл’ариэль",
    "Эльрианора",
)


class Person:
    """Класс персонажа"""

    def __init__(self) -> None:
        """Базовый класс персонажа."""
        self.name = choice(_names)
        self.health = uniform(100, 1000)
        self.base_attack = uniform(10, 50)
        self.base_defense = uniform(0.01, 0.1)
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
            raise Exception("total_defense > 1")
        self.damage = attack * (1 - total_defense)
        self.health -= self.damage

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

