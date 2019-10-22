# Rating: ~ 2.1 / 10
# Link: https://open.kattis.com/problems/armystrengtheasy

def main():
  cases = int(input())
  for x in range(cases):
    input()

    G, M = map(int, input().split())
    GArmy = [int(y) for y in input().split()]
    MArmy = [int(y) for y in input().split()]

    GArmy = sorted(GArmy, reverse=True)
    MArmy = sorted(MArmy, reverse=True)

    while GArmy and MArmy:
      if MArmy[-1] > GArmy[-1]:
        GArmy.pop()
      else:
        MArmy.pop()

    if GArmy:
      print('Godzilla')
    else:
      print('MechaGodzilla')


if __name__ == "__main__":
  main()
