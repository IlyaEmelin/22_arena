from thing_type import ThingType

class Thing:
    """Предмет"""
    name: str
    percent_protection: float  # процент защиты
    attack: float  # атаку
    life: float  # жизнь
    thing_type: ThingType