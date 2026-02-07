from typing import TypedDict

class Person(TypedDict):
    
    name: str
    age: int

new_person: Person = {'name': 'nitish', 'age': 35}
# new_person: Person = {'name': 'nitish', 'age': '35'}
# This is also allows you at the runtime also

print(new_person)
