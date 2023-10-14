class Game():
    def __init__(self, title):
        self.title = title

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if isinstance(value, str):
            self._title = value

    def results(self):
        return (Result())
        
    def players(self):
        pass

    def average_score(self, player):
        pass

class Player:
    # all = []

    def __init__(self, username):
        self.username = username
        # Player.all.append(self)

    def results(self):
        pass

    def games_played(self):
        pass

    def played_game(self, game):
        pass

    def num_times_played(self, game):
        pass

class Result:
    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)
