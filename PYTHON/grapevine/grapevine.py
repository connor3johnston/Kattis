from sys import stdin
from collections import deque

# Rating: ~ 3.5 / 10
# Link: https://open.kattis.com/problems/grapevine

def main():
  lines = deque(stdin.readlines())

  n, m, d = map(int, lines.popleft().strip().split())
  skeptical = {}
  ships = {}
  for x in range(n):
    line = lines.popleft().strip().split()
    name = line[0]
    needed = int(line[1])
    skeptical[name] = needed
    ships[name] = set()
  for y in range(m):
    pair = lines.popleft().strip().split()
    ships[pair[0]].add(pair[1])
    ships[pair[1]].add(pair[0])
  origin = lines.popleft().strip()
  sources = deque([origin])
  seen = {origin}
  for z in range(d):
    temp = deque()
    while sources:
      cur = sources.pop()
      for person in ships[cur]:
        if person not in seen:
          seen.add(person)
        skeptical[person] -= 1
        if skeptical[person] == 0:
          temp.append(person)
    sources = temp
  print(len(seen) - 1)


if __name__ == "__main__":
  main()
