class Game:
    all =[]   

    def __init__(self, title):
        self.title = title
        Game.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if not (hasattr(self, 'title')):
            if (isinstance(value, str) and len(value) > 0):
                self._title = value

    def results(self):
        return [result for result in Result.all if result.game == self]
        
    def players(self):
        my_list = [player for player in Result.all if player.game == self]
        return set(my_list)

    def average_score(self, player):
        pass


class Player:
    all = []

    def __init__(self, username):
        self.username = username
        Player.all.append(self)

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if (isinstance(username, str) and 1 < len(username) < 17):
            self._username = username

    def results(self):
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        my_list = [game for game in Game.all if game.player == self]
        return set(my_list)
    # not sure if this is right ^^^^^^^^^^^^

    def played_game(self, game):
        if self in game:
            return True
        else:
            return False

    def num_times_played(self, game):
        pass



class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if not (hasattr(self, 'score')):
            if (isinstance(score, int) and 0 < score < 5001):
                self._score = score
       
    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, player):
        if (isinstance(player, Player)):
            self._player =  player

    @property
    def game(self):
        return self._game

    @game.setter
    def game(self, game):
        if (isinstance(game, Game)):
            self._game =  game