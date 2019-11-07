from sys import stdin, stdout
from collections import deque

# Rating: ~ 3.0 / 10
# Link: https://open.kattis.com/problems/bank

def main():
  N, T = map(int, stdin.readline().split())
  line = []
  serve = [0] * T

  for x in range(N):
    money, time = map(int, stdin.readline().split())
    line.append((money, time))

  line = sorted(line, key=lambda y: (-y[0], y[1]))

  for cash, by in line:
    while by > -1:
      if serve[by] == 0:
        serve[by] = cash
        break
      by -= 1

  stdout.write('%s\n' % sum(serve))


if __name__ == "__main__":
  main()
