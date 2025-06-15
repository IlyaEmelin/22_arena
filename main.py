from random import choice

from thing_type import ThingType
from thing import Thing, generate_item
from Person import generate_person

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    # Use a breakpoint in the code line below to debug your script.
    thing_type = choice(ThingType.all)
    print("thing_type:", thing_type)
    thing = generate_item(thing_type)
    print("thing:", thing)

    person = generate_person()
    print("person:", person)


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
