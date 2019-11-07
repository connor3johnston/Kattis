from sys import stdin, stdout
from math import inf
from collections import deque

# Rating: ~ 3.3 / 10
# Link: https://open.kattis.com/problems/slikar

dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))

def main():
  R, C = map(int, stdin.readline().split())
  board = []
  for x in range(R):
    board.append(stdin.readline().strip())

  start = (-1, -1)
  floodQ = deque()
  painterQ = deque()
  floodTimes = [[inf for a in range(C)] for b in range(R)]
  painterTimes = [[inf for a in range(C)] for b in range(R)]

  for r in range(R):
    for c in range(C):
      if board[r][c] == '*':
        floodQ.append((r, c, 0))
        floodTimes[r][c] = 0
      elif board[r][c] == 'S':
        start = (r, c)

  while floodQ:
    currR, currC, currT = floodQ.popleft()
    for x, y in dirs:
      if currR + x < R and currR + x > -1 and currC + y < C and currC + y > -1:
        nextR = currR + x
        nextC = currC + y

        if floodTimes[nextR][nextC] == inf and board[nextR][nextC] == '.':
          floodTimes[nextR][nextC] = currT + 1
          floodQ.append((nextR, nextC, currT + 1))

  result = inf
  painterQ.append((start[0], start[1], 0))
  painterTimes[start[0]][start[1]] = 0

  while painterQ:
    currR, currC, currT = painterQ.popleft()

    if board[currR][currC] == 'D':
      result = currT
      break

    for x, y in dirs:
      if currR + x < R and currR + x > -1 and currC + y < C and currC + y > -1:
        nextR = currR + x
        nextC = currC + y

        if painterTimes[nextR][nextC] == inf and (board[nextR][nextC] == '.' or board[nextR][nextC] == 'D') and currT + 1 < floodTimes[nextR][nextC]:
          painterTimes[nextR][nextC] = currT + 1
          painterQ.append((nextR, nextC, currT + 1))

  if result == inf:
    stdout.write('KAKTUS\n')
  else:
    stdout.write('%s' % result)


if __name__ == "__main__":
  main()
