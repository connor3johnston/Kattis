from collections import deque

# Rating: ~ 2.9 / 10
# Link: https://open.kattis.com/problems/elevatortrouble

def main():
  f, s, g, u, d = map(int, input().split())
  out = bfs(f, s, g, u, d)
  print(out)


def bfs(f, s, g, u, d):
  q = deque([(s, 0)])
  seen = {s}

  while q:
    curr = q.popleft()

    if curr[0] == g:
      return curr[1]

    up = curr[0] + u
    down = curr[0] - d

    if up <= f and up not in seen:
      q.append((up, curr[1] + 1))
      seen.add(up)
    if down > 0 and down not in seen:
      q.append((down, curr[1] + 1))
      seen.add(down)

  return 'use the stairs'


if __name__ == "__main__":
  main()
