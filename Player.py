class Player:

    def __init__(self, name, round_score=0, total_score=0):
        self._name = name
        self._round_score = round_score
        self._total_score = total_score

    @property
    def name(self):
        return self._name

    @property
    def total_score(self):
        return self._total_score

    @property
    def round_score(self):
        return self._round_score

    def add_total_score(self, val):
        self._total_score += val

    def add_round_score(self, val):
        self._round_score += val

    # Reset the value of specified score to 0
    # Valid parameters for which are:
    # "ROUND", "TOTAL", "BOTH"
    def reset_score(self, which="ROUND", ):
        if which is "ROUND":
            self._round_score = 0
        elif which is "TOTAL":
            self._total_score = 0
        else:
            self._round_score = 0
            self._total_score = 0
