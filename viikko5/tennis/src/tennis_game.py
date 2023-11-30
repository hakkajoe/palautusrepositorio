class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_score(self):
        if self.player1_score == self.player2_score:
            return self.equal_scores()
        elif self.player1_score >= 4 or self.player2_score >= 4:
            return self.advantage_or_win()
        else:
            return self.non_equal_scores()

    def equal_scores(self):
        if self.player1_score <= 2:
            return self.score_mapping[self.player1_score] + "-All"
        else:
            return "Deuce"

    def advantage_or_win(self):
        minus_result = self.player1_score - self.player2_score
        if abs(minus_result) == 1:
            return f"Advantage {self.leading_player()}"
        else:
            return f"Win for {self.leading_player()}"

    def leading_player(self):
        return "player1" if self.player1_score > self.player2_score else "player2"

    def non_equal_scores(self):
        return f"{self.score_mapping[self.player1_score]}-{self.score_mapping[self.player2_score]}"

    score_mapping = {
        0: "Love",
        1: "Fifteen",
        2: "Thirty",
        3: "Forty"
    }