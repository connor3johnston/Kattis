# Rating: ~ 4.3 / 10
# Link: https://open.kattis.com/problems/airconditioned

def main():
  minions = int(input())
  range_ = [int(x) for x in input().split()]
  rooms = [range_]
  for y in range(1, minions):
    range_ = [int(x) for x in input().split()]
    found = False
    for temps in rooms:
      if range_[0] >= temps[0] and range_[0] <= temps[1]:
        if range_[1] < temps[1]:
          temps[1] = range_[1]
        if range_[0] > temps[0]:
          temps[0] = range_[0]
        found = True
        break
      elif range_[1] >= temps[0] and range_[1] <= temps[1]:
        if range_[1] < temps[1]:
          temps[1] = range_[1]
        if range_[0] > temps[0]:
          temps[0] = range_[0]
        found = True
        break
    if not found:
      rooms.append(range_)
  print(len(rooms))


if __name__ == "__main__":
  main()
