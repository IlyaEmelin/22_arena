from gladiators.person import Person


class Paladin(Person):
    """Класс паладина."""

    def __init__(self) -> None:
        super().__init__()
        self.base_defense = self.base_defense * 2
        self.health = self.health * 2

        def __str__(self) -> str:
            """Строковое представление."""
            return f"[Паладин] {super().__str__()}"
