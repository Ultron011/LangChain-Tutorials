from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str = "saurabh"
    age: Optional[int] = None
    email : EmailStr
    cgpa : float = Field(gt = 0, lt=10, default=5, description="Deicmal value representing the cgpa of the student")
    
    
new_student = {'age': 12, "email": "abc@gmail.com", "cgpa": 8.2}

student = Student(**new_student)

student_dict = dict(student)
student_json = student.model_dump_json()

print(student_dict)
print(student_json)