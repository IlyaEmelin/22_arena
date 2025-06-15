from gladiators.person import Person


class Warrior(Person):
    """Класс воин"""

    def __init__(self, added_names: set[str]) -> None:
        super().__init__(added_names)
        self.base_attack = self.base_attack * 2

    def __str__(self) -> str:
        """Строковое представление."""
        return f"Войн {self.get_name()}"
