from collections import deque
from sys import stdin, stdout

# Rating: ~ 3.2 / 10
# Link: https://open.kattis.com/problems/knightsfen

# White = 0, Black = 1

DIRS = ((-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2))
END = (1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 2, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0)

def get_moves():
  moves = {}
  moves[END] = 0

  q = deque([])
  q.append((END, 12, 0))

  while q:
    board, gap, dist = q.popleft()

    if dist >= 10:
      break

    neighbors = get_neighbors(gap)
    for neighbor in neighbors:
      new_board = list(board)
      new_board[gap] = board[neighbor]
      new_board[neighbor] = 2

      new_board = tuple(new_board)
      if new_board not in moves:
        moves[new_board] = dist + 1
        q.append((new_board, neighbor, dist + 1))

  return moves


def get_neighbors(gap):
  row = gap//5
  col = gap%5
  neighbors = []

  for DIR in DIRS:
    new_row = row + DIR[0]
    new_col = col + DIR[1]

    if new_row > -1 and new_row < 5 and new_col > -1 and new_col < 5:
      neighbors.append(5 * new_row + new_col)

  return neighbors


def main():
  moves = get_moves()
  sets = int(stdin.readline())

  for i in range(sets):
    curr_board = []
    for r in range(5):
      line = stdin.readline()
      for c in range(5):
        if line[c] == ' ':
          curr_board.append(2)
        else:
          curr_board.append(int(line[c]))

    curr_board = tuple(curr_board)
    if curr_board in moves:
      stdout.write(f'Solvable in {moves[curr_board]} move(s).\n')
    else:
      stdout.write('Unsolvable in less than 11 move(s).\n')


if __name__ == "__main__":
  main()
