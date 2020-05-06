from sys import stdin, stdout

# Rating: ~ 3.2 / 10
# Link: https://open.kattis.com/problems/queens

def main():
  positions = stdin.readlines()[1:]
  cols = set()
  rows = set()
  ldiags = set()
  rdiags = set()

  for position in positions:
    c, r = map(int, position.split())
    ldiag = c + r
    rdiag = 7 + c - r

    if c in cols or r in rows or ldiag in ldiags or rdiag in rdiags:
      stdout.write('INCORRECT\n')
      return
    else:
      cols.add(c)
      rows.add(r)
      ldiags.add(ldiag)
      rdiags.add(rdiag)

  stdout.write('CORRECT\n')


if __name__ == "__main__":
  main()
