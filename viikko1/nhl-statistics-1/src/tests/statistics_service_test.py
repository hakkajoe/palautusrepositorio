import unittest
from statistics_service import StatisticsService, SortBy
from player import Player
from player_reader import PlayerReader

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_existing_player(self):
        player = self.stats.search("Gretzky")
        self.assertEqual(player.name, "Gretzky")

    def test_search_non_existing_player(self):
        player = self.stats.search("NonExistentPlayer")
        self.assertIsNone(player)

    def test_team(self):
        team_players = self.stats.team("EDM")
        self.assertEqual(len(team_players), 3)
        self.assertTrue(all(player.team == "EDM" for player in team_players))

    def test_top(self):
        top_scorers = self.stats.top(3)
        self.assertEqual(len(top_scorers), 3)
        self.assertTrue(top_scorers[0].points >= top_scorers[1].points >= top_scorers[2].points)

    def test_top_points(self):
        top_scorers = self.stats.top(3, SortBy.POINTS)
        self.assertEqual(len(top_scorers), 3)
        self.assertTrue(top_scorers[0].points >= top_scorers[1].points >= top_scorers[2].points)

    def test_top_goals(self):
        top_goals = self.stats.top(3, SortBy.GOALS)
        self.assertEqual(len(top_goals), 3)
        print(top_goals[0])
        print(top_goals[1])
        print(top_goals[2])

        self.assertTrue(top_goals[0].goals >= top_goals[1].goals >= top_goals[2].goals)

    def test_top_assists(self):
        top_assists = self.stats.top(3, SortBy.ASSISTS)
        self.assertEqual(len(top_assists), 3)
        self.assertTrue(top_assists[0].assists >= top_assists[1].assists >= top_assists[2].assists)