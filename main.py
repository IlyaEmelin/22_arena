from random import choice

from thing_type import ThingType
from thing import Thing, generate_item
from person import Person
from all_person import generate_person


def main():
    persons = []
    print("Создание персонажей:")
    for __ in range(10):
        person = generate_person()
        print("Создан персонаж:", person)
        persons.append(person)

    while len(persons) >= 2:

        defender_index = choice(range(len(persons)))
        defender = persons[defender_index]
        attaker = get_attaker(defender, persons)

        attack = attaker.calculate_attack()
        life, damage = defender.take_damage(attack)
        if not life:
            persons.pop(defender_index)

        print(
            (
                f"Пользователь {attaker} "
                f"нанес урон {defender}, в размере {damage:.0f}"
            )
        )

    print("Победитель:", persons[0])


def get_attaker(defender: Person, persons):
    while True:
        attaker = choice(persons)
        if defender != attaker:
            break
    return attaker


if __name__ == "__main__":
    main()
