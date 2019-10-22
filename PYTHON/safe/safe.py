from collections import deque

# Rating: ~ 3.3 / 10
# Link: https://open.kattis.com/problems/safe

def bfs(pad):
  starts = []

  for x in range(3):
    for y in range(3):
      starts.append((pad, x, y, 0))

  q = deque(starts)
  seen = set()
  seen.add(pad)

  while q:
    curr, r, c, m = q.popleft()

    if curr == ((0, 0, 0), (0, 0, 0), (0, 0, 0)):
      return m

    alt = alter(curr, r, c)

    if alt in seen:
      continue

    seen.add(alt)

    for i in range(3):
      for j in range(3):
        q.append((alt, i, j, m + 1))

  return -1


def alter(curr, r, c):
  alt = [list(a) for a in curr]
  alt[r][c] += 1
  if alt[r][c] > 3:
    alt[r][c] = 0

  for x in range(3):
    if x == r:
      continue
    alt[x][c] += 1

    if alt[x][c] > 3:
      alt[x][c] = 0

  for y in range(3):
    if c == y:
      continue
    alt[r][y] += 1

    if alt[r][y] > 3:
      alt[r][y] = 0

  return tuple(tuple(b) for b in alt)


def main():
  pad = []
  for x in range(3):
    pad.append(tuple(int(y) for y in input().split()))

  print(bfs(tuple(pad)))


if __name__ == "__main__":
  main()
