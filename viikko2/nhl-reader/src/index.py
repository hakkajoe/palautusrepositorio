import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.response = requests.get(url).json()

    def get_players(self):
        players = []

        for player_dict in self.response:
            player = Player(player_dict)
            players.append(player)

        sorted_players = sorted(players, key=lambda player: player.goals + player.assists, reverse=True)
        return sorted_players


class PlayerStats:
    def __init__(self, players):
        self.players = players.get_players()

    def top_scorers_by_nationality(self, nat):
        print(f"Players from {nat}:\n")

        filtered_list = []
        for player in self.players:
            if player.nationality == nat:
                filtered_list.append(player)

        return filtered_list


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    for player in players:
        print(player)

if __name__ == "__main__":
    main()
