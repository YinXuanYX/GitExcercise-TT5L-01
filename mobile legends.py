class Player:
<<<<<<< HEAD
    def __init__(user, games, wins):
        self.games = games
        self.wins = wins

    def get_win_rate(player):
        win_rate = (user.wins / user.games) * 100
=======
    def __init__(self, games, wins):
        self.games = games
        self.wins = wins

    def get_win_rate(self):
        win_rate = (self.wins / self.games) * 100
>>>>>>> 08a96e60b786ef5e3b65a987a305e3c610a6153c
        return int(win_rate)

def main():
    games = int(input("Enter the number of games played: "))
    wins = int(input("Enter the number of wins: "))

    player = Player(games, wins)
    win_rate = player.get_win_rate()

    print(f"Your win rate is {win_rate}%")

if __name__ == "__main__":
    main()