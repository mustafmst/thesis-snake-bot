import random


class Specimen:
    """
    Todo:
    implement creating model based on configurations
    """
    def __init__(self, config):
        self.__score = None
        self.__config = config
        pass

    """
    Todo:
    implement real playing using snake
    """
    def __play_game(self):
        self.__score = random.randint(0, 100000)
        pass

    """
    Todo:
    implement real crossing
    """
    def cross_with(self, other):
        return Specimen(other.__config)

    """
    Todo
    """
    def mutate(self):
        self.__score = None
        pass

    def get_score(self):
        if self.__score is None:
            self.__play_game()
        return self.__score
