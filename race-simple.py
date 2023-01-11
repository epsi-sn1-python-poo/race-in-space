class Track():

    def add_space_ship(self, space_ship):
        pass  # todo

    def start_race(self):
        pass  # todo

    def who_wins(self):
        pass  # todo


class SpaceShip():

    def __init__(self, name, speed):
        self._name = name
        self._speed = speed

    def get_name(self):
        return self._name

    def __repr__(self):
        return f'{self._name}: {self._speed} km/h'


track1 = Track()  # todo
spaceShip1 = SpaceShip("space1", 5)  # km/h
spaceShip2 = SpaceShip("space2", 6)
spaceShip3 = SpaceShip("space3", 3)
spaceShip4 = SpaceShip("space4", 8)
spaceShip5 = SpaceShip("space5", 2)

print(spaceShip1)

track1.add_space_ship(spaceShip1)  # do the same for remaining spaceship

track1.start_race()

print(track1.who_wins())  # display space4
