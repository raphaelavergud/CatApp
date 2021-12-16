#!/usr/bin/env python3

# initialising the basic lists i need for this:

comfy_list = ['sofa', 'paper bag', 'bed', 'cat bed', 'cat tree']
catlist = []

# defining the cat class:

class Cat:
    def __init__(self, name, age, food, surface = ''):
        self.name = name
        self.age = age
        self.fav_food = food
        self.surface = surface

# calico class copies the parameters of the cat class but it has a meow method.

class Calico(Cat):
    def meow(self):
        if self.surface in comfy_list:
            return 'Meow, this is too comfortable....'
        else:
            return 'Meow! I love it here!'

# testing out the iterating over objects thing i found here: https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python
# getting the surface input for the last parameter in Cat class:

class Checker(): # this does not need to be a class, all it does is it has a method.
    # i want to use a class method here so it will return a cat object again.
    # i have yet to figure out how.
    def uncomfy_checker(self, catobject):
        catobject.surface_input = str(input(f'Where is {catobject.name} sitting right now? '))
        # formatting the input so it works with my program
        catobject.surface = catobject.surface_input.strip().lower()
        # checking the input against the list i made of comfortable surfaces
        if catobject.surface not in comfy_list:
            surface = 'uncomfortable'
        else:
            surface = 'comfortable'
        return f'{catobject.name} is sitting on: {catobject.surface}. It looks {surface}.'

# defining the objects and appending them to a list i keep of the objects

catlist.append(Cat('Samsa', 7, "Meat'n'Greets"))
catlist.append(Cat('Olga', 5, 'Cornflakes'))
catlist.append(Cat('Emily', 2, 'Fish'))

catlist.append(Calico('James', 12, 'Coffee'))

# testing by printing

for cat in catlist:
    result = Checker().uncomfy_checker(cat)
    print(result)
    # below code does not work yet!
    # if cat == Calico():
    #     print(Calico.meow(cat))

# right now the calico meow function works for all cats because of the code above,
# i want to change that still so only calicos do the meow thing.



