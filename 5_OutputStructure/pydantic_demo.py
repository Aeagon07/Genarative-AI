from pydantic import BaseModel, EmailStr, Field
from typing import Optional

# field fuction is used for the setting the constraint
class Student(BaseModel):
    name: str = 'nitesh'
    # this how you set the default values..
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt= 0, lt= 10, default=5)

new_student = {'age': '32', 'email': 'abc@gmail.com', 'cgpa': 5}
# this will through you an error cause you define the eamil is EmailStr but you can not write anything like @gmail.com that why.. => these are the Built-Validation in the pydyantic 

# But the pydyantic is samrt enogh that it convert the string and get the number in the string into the interger formate => You called it as the Coerce 

student = Student(**new_student)


# print(student.name)
#In Dictionary formate 
student_dict = dict(student)
print(student_dict['age'])

student_json = student.model_dump_json() # creating the JSON