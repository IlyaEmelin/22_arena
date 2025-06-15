from enum import Enum, auto


class SubtypeThing(Enum):
    """
    Подтип предметов защитные атакующие, увеличивающие количество жизней и др.
    """

    def __init__(
        self,
        attack_multiplier,
        defense_multiplier,
        health_multiplier,
    ):
        self.attack_multiplier: float = attack_multiplier
        self.defense_multiplier: float = defense_multiplier
        self.health_multiplier: float = health_multiplier

    DEFENDER = (0.0, 1.0, 0.0)
    ATTACKERS = (1.0, 0.0, 0.0)
    HEALERS = (0.0, 0.0, 1.0)
    ULTIMATUMS = (0.7, 0.7, 0.7)


class ThingType(Enum):
    """Типы предметов"""

    def __init__(
        self, thing_name, all_full_names, subtype
    ):
        self.thing_name: str = thing_name
        self.all_full_names: list[str] = all_full_names
        self.subtype: SubtypeThing = subtype

    RING = (
        "Кольцо",
        [
            "Кольцо всевластья",
            "Золотое кольцо",
            "Серебренное кольцо",
        ],
        SubtypeThing.ULTIMATUMS,
    )
    PANTS = (
        "Штаны",
        (
            "Хлопковые штаны",
            "Кожаные штаны",
            "Железные штаны",
            "Пояс верности",
        ),
        SubtypeThing.DEFENDER,
    )
    JACKET = (
        "Куртка",
        (
            "Хлопковая куртка",
            "Кожаная куртка",
            "Железная куртка",
            "Золотая кираса",
        ),
        SubtypeThing.DEFENDER,
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
        SubtypeThing.DEFENDER,
    )
    SHOES = (
        "Обувь",
        (
            "Сапоги скороходы",
            "Домашние тапочки",
            "Кожаные ботинки",
            "Железные ботинки",
        ),
        SubtypeThing.DEFENDER,
    )
    GLOVES = (
        "Перчатки",
        (
            "Кружевные  перчатки",
            "Кожанные перчатки",
            "Железные перчатки",
            "Титановые варежки",
        ),
        SubtypeThing.DEFENDER,
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
        SubtypeThing.ATTACKERS,
    )


all_thing_type = list(ThingType)
