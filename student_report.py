class Student:
  def __init__(self, name, age, gender):
    self.name = name
    self.age = age
    self.gender = gender
  
  def get_grade(self, grade):
    self.grade =grade
    return grade

class Course:
  def __init__(self, name, max_students) :
     self.name = name
     self.max_students = max_students
     self.students = []
     
  def add_student(self, student):
    if len(self.students) < self.max_students:
        self.students.append(student)
        return True
    return False
  
  def get_average_grade(self):
     value=0
     for student in self.students:
        value += student.get_grade()
      
     return value / len(self.students)

s1 = Student("Johnny", 19, 95)
s2 = Student("Ben",20, 78)
s3 = Student("Kelly", 19, 70)

course = Course("Science", 2)
course.add_student(s1)
course.add_student(s2)
course.add_student(s3)
print(course.get_average_grade())
