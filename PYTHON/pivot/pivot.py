# Rating: ~ 2.9 / 10
# Link: https://open.kattis.com/problems/pivot

def main():
  nums = int(input())
  values = [int(x) for x in input().split()]
  greaterthan = {values[0]}
  lessthan = {values[-1]}
  currmax = values[0]
  currmin = values[-1]
  for x in values:
    if x >= currmax:
      greaterthan.add(x)
      currmax = x
  for x in values[::-1]:
    if x <= currmin:
      lessthan.add(x)
      currmin = x
  both = greaterthan.intersection(lessthan)
  print(len(both))


if __name__ == "__main__":
  main()
