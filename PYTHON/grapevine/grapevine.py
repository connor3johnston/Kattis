import sys
from collections import deque

# Rating: ~ 3.5 / 10
# Link: https://open.kattis.com/problems/grapevine

def main():
  lines = deque(sys.stdin.readlines())
  n, m, d = map(int, lines.popleft().strip().split())
  skeptical = {}
  ships = {}
  for x in range(n):
    line = lines.popleft().strip().split()
    skeptical[line[0]] = int(line[1])
    ships[line[0]] = []
  for y in range(m):
    pair = lines.popleft().strip().split()
    ships[pair[0]].append(pair[1])
    ships[pair[1]].append(pair[0])
  origin = lines.popleft().strip()
  sources = deque([origin])
  seen = {origin}
  for z in range(d):
    temp = []
    while sources:
      cur = sources.popleft()
      for person in ships[cur]:
        if person not in seen:
          seen.add(person)
        skeptical[person] -= 1
        if skeptical[person] == 0:
          temp.append(person)
    sources = deque(temp)
  print(len(seen) - 1)


if __name__ == "__main__":
  main()
