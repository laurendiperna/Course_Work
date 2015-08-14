# This is simple interactive game: the player wakes up with the intention to go hang out at Ocean Beach
# only to realize they need to gets some coffee first. What ensues are the silly trials and tribulations
# of living in San Francisco, namely that everything has a ridiculouly long line. The intention of the game
# was to practice building a few classes and passing variables.

from sys import exit
from random import randint

# This class gets overwritten by the classes later on which inherit from it. It was created so I could
# build a skeleton of the game using 'pass' in the classes so I wouldn't need to add content to them
# before completing my game outline


class IconicStop(object):

    # once_there is a method that prints out a description of
    # your location once you get there, and then enters the class
    # with that location's name
    def once_there(self):
        print 'you have arrived at your new destination'
        exit(1)


# the IPhone class is what runs your Map and provides the stops you need to hit, to arrive at your coffee destination
class IPhone(object):

    # initialized the self and iconic_stop_directions parameters/ IPhone() takes one variable iconic_stop_directions
    def __init__(self, iconic_stop_directions):
        self.iconic_stop_directions = iconic_stop_directions  # set iconic_stop_directions attribute to directions

    def play(self):
        current_stop = self.iconic_stop_directions.first_iconic_stop()  # get first_iconic_stop() w 'ocean_beach'.
        last_stop = self.iconic_stop_directions.next_stop('caffeine_success')  # returns the class CaffeineSuccess()

        while current_stop != last_stop:
            next_stop_name = current_stop.once_there()  # this should return a string of the stop name
            current_stop = self.iconic_stop_directions.next_stop(next_stop_name)  # this should return a class

        current_stop.once_there()  # this runs the final CaffeineSuccess class, otherwise it gets skipped


class HashtagSFFAIL(IconicStop):
    # eventually make this pull a quote for a specific type of fail
    fails = ["you would have remembered if the pink mustaches hadn't distracted you",
             "why did you get in the wrong uber?",
             "sometimes responding to a friend's text is a really good idea",
             ]

    def once_there(self):
        print HashtagSFFAIL.fails[randint(0, len(self.fails) - 1)]
        exit(1)


class OceanBeach(IconicStop):

    def once_there(self):
        print """
        You decided to spend the day at the beach,
        only to realize you forgot to drink your coffee...
        which is still steaming on your kitchen counter.
        'No prob' you think, 'I'll just hop the N Judah
        to Duboce Triangle and then walk to Tartine for
        a delicious cafe au lait!' So you walk over to the
        muni stop.
        """

        forgetful_or_not = raw_input('did you remember your clipper car? (yes/no) > ')

        if forgetful_or_not == 'no':
            return 'hashtagsffail'  # before => HashtagSFFAIL()
        elif forgetful_or_not == 'yes':
            print """
                phew! you get on muni and are on your way"""
            return 'duboce_triangle'


class DuboceTriangle(IconicStop):

    def once_there(self):
        print """
        You step out of the muni, pass the Duboce Triangle Cafe - resist the
        urge to buy coffee! You can make it! Tartine is only 15 minute
        walk away.

        Your phone buzzes with a text from your friend, but
        you're on a mission.
        """

        text_response = raw_input('want to check your phone? > (yes/no) ')

        if text_response == 'yes':
            print """
            Your friend tells you they are at Hearth and you
            should join. You think it over and decide, 'why not?'
            Hearth could be great.
            """
            return 'hearth'
        elif text_response == 'no':
            print """
            Good! Nothing should get in the way of your coffee!"""
            return 'tartine'


class Tartine(IconicStop):

    def once_there(self):
        print """
        At Tartine you are greeted by a massive line that
        wraps around the corner and shoots down the block.
        Unphased you stand in line.
        """
        waiting = raw_input("It's been 30 minutes, do you keep waiting? > (yes/no) ")

        if waiting == 'yes':
            print """
            Glad you're willing to wait. You'll be waiting for
            the next two hours
            """
            return 'hashtagsffail'
        elif waiting == 'no':
            print """
            So bored you finally check your phone and see
            your friends text, saying to join them at Hearth,
            where there is no wait and delicious everything.
            Caffeine headache reaching its peak you step out
            of the line and head to Hearth.
            """
            return 'hashtagsffail'


class Hearth(IconicStop):

    def once_there(self):
        print """
        You arrive at the warm and friendly door
        of Hearth, an amazing coffee shop that never
        has a long wait and only offers amazing pastries
        and sandwiches, made by one gifted woman.
        """
        return 'caffeine_success'


class CaffeineSuccess(IconicStop):
    def once_there(self):
        print "You smile. Today is the day you beat that only-in-SF moment."

        return 'caffeine_success'


# iconic_stops is a dictionary of stops and their corresponding class name
class Map(object):
    # iconic_stops is a dictionary of stops and their corresponding class name
    iconic_stops = {'ocean_beach': OceanBeach(),
                    'duboce_triangle': DuboceTriangle(),
                    'tartine': Tartine(),
                    'hearth': Hearth(),
                    'hashtagsffail': HashtagSFFAIL(),
                    'caffeine_success': CaffeineSuccess()
                    }

    # Where does starting_point get assigned from? is it the object you give map when you run an instance of Map?
    def __init__(self, starting_point):
        self.starting_point = starting_point
    # call the class Map with the attribute 'iconic_stops'
    # where and get the value of 'iconic_stops' with the key
    # iconic_stop_name

    def next_stop(self, iconic_stop_name):
        val = Map.iconic_stops.get(iconic_stop_name)
        return val

    def first_iconic_stop(self):
        return self.next_stop(self.starting_point)

# set directions to an instance of class Map
directions = Map('ocean_beach')
# IPhone is-a direcions, which is an instance of the class Map
game = IPhone(directions)  # is 'val' the object in IPhone (i.e. IPhone(val)?
# from game get the method called play
game.play()
