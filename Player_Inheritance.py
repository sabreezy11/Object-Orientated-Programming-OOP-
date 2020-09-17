#This class will represent the people playing the game

class Player(object): # Method

    def __init__(self, name):
        self.name = name
        self._lives = 3  # start with 3 lives
        self._level = 1  # start on level 1
        self._score = 0  # start with a score of 0

    def _get_lives(self):  # getter property (get the lives value)
        return self._lives

    def _set_lives(self, lives):  # setter property (set the lives value)
        if lives >= 0:
            self._lives = lives
        else:
            print("Lives cannot be negative")
            self._lives = 0

    def _get_level(self): # property
        return self._level

    def _set_level(self, level): # property
        #  Has to check that level > 0, then calculate the bonus that will be added to the score
        if level > 0:
            delta = level - self._level
            self._score += delta * 1000
            self._level = level
        else:
            print("Level can't be less than 1")


    lives = property(_get_lives, _set_lives)  # ctrl + click to see 'property' description
    level = property(_get_level, _set_level)

    """A decorator takes in a function, adds some functionality and returns it."""
    @property  # decorator takes care of the score = property line
    def score(self):
        return self._score

    @score.setter
    def score(self,score):
        self._score = score # if ou type .score instead of ._score, you can get a recursive problem

    def __str__(self):
        return "Name: {0.name}\nLives: {0.lives}\nScore: {0.score}\nLevel: {0.level}".format(self)

  