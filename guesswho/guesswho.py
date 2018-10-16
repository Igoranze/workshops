import yaml
from random import choice
from person import Person

options = {
    'sex': ('man', 'woman'),
    'eye_color': ('blue', 'brown'),
    'hair_color': ('black', 'brown', 'red', 'blond', 'white'),
    'nose_size': ('big', 'small'),
    'mouth_size': ('big', 'small'),
    'rosy_cheeks': (True, False),
    'bald': (True, False),
    'hat': (True, False),
    'glasses': (True, False),
    'moustache': (True, False),
    'beard': (True, False),
}

class Game:
    def __init__(self):
        self.people = {}
        self.data = yaml.safe_load(open('people.yml'))
        for name, person in self.data.items():
            self.people[name] = Person(name=name, **person)
    
    def pick_person(self):
        self.picked_person = choice(list(self.people))
        print(self.picked_person)

    def pick_ask_or_guess(self):
        print('1. Guess name')
        for index, o in enumerate(list(options)):
            print('{}. {}'.format(index+2, o))
        
        pick = int(input())
        if pick == 1:
            correct_guess = self.guess(input('Who do you think it is?'))
            if correct_guess:
                print('YOU WIN!')
            else:
                print('Guess was not correct!')
        else:
            print(self.ask(list(options)[pick-2]))

    def ask(self, characteristic):
        for index, o in enumerate(list(options[characteristic])):
            print('{}. {}'.format(index+1, o))
        return getattr(self.people[self.picked_person], characteristic) == options[characteristic][int(input())-1]

    def guess(self, name):
        return self.picked_person == name
