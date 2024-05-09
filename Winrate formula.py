class Player:
    def __init__(self, games, wins):
        self.games = games
        self.wins = wins

    def get_win_rate(self):
        win_rate = (self.wins / self.games) * 100
        return float(win_rate)

def main():
    games = float(input("Enter the number of games played: "))
    wins = float(input("Enter the number of wins: "))

    player = Player(games, wins)
    win_rate = player.get_win_rate()

    print(f"Your heroes' win rate is {win_rate}%")

if __name__ == "__main__":
    main()