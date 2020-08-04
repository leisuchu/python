class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        self.hadWork = False

    def do_work(self):
        self.hadWork = True


class Teacher:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def check_work(self, student):
        if student.hadWork:
            return '做的不错！'
        else:
            return '给我站出去！'


student1 = Student('leiuchu', 6)
teacher = Teacher('leee', 6)
# student1.do_work()
print(teacher.check_work(student1))
