from sys import exit
from random import randint


class Scene(object):
    def enter(self):
        print "it's no use"
        exit(1)


class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            print "------"
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)


class choosebike(Scene):
    model = {
        'bike1': 'you got a merida bike',
        'bike2': 'you got a giant bike',
        'bike3': 'congratuations,you got a specialized bike!'
    }

    def enter(self):
        print """there have three bike
                they are bike1, bike2, bike3.
                if you can choose your bike,
                which will you choose ?
            """
        bike = raw_input(">")

        if bike == 'bike1' or bike == 'bike2' or bike == 'bike3':
            print choosebike.model[bike]
            print "now, to complete your race with your bike!"
            print "Good luck!"

            return 'lock'
        else:
            print"oh no"
            print "please input agian"
            return 'choosebike'


class lock(Scene):
    def enter(self):
        print "oh my god! the bike have locked"
        print "ah! it have a note"
        print "it say 'you should guess the number correctly and you can go'"
        print "and you should take notice to your time "
        print "you just have 20 times"
        print "please input the number which is a double-digit you guess!"
        # Debug
        number = "12"
        #        number = "%d%d" % (randint(0, 9), randint(0, 9))
        guess = raw_input("-->")
        guesses = 0

        # return 'speedorno'
        while guess != number and guesses < 20:
            guesses += 1
            print "input again"
            guess = raw_input("-->")

        if guess == number:
            print "ahhh you are so samartly"
            print "now ,continue your race"

            return 'speedorno'

        else:
            print "\a\a\a\a"
            print "so sorry, your times is uesd out"
            print "you have no time to compelete the race"
            exit(1)


class speedorno(Scene):
    results = [
        'you are so cool, you got the no.1!! congratuations!!',
        'oh it\'s a nice race , you got the no.2, congratuations',
        'i belive you will be the no.1 next time! ',
        'e...it\'s really a little pity, you are the no.4, but you are very good,you will better next time!']

    def enter(self):
        print "you will compelete race immediately,"
        print "and now you want speed, but"
        print "if you speed,your leg may hurted and can't go on"
        print "if you not speed, you not speed ,you may win"
        print "but it's probability is smaller then speed"
        print "will you speed?"
        spdorno = raw_input(">")

        print "you choose %r " % spdorno

        print speedorno.results[randint(0, 3)]
        return 'finished'


class finished(object):11235777747444444
    def enter(self):
        exit(0)


class Map(object):
    scenes = {
        'choosebike': choosebike(),
        'lock': lock(),
        'speedorno': speedorno(),
        'finished': finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):  # the function of next_scene
        return Map.scenes.get(scene_name)  # system function .get -dictionary

    def opening_scene(self):  # the function of opening_scene  and use function next scene
        return self.next_scene(self.start_scene)

start = Map('choosebike')
game = Engine(start)
game.play()
