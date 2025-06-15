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


def generate_person():
    cls_person = _get_class_person()
    person = cls_person()

    added_thing = list()
    added_thing_type = set()
    count = 0
    while True:
        thing_type = choice(all_thing_type)
        if thing_type in added_thing_type:
            continue
        added_thing_type.add(thing_type)

        thing = Thing(thing_type)
        added_thing.append(thing)
        count += 1
        if count > 4:
            break
    person.set_things(added_thing)
    return person
