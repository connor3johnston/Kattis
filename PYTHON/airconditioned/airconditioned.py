# Rating: ~ 4.1 / 10
# Link: https://open.kattis.com/problems/airconditioned

def main():
  cases = int(input())
  minions = list()
  rooms = set()
  for x in range(cases):
    low, high = map(int, input().split())
    minions.append((high, low))
  minions.sort()
  for minion in minions:
    found = False
    for temp in range(minion[1], minion[0]+1):
      if temp in rooms:
        found = True
        break
    if not found:
      rooms.add(minion[0])
  print(len(rooms))


if __name__ == "__main__":
  main()
