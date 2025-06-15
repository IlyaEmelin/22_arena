from random import choice, uniform

from thing_type import ThingType
from thing import Thing, generate_item


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
            raise Exception("total_defense > 1")
        damage = attack * (1 - total_defense)
        self.health -= int(damage)

        print(
            f"""{self.name} получил {int(damage)} урона.
            Осталось HP: {self.health}"""
        )

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


names = (
    "Алариэль",
    "Селестинара",
    "Элариондар",
    "Лираэльна",
    "Брандарсон",
    "Ариаднара",
    "Кэл’ариэль",
    "Эльрианора",
)


def generate_person():
    person = Person(
        choice(names),
        uniform(100, 1000),
        uniform(0.01, 0.1),
        uniform(10, 50),
    )

    added_thing = list()
    added_thing_type = set()
    count = 0
    while True:
        thing_type = choice(ThingType.all)
        if thing_type in added_thing_type:
            continue
        added_thing_type.add(thing_type)

        thing = generate_item(thing_type)
        added_thing.append(thing)
        count += 1
        if count > 4:
            break
    person.set_things(added_thing)
    return person
