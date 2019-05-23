class Specimen:
    def __init__(self):
        self.__score = None
        pass

    def __play_game(self):
        pass

    def get_score(self):
        if self.__score in None:
            self.__play_game()
        return self.__score
