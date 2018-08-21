class PartyAnimal:
    x=0

    def __init__(self):
        print('I ama constructed')

    def party(self) :
        self.x = self.x + 1
        print('So far', self.x)

an = PartyAnimal()
an.party()
an.party()
an.party()
an.party()
an.party()
