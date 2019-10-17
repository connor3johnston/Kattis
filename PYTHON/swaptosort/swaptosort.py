from sys import stdin

# Rating: ~ 4.2 / 10
# Link: https://open.kattis.com/problems/swaptosort

def union(parents, x, y):
  parents[find(parents, x)] = find(parents, y)


def find(parents, child):
  if parents[child] != child:
    parents[child] = find(parents, parents[child])
  return parents[child]


def main():
  N, K = map(int, stdin.readline().split())
  parents = list(range(N + 1))

  for x in range(K):
    x, y = map(int, stdin.readline().split())
    union(parents, x, y)

  possible = True
  for x in range(1, N + 1):
    if find(parents, N - x + 1) != find(parents, x):
      possible = False
      break

  if possible:
    print('Yes')
  else:
    print('No')


if __name__ == "__main__":
  main()
