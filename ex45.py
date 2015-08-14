class IconicStop(object):

    def once_there(self):
        pass


class IPhone(object):

    def __init__(self, iconic_stop_directions):
        pass

    def play(self):
        pass


class OceanBeach(IconicStop):

    def once_there(self):
        pass


class DuboceTriangle(IconicStop):

    def once_there(self):
        pass


class Tartine(IconicStop):

    def once_there(self):
        pass


class Hearth(IconicStop):

    def once_there(self):
        pass


class Map(object):

    def __init__(self, starting_point):
        pass

    def next_stop(self, iconic_stop_name):
        pass

    def first_iconic_stop(self):
        pass

# To run the game
directions = Map('ocean_beach')
game = IPhone(directions)
game.play()
