from sys import stdin, stdout
# Rating: ~ 4.5 / 10
# Link: https://open.kattis.com/problems/virtualfriends

def union(parent, x, y):
  parent[find(parent, y)] = find(parent, x)


def find(parent, child):
  if parent[child] != child:
    parent[child] = find(parent, parent[child])

  return parent[child]


def main():
  cases = int(stdin.readline().strip())
  out = []

  for x in range(cases):
    ships = dict()
    sizes = dict()
    num = int(stdin.readline().strip())

    for y in range(num):
      x, y = sorted(stdin.readline().split())
      if x not in ships:
        ships[x] = x
        sizes[x] = 1
      if y not in ships:
        ships[y] = y
        sizes[y] = 1

      root1 = find(ships, x)
      root2 = find(ships, y)

      if root1 == root2:
        out.append(str(sizes[root2]))
        continue

      both = sizes[root1] + sizes[root2]
      out.append(str(both))
      union(ships, x, y)
      sizes[root1] = both
      sizes[root2] = both

  stdout.write('\n'.join(out))


if __name__ == "__main__":
  main()
