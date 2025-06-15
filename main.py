from random import choice

from gladiators.person import Person
from gladiators.all_person import generate_person, generate_10_person


def main():
    """
    Класс игры
    """
    persons = generate_10_person()
    print("--- Да начнется битва!!! ---")
    while len(persons) >= 2:
        defender_index = choice(range(len(persons)))
        defender = persons[defender_index]
        attaker = get_attaker(defender, persons)

        attack = attaker.calculate_attack()
        life, damage = defender.take_damage(attack)
        if not life:
            persons.pop(defender_index)
            print(
                f"{attaker} убил {defender}, "
                f"нанеся урон в размере {damage:.0f}"
            )
        else:
            print(f"{attaker} нанес урон {defender}, в размере {damage:.0f}")

    print("Победитель:", persons[0])


def get_attaker(defender: Person, persons) -> Person:
    """
    Получить атакующего персонажа

    Args:
        defender: защищающийся персонаж
        persons: все персонажи

    Returns:
        Person: атакующий персонаж
    """
    while True:
        attaker = choice(persons)
        if defender != attaker:
            break
    return attaker


if __name__ == "__main__":
    main()
