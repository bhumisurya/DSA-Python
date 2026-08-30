class Employee:
    def __init__(self,name):
        self.name = name

class Developer(Employee):
    def __init__(self,name,language):
        super().__init__(name)
        self.language = language

developer = Developer("Bhumika","Python")
print(developer.name)
print(developer.language)