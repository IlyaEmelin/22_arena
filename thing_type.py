from enum import Enum, auto


class SubtypeThing(Enum):
    def __init__(
        self,
        attack_multiplier,
        defense_multiplier,
        health_multiplier,
    ):
        self.attack_multiplier = attack_multiplier
        self.defense_multiplier = defense_multiplier
        self.health_multiplier = health_multiplier

    DEFENDER = (0.0, 1.0, 0.0)
    ATTACKERS = (1.0, 0.0, 0.0)
    HEALERS = (0.0, 0.0, 1.0)
    ULTIMATUMS = (0.5, 0.5, 0.5)


class ThingType(Enum):
    """Типы предметов"""

    def __init__(
        self,
        thing_name,
        all_full_names,
    ):
        self.thing_name = thing_name
        self.all_full_names = all_full_names

    RING = (
        "Кольцо",
        ["Кольцо всевластья", "Золотое кольцо", "Серебренное кольцо"],
    )
    PANTS = (
        "Штаны",
        (
            "Хлопковые штаны",
            "Кожаные штаны",
            "Железные штаны",
            "Пояс верности",
        ),
    )
    JACKET = (
        "Куртка",
        (
            "Хлопковая куртка",
            "Кожаная куртка",
            "Железная куртка",
            "Золотая кираса",
        ),
    )
    HAT = (
        "Шапка",
        (
            "Вязаная шапочка",
            "Красная шапочка",
            "Кожаная шапочка",
            "Хлопковая шапка",
            "Железная шапка",
        ),
    )
    SHOES = (
        "Обувь",
        (
            "Сапоги скороходы",
            "Домашние тапочки",
            "Кожаные ботинки",
            "Железные ботинки",
        ),
    )
    GLOVES = (
        "Перчатки",
        (
            "Кружевные  перчатки",
            "Кожанные перчатки",
            "Железные перчатки",
            "Титановые варежки",
        ),
    )
    WEAPON = (
        "Оружие",
        (
            "Меч кладенец",
            "Железные меч",
            "Деревянный меч",
            "Каменный меч",
            "Железное копье",
        ),
    )


all_thing_type = list(ThingType)
