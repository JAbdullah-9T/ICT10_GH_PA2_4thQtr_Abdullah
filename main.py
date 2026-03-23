# Object Oriental Programing
from pyscript import document, display


class petInfo:
        def __init__ (self, name, owner):
            self.name = name
            self.owner = owner
            
class petBreed(petInfo):
    def __init__ (self, breed):
            self.breed = breed
    
def displayInfo(e):
    output = document.getElementById("output")
    output.innerHTML = ""
    
    name = document.getElementById("name").value
    breed = document.getElementById("breed").value
    owner = document.getElementById("owner").value
            
    pet1 = petInfo(name, owner)
    breed1 = petBreed(breed)
    
    display(f'Name: {pet1.name}', target="output")
    display(f'Breed: {breed1.breed}', target="output")
    display(f'Owner: {pet1.owner}', target="output")


#class Family: 
#    def __init__(self, name, age, level, gender, school):
#        self.name = name #attributes
#        self.age = age #attributes
#        self.level = level #attributes
#        self.gender = gender #attributes
#        self.school = school #attributes


# Creating an Object/Instantiating an Object
#name1 = Family('Abdullah', 16, 'gr10', 'male', 'obmc')
#name2 = Family('Garcia', 16, 'gr10', 'male', 'obmc')

#display(f'{name1.name}, who is a {name1.gender}, is a part of the Family', target='output')
#display(f'{name2.name}, who is a {name2.gender}, is a part of the Family', target='output')


#class Cat:
#    def __init__(self, breed, age, name, owner):
#        self.breed = breed
#        self.age = age
#        self.name = name
#        self.owner = owner


#    def meow(self):
#        display('Meow! '*2, target='output')


#cat1 = Cat('Maine Coon', 6, 'Jack', 'Jalainie')
#cat1.meow()
#cat2 = Cat('Singapura', 7, 'Jenny', 'N/A')


#display(f'{cat1.name}, who is a {cat1.breed}, is owned by {cat1.owner}', target='output')
#display(f'{cat2.name}, who is a {cat2.breed}, is owned by {cat2.owner}', target='output')

# Creating a Child Class
#class PersianCat(Cat):
#    pass

#cat1 = PersianCat('Persian Cat', 7, 'Nero', 'Clara')

#display(f'{cat1.name}, who is a {cat1.breed}, is owned by {cat1.owner}', target='output')