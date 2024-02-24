import random

from data.data import Person
from faker import Faker

faker_en = Faker('En')


def generated_person():
    yield Person(
        full_name=faker_en.first_name() + " " + faker_en.last_name(),
        first_name=faker_en.first_name(),
        last_name=faker_en.last_name(),
        email=faker_en.email(),
        age=random.randint(1, 99),
        salary=random.randint(1, 9999999999),
        current_address=faker_en.street_address(),
        permanent_address=faker_en.street_address(),
        department=faker_en.job(),
    )


def generated_file():
    # path = rf'C:\Users\Denys\PycharmProjects\ui_test_fw_on_python\test_file{random.randint(0, 999)}.txt' #windows path
    path = rf'/Users/denys/PycharmProjects/ui_testing_fw_python/tests/test_file{random.randint(0, 999)}.txt' #mac path
    file = open(path, 'w+')
    file.write(f'Hello{random.randint(0, 999)}World{random.randint(0, 999)}')
    file.close()
    return file.name, path
