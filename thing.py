from random import choice, uniform

from thing_type import ThingType


class Thing:
    """Предмет"""

    def __init__(self, thing_type: ThingType):
        self.name: str = choice(thing_type.all_full_names)

        subtype = thing_type.subtype
        self.percent_protection = subtype.defense_multiplier * uniform(
            0.01, 0.1
        )
        self.attack = subtype.attack_multiplier * uniform(1, 10)
        self.life = subtype.health_multiplier * uniform(10, 100)
        self.thing_type = thing_type

    def __str__(self):
        return (
            f"{self.name} "
            f" и атакой {self.attack:.0f} "
            f" и защитой {self.percent_protection:.2f}"
            f" и жизнью {self.life:.0f}"
        )
