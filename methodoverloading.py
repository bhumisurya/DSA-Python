class Calculator:
    def add(self, *args):
        return sum(args)

a = Calculator()

print(a.add(100))
print(a.add(100,20))
print(a.add(100,500,456))
