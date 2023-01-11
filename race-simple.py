class Track():
	pass

class SpaceShip():
	pass


track1 = Track(2000)
spaceShip1 = SpaceShip("space1", 5) # km/h
spaceShip2 = SpaceShip("space2", 6)
spaceShip3 = SpaceShip("space3", 3)
spaceShip4 = SpaceShip("space4", 8)
spaceShip5 = SpaceShip("space5", 2)

track1.addSpaceShip(spaceShip1) # do the same for remaining spaceship

track1.startRace()

print(track1.whoWins()) # display space4