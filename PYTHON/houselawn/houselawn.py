from sys import stdin, stdout

# Rating: ~ 3.4 / 10
# Link: https://open.kattis.com/problems/houselawn

def main():
  lines = stdin.readlines()
  l, m = map(int, lines[0].split())

  valid = {}
  for i in range(1, m + 1):
    line = lines[i].strip().split(',')
    n = line[0]
    p, c, t, r = map(int, line[1:])

    total_cut = (10080 * c * t)//(t + r)

    if total_cut >= l:
      if p not in valid:
        valid[p] = []
      valid[p].append(n)

  if valid:
    out = '\n'.join(valid[min(valid)])
    stdout.write(f'{out}\n')
  else:
    stdout.write('no such mower\n')


if __name__ == "__main__":
  main()
