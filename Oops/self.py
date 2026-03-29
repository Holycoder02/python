class Student:
    def set_details(self, name, marks):
        self.name = name
        self.marks = marks
    
student1 = Student()
student1.set_details('Raju', 85)
print(student1.name, student1.marks)