class Soldier:

    def __init__(self, name, model_of_weapon):
        self.name = name
        self.model_of_weapon = model_of_weapon



class Act_of_Shooting(Soldier):

    def __init__(self, name, model_of_weapon):
        self.name = name
        self.model_of_weapon = model_of_weapon


    def fire(self):
        print('{} tigi-tigitishh'.format(self.name))

    def guns_fire(self):
        print('{} fire bullets'.format(self.model_of_weapon))

    def fill_bullets(self, numb_of_bullets):
        print('{} reloads {} bullets'.format(self.name,numb_of_bullets))

ryan = Act_of_Shooting('Ryan', 'AK47')
ryan.fire()
ryan.guns_fire()
ryan.fill_bullets(20)

