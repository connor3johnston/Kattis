# Rating: ~ 5.2 / 10
# Link: https://open.kattis.com/problems/virtualfriends

def union(ships, root2, root1):
  ships[root2] = root1


def find(ships, person):
  if ships[person] == person:
    return person
  ships[person] = find(ships, ships[person])
  return ships[person]


def main():
  cases = int(input())
  for x in range(cases):
    ships = dict()
    sizes = dict()
    F = int(input())
    for y in range(F):
      ship = input().split()
      if ship[0] not in ships:
        ships[ship[0]] = ship[0]
      if ship[1] not in ships:
        ships[ship[1]] = ship[1]
      root1 = find(ships, ship[0])
      root2 = find(ships, ship[1])

      if root1 == root2:
        print(sizes[root2])
        continue

      union(ships, root2, root1)

      if root1 not in sizes:
        sizes[root1] = 1
      if root2 not in sizes:
        sizes[root2] = 1

      sizes[root1] += sizes[root2]
      del sizes[root2]

      print(sizes[root1])


if __name__ == "__main__":
  main()
