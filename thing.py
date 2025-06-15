from random import choice, uniform

from thing_type import ThingType


class Thing:
    """Предмет"""

    def __init__(self):
        self.name: str = None
        self.percent_protection: float = None  # процент защиты
        self.attack: float = None  # атаку
        self.life: float = None  # жизнь
        self.thing_type: ThingType = None  # тип предмета

    def __str__(self):
        return (
            f"{self.name} c защитой {self.percent_protection} "
            f"и атакой {self.attack} "
            f"и защитой {self.percent_protection}"
            f"и жизнью {self.life}"
        )


def generate_item(thing_type: ThingType) -> "Thing":
    new_thing = Thing()
    new_thing.name = choice(thing_type[1])
    new_thing.attack = uniform(1, 10)
    new_thing.life = uniform(10, 100)
    new_thing.thing_type = thing_type
    return new_thing
