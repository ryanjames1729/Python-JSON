import json
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int
    grade_level: int

# 1. Load the file (json.load will return a list of dictionaries)
with open('data.json', 'r') as file:
    raw_data = json.load(file)

# 2. Use a list comprehension to transform dictionaries into Student objects
students = [Student(**item) for item in raw_data]

# 3. You can now access them like a standard Python list
for student in students:
    print(f"{student.name} is in grade {student.grade_level}")

