from sys import stdin, stdout

# Rating: ~ 3.1 / 10
# Link: https://open.kattis.com/problems/moneymatters

def main():
  friends, rem_ships = map(int, stdin.readline().split())
  owes = []
  ships = [z for z in range(friends)]
  for i in range(friends):
    owes.append(int(stdin.readline()))

  for j in range(rem_ships):
    x, y = map(int, stdin.readline().split())
    union(x, y, ships)

  net = {}
  for k in range(friends):
    key = find(k, ships)
    if key not in net:
      net[key] = 0
    net[key] += owes[k]

  for val in net.values():
    if val != 0:
      stdout.write('IMPOSSIBLE\n')
      return
  stdout.write('POSSIBLE\n')


def union(x, y, ships):
  ships[find(x, ships)] = find(y, ships)


def find(val, ships):
  if ships[val] != val:
    ships[val] = find(ships[val], ships)
  return ships[val]


if __name__ == "__main__":
  main()
