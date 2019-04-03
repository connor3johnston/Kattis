# Rating: ~ 5.3 / 10
# Link: https://open.kattis.com/problems/grapevine

def main():
  n, m, d = map(int, input().split())
  skeptical = dict()
  ships = dict()
  index = 0
  for x in range(n):
    line = input().split()
    name = line[0]
    needed = int(line[1])
    skeptical[name] = needed
    ships[name] = set()
  for y in range(m):
    pair = input().split()
    ships[pair[0]].add(pair[1])
    ships[pair[1]].add(pair[0])
  origin = input()
  count = 0
  sources = [origin]
  seen = {origin}
  for z in range(d):
    temp = list()
    while sources:
      cur = sources.pop()
      for person in ships[cur]:
        if person not in seen:
          count += 1
          seen.add(person)
        skeptical[person] -= 1
        if skeptical[person] == 0:
          temp.append(person)
    sources = temp
  print(count)


if __name__ == "__main__":
  main()
