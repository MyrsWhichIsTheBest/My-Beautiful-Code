class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade

    def get_name(self):
        return self.name


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            print(f"Entered into class!")
            return True
        print("Class is Full!")
        return False

    def get_average_grade(self):
        total = 0
        for student in self.students:
            total += student.get_grade()
        return total / len(self.students)


s1 = Student("Janelle Hollis", 16, 65)
s2 = Student("Janice Burbroke", 17, 95)
s3 = Student("Taane Pairama", 15, 2)

course1 = Course("Computer Science", 3)
course2 = Course("English LIT", 160)

course1.add_student(s1)
course1.add_student(s2)
print(course1.add_student(s3))

print(f"The Average Grade in {course1.name} is {course1.get_average_grade()}")

