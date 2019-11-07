from collections import deque
from sys import stdin, stdout

# Rating: ~ 3.4 / 10
# Link: https://open.kattis.com/problems/delivery

def cost(routes, cap):
  cost = 0

  while routes:
    loc, need = routes.popleft()

    while need > 0:
      cost += 2 * loc
      need -= cap

    # Back
    leftover = abs(need)
    while leftover > 0 and routes:
      loc, need = routes.popleft()

      if leftover > need:
        leftover -= need
        need = 0
      else:
        need -= leftover
        leftover = 0

      if need != 0:
        routes.appendleft((loc, need))

  return cost


def main():
  num, cap = map(int, stdin.readline().split())
  neg = deque()
  pos = deque()

  for x in range(num):
    loc, to = map(int, stdin.readline().split())

    if loc < 0:
      neg.append((loc * -1, to))
    else:
      pos.append((loc, to))

  pos = deque(sorted(pos, reverse=True))

  cost1 = cost(pos, cap)
  cost2 = cost(neg, cap)

  stdout.write('%s\n' % (cost1 + cost2))


if __name__ == "__main__":
  main()
