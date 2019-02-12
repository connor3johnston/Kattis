# Rating: ~ 1.6 / 10
# Link: https://open.kattis.com/problems/inflation

def main():
  num = int(input())
  balloons = list(range(1,num+1))
  cans = [int(x) for x in input().split()]
  cans = sorted(cans)
  check = True
  percents = set()
  for index, balloon in enumerate(balloons):
    if cans[index] > balloon:
      check = False
      break
    if cans[index] <= balloon:
      percents.add(cans[index]/balloon)
  if check:
    print(min(percents))
  else:
    print('impossible')


if __name__ == "__main__":
  main()
