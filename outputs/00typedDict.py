from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int

new_person: Person = {
    'name': 'ashish',
    'age': 23
}

print(new_person)


another_person = {
    'name':'ashish',
    'age': '23'
}


print(another_person)