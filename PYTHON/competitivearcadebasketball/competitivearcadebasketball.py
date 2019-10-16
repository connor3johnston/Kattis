from collections import deque
from sys import stdin, stdout

# Rating: ~ 3.0 / 10
# Link: https://open.kattis.com/problems/competitivearcadebasketball

def main():
  lines = deque(stdin.readlines())
  n, p, m = map(int, lines.popleft().split())
  players = {}
  winners = []
  seen = set()

  for x in range(n):
    players[lines.popleft().strip()] = 0

  for y in range(m):
    player, points = lines.popleft().split()
    points = int(points)
    players[player] += points

    if players[player] >= p and player not in seen:
      winners.append(player)
      seen.add(player)

  if len(winners) == 0:
    stdout.write('No winner!\n')
  else:
    for winner in winners:
      stdout.write('%s wins!\n' % winner)


if __name__ == '__main__':
  main()
