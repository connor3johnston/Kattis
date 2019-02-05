# Rating: ~ 3.4 / 10
# Link: https://open.kattis.com/problems/dominoes2

def main():
  cases = int(input())
  for x in range(cases):
    line = [int(x) for x in input().split()]
    dominoes = line[0]
    falls = {}
    fallen = set()
    by_hand = []
    for y in range(line[1]):
      temp = [int(x) for x in input().split()]
      if temp[0] in falls:
        falls[temp[0]].append(temp[1])
      else:
        falls[temp[0]] = [temp[1]]
    for z in range(line[2]):
      by_hand.append(int(input()))
    cur = 0
    while cur < len(by_hand):
      here = by_hand[cur]
      cur += 1
      if here in fallen:
        continue
      fallen.add(here)
      if here in falls:
        for p in falls[here]:
          by_hand.append(p)
    print(len(fallen))


if __name__ == "__main__":
  main()
