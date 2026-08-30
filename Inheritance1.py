class Person:
    def speak(self):
        print("Speaking")

class Employee(Person):
    def work(self):
        print("Working")

a = Employee()
a.speak()
a.work()