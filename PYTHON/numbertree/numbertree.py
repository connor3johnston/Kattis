# Rating: ~ 2.1 / 10
# Link: https://open.kattis.com/problems/numbertree

def main():
  line = input().split()
  P = ''

  if len(line) > 1:
    P = line[1]

  H = int(line[0])

  top = (2**(H + 1)) - 1
  tree = list()

  point = 0
  for move in P:
    if move == 'L':
      point = (2 * point) + 1
    else:
      point = (2 * point) + 2

  print(top - point)


if __name__ == "__main__":
  main()
