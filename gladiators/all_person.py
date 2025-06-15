from random import choice

from thing_type import ThingType, all_thing_type
from thing import Thing
from gladiators.person import Person
from gladiators.paladin import Paladin
from gladiators.warrior import Warrior

_all_person = (Person, Paladin, Warrior)


def _get_class_person() -> Person:
    """
    Получить рандомный класс персонажа

    Returns:
        Person: класс персонажа
    """
    return choice(_all_person)


def generate_person(added_names: set[str]) -> Person:
    """
    Создать персонажа

    Args:
        added_names: добавленные имена

    Returns:
        Person: Персонаж
    """
    cls_person = _get_class_person()
    person = cls_person(added_names)

    added_thing, added_thing_type = [], set()
    for __ in range(4):
        thing_type = choice(all_thing_type)
        while thing_type in added_thing_type:
            thing_type = choice(all_thing_type)
        added_thing_type.add(thing_type)
        thing = Thing(thing_type)
        added_thing.append(thing)

    person.set_things(added_thing)
    return person


def generate_10_person() -> list[Person]:
    """
    Сгенерировать 10 персонажей

    Returns:
        list: 10 персонажей
    """
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
    return persons
