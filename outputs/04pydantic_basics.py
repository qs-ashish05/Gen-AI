from pydantic import BaseModel

class Student(BaseModel):
    name: str
    roll_num: int

new_student = {
    "name": "ashish",
    "roll_num": 404
}

# new_student = {
#     "name": 20,
#     "roll_num": 404
# }

s1 = Student(**new_student)

print(s1)
print(type(s1))


##https://github.com/campusx-official/langchain-structured-output/blob/main/pydantic_demo.py
