# Rating: ~ 3.0 / 10
# Link: https://open.kattis.com/problems/goodmorning

def bfs(possible: list, stack: list, moves: dict):
  while stack:
    here = stack.pop(0)
    add = moves[int(here[-1])]
    for y in add:
      if len(here + str(y)) > 3:
        return
      possible.append(here+str(y))
      stack.append(here+str(y))


def main():
  moves = {0: [0],
           1: [0,1,2,3,4,5,6,7,8,9],
           2: [0,2,3,5,6,8,9],
           3: [3,6,9],
           4: [0,4,5,6,7,8,9],
           5: [0,5,6,8,9],
           6: [6,9],
           7: [0,7,8,9],
           8: [0,8,9],
           9: [9]}
  cases = int(input())
  for x in range(cases):
    num = int(input())
    possible = list()
    for y in range(1, 10):
      stack = list()
      stack.append(str(y))
      possible.append(str(y))
      bfs(possible, stack, moves)
    track = list()
    for s in possible:
      cur = abs(num-int(s))
      track.append(cur)
    print(possible[track.index(min(track))])


if __name__ == "__main__":
  main()
