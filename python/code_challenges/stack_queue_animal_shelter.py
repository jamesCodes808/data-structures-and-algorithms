from data_structures.stack.stack import Stack


class AnimalShelter:
    def __init__(self):
        self.cats = []
        self.dogs = []
        self.head = None
        self.rear = None
        # self.length = 0

    def enqueue(self, animal):
        species = animal.species
        if species == 'cat':
            self.cats.append(animal)

        if species == 'dog':
            self.dogs.append(animal)

    def dequeue(self, pref):
        if pref == 'dog':
            popped = self.dogs.pop()
            return popped

        if pref == 'cat':
            popped = self.cats.pop()
            return popped


class Dog:
    def __init__(self):
        # self.name = ''
        # self._next = _next
        self.species = 'dog'

class Cat:
    def __init__(self):
        # self.name = ''
        # self._next = _next
        self.species = 'cat'

if __name__ == '__main__':
    new_dog = Dog()
