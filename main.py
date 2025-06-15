from random import choice

from gladiators.person import Person
from all_person import generate_person


def main():
    persons = []
    print("Создание персонажей:")
    added_names = set()
    for __ in range(10):
        person = generate_person(added_names)

        added_names.add(person.name)
        persons.append(person)
        print("Создан персонаж:", person.get_full_name())
        for thing in person.things:
            print(f"--- {thing}")

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


def get_attaker(defender: Person, persons):
    while True:
        attaker = choice(persons)
        if defender != attaker:
            break
    return attaker


if __name__ == "__main__":
    main()
