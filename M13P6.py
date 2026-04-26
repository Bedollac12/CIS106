def display_players(player_dict):
  print(f"{'Player':<15}{'Average':>10}")
  print("-" * 25)
  for name in player_dict:
    avg = player_dict[name]
    print(f"{name:<15}{avg:>10.3f}")

f = open("players.txt", "r")
players = {}

line = f.readline().rstrip('\n')

while line !="":
  avg = float(f.readline())
  players[line] = avg
  line = f.readline().rstrip('\n')

f.close()

display_players(players)