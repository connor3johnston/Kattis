# Rating: ~ 3.2 / 10
# Link: https://open.kattis.com/problems/dvds

def main():
  cases = int(input())
  for x in range(cases):
    num = int(input())
    dvds = [int(i) for i in input().split()]
    find = 1
    moves = 0
    for dvd in dvds:
      if dvd != find:
        moves += 1
      else:
        find += 1
    print(moves)


if __name__ == "__main__":
  main()
