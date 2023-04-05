from data_structures.stack.stack import Stack


class AnimalShelter:
    def __init__(self):
        self.cats = []
        self.dogs = []
        self.front = None
        self.rear = None
        # self.length = 0

    def enqueue(self, animal):
        species = animal.species
        if species == 'cat':
            self.cats.append(animal)

        if species == 'dog':
            self.dogs.append(animal)

        # When doing it as a queue
        # if self.is_empty():
        #     self.front = animal
        #     self.rear = animal
        #
        # if not self.is_empty():
        #     self.rear.next = animal
        #     self.rear = animal

    def dequeue(self, pref):
        if pref == 'dog':
            popped = self.dogs.pop()
            return popped

        if pref == 'cat':
            popped = self.cats.pop()
            return popped

        # Doing it as a queue
        # if self.is_empty():
        #     return 'The animal queue is empty'
        #
        # if pref != 'dog' or pref != 'cat':
        #     return None
        #
        # temp_front = self.front
        #
        # while True:
        #     if self.front.species == pref and self.front == temp_front:
        #         return_animal = self.front
        #         self.front = self.front.next
        #         return return_animal
        #     elif self.front.species == pref:
        #         return_animal = self.front
        #         self.front = self.front.next

        #         if self.front == temp_front:
        #           return return_animal
        #         else:
        #           while self.front != temp_front:
        #               temp = self.front
        #               self.front = self.front.next
        #               self.enqeueue(temp)
        #           return return_animal
        #
        #     if self.front.species != pref:
        #         temp = self.front
        #         self.front = self.front.next
        #         self.enqueue(temp)

    def is_empty(self):
        pass


class Animal:
    def __init__(self, name, species='Dog'):
        self.name = name
        self.species = species


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
