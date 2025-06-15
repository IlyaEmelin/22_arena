from person import Person


class Paladin(Person):
    """Класс паладина."""

    def __init__(
            self,
            name: str,
            health: int,
            base_attack: int,
            base_defense: float,
    ) -> None:
        super().__init__(
            name=name,
            health=health * 2,
            base_attack=base_attack,
            base_defense=base_defense * 2,
        )

        def __str__(self) -> str:
            """Строковое представление."""
            return f"[Паладин] {super().__str__()}"
