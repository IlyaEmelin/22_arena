from random import choice, uniform

from thing import Thing

_names = (
    "Алариэль",
    "Селестинара",
    "Элариондар",
    "Лираэльна",
    "Брандарсон",
    "Ариаднара",
    "Кэл’ариэль",
    "Эльрианора",
    "Добрыня Никитич",
    "Алёша Попович",
    "Святогор",
    "Микула Селянинович",
    "Садко",
    "Ставр Годинович",
    "Халк (Брюс Бэннер)",
    "Человек-паук (Питер Паркер)",
    "Доктор Стрэндж (Стивен Стрэндж)",
    "Соколиный глаз (Клинт Бартон)",
    "Капитан Марвел (Кэрол Дэнверс)",
    "Чёрная вдова (Наташа Романова)",
)


class Person:
    """Класс персонажа"""

    def __init__(self, added_names: set[str]) -> None:
        """
        гладиатор.

        Args:
            added_names: добавленные имена
        """
        """Базовый класс персонажа."""
        self.name = self.__generate_name(added_names)
        self.health = uniform(100, 400)
        self.base_attack = uniform(10, 50)
        self.base_defense = uniform(0.01, 0.1)
        self.things = []

    @staticmethod
    def __generate_name(added_names: set[str]) -> str:
        """
        Сгенерировать имя гладиатора

        Args:
            added_names: уже добавленные имена гладиаторов

        Returns:
            str: имя гладиатора
        """
        name = choice(_names)
        while name in added_names:
            name = choice(_names)
        return name

    def set_things(self, things: list[Thing]) -> None:
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
        self.health -= damage

        return self.health > 0, damage

    def calculate_attack(self) -> int:
        """Общая атака с учетом вещей."""
        total_attack = self.base_attack
        for thing in self.things:
            total_attack += thing.attack
        return total_attack

    def get_full_name(self) -> str:
        """
        Получить полное имя персонажа

        Returns:
            str: полное имя персонажа
        """
        return (
            f"{self.get_name()} "
            f"атакой: {self.base_attack:.0f} "
            f"защитой {self.base_defense:.2f}"
        )

    def get_name(self) -> str:
        """
        Получить имя персонажа

        Returns:
            str: имя персонажа
        """
        return f"{self.name}: HP={max(self.health, 0.):.0f}"

    def __str__(self) -> str:
        """Строковое представление персонажа"""
        return f"Гладиатор {self.get_name()}"
