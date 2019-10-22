from sys import stdin, stdout
# Rating: ~ 4.1 / 10
# Link: https://open.kattis.com/problems/wheresmyinternet

def union(parents, x, y):
  parX = find(parents, x)
  parY = find(parents, y)

  parents[parY] = parX


def find(parents, child):
  if parents[child] != child:
    parents[child] = find(parents, parents[child])

  return parents[child]


def main():
  N, M = map(int, stdin.readline().split())
  parents = list(range(N + 1))

  for x in range(M):
    x, y = map(int, stdin.readline().split())

    union(parents, x, y)

  check = find(parents, 1)
  allConnected = True

  for y in range(1, N + 1):
    curr = find(parents, y)
    if curr != check:
      allConnected = False
      stdout.write('%s\n' % y)

  if allConnected:
    stdout.write('Connected\n')


if __name__ == "__main__":
  main()
