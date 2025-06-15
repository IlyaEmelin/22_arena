from gladiators.person import Person


class Warrior(Person):
    """Класс паладина."""

    def __init__(self) -> None:
        super().__init__()
        self.base_attack = self.base_attack * 2

        def __str__(self) -> str:
            """Строковое представление."""
            return f"[Паладин] {super().__str__()}"
