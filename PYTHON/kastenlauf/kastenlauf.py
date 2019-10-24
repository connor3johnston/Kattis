from sys import stdin, stdout
from collections import deque

# Rating: ~ 4.0 / 10
# Link: https://open.kattis.com/problems/kastenlauf

def dfs(start, end, stores):
  stack = [start]
  visited = set()

  while stack:
    x, y = stack.pop()

    if abs(x - end[0]) + abs(y - end[1]) <= 1000:
      return 'happy'

    for store in stores:
      if store not in visited and abs(x - store[0]) + abs(y - store[1]) <= 1000:
        stack.append(store)
        visited.add(store)

  return 'sad'


def main():
  cases = int(stdin.readline().strip())

  for x in range(cases):
    start = None
    stores = set()
    end = None
    numS = int(stdin.readline().strip())

    start = tuple(int(a) for a in stdin.readline().split())
    for y in range(numS):
      x, y = map(int, stdin.readline().split())
      stores.add((x, y))
    end = tuple(int(a) for a in stdin.readline().split())

    print(dfs(start, end, stores))


if __name__ == "__main__":
  main()
