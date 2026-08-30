class Person:
    def speak(self):
        print("Speaking")

class Employee(Person):
    def work(self):
        print("Working")

class Developer(Person):
    def code(self):
        print("Coding")

a = Employee()
a.speak()
a.work()


b = Developer()
b.speak()
b.code()
