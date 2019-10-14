# Rating: ~ 4.6 / 10
# Link: https://open.kattis.com/problems/touchdown

def get(plays):
  yard = 20
  first = 0
  down = 1

  for play in plays:
    yard += play
    first += play

    if yard <= 0:
      return 'Safety'
    elif yard >= 100:
      return 'Touchdown'
    elif first >= 10:
      down = 1
      first = 0
    else:
      down += 1
      if down == 5:
        return 'Nothing'
  return 'Nothing'


def main():
  num = int(input())
  plays = [int(x) for x in input().split()]
  print(get(plays))


if __name__ == '__main__':
  main()
