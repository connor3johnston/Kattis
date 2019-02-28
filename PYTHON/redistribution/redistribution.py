# Rating: ~ 2.2 / 10
# Link: https://open.kattis.com/problems/redistribution

def main():
  num = int(input())
  rooms = [int(x) for x in input().split()]
  max_ = max(rooms)
  index = rooms.index(max_)
  if max_ <= (sum(rooms[0:index]) + sum(rooms[index+1::])):
    out = str(index+1) + ' '
    rooms[index] = -1
    max_ = max(rooms)
    index = rooms.index(max_)
    while max_ != -1:
      out += str(index+1) + ' '
      rooms[index] = -1
      max_ = max(rooms)
      index = rooms.index(max_)
    print(out)
  else:
    print('impossible')


if __name__ == "__main__":
  main()
