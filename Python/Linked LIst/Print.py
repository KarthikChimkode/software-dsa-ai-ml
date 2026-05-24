#How to print 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Person {self.name} - {self.age}"
    
new_person = Person("Karthik", 23)
print(new_person)