# Rating: ~ 3.3 / 10
# Link: https://open.kattis.com/problems/coast

from sys import stdin, stdout

def bfs(levels, r, c, visited):
  queue = [(0, 0)]
  visited[0][0] = True

  count = 0

  while queue:
    curr = queue.pop()
    row = curr[0]
    col = curr[1]

    if row - 1 > -1 and not visited[row - 1][col]:
      if levels[row - 1][col] == 1:
        count += 1
      else:
        queue.insert(0, (row - 1, col))
        visited[row - 1][col] = True
    if row + 1 < r + 2 and not visited[row + 1][col]:
      if levels[row + 1][col] == 1:
        count += 1
      else:
        queue.insert(0, (row + 1, col))
        visited[row + 1][col] = True
    if col - 1 > -1 and not visited[row][col - 1]:
      if levels[row][col - 1] == 1:
        count += 1
      else:
        queue.insert(0, (row, col - 1))
        visited[row][col - 1] = True
    if col + 1< c + 2 and not visited[row][col + 1]:
      if levels[row][col + 1] == 1:
        count += 1
      else:
        queue.insert(0, (row, col + 1))
        visited[row][col + 1] = True
  return count


def main():
  r, c = map(int, stdin.readline().split())
  levels = list()
  visited = list()

  levels.append([0] * (c + 2))
  visited.append([False] * (c + 2))
  for x in range(r):
    add = [0]
    add.extend([int(y) for y in list(stdin.readline().strip())])
    add.append(0)

    levels.append(add)
    visited.append([False] * (c + 2))
  visited.append([False] * (c + 2))
  levels.append([0] * (c + 2))

  print(bfs(levels, r, c, visited))


if __name__ == "__main__":
  main()
