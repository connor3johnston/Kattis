# Rating: ~ 2.1 / 10
# Link: https://open.kattis.com/problems/towering

def main():
  line = [int(x) for x in input().split()]
  h1 = line.pop(-1)
  h2 = line.pop(-1)
  here = find(line, h1)
  print1 = list()
  for x in here:
    print1.append(line[x])
  print2 = list(set(line) - set(print1))
  print1 = [str(p) for p in sorted(print1, reverse = True)]
  print2 = [str(p) for p in sorted(print2, reverse = True)]
  print(' '.join(print2), ' '.join(print1))


def find(line, h1):
  for a in range(6):
    for b in range(a+1,6):
      for c in range(b+1,6):
        check = line[a] + line[b] + line[c]
        if check == h1:
          return [a,b,c]
  return


if __name__ == "__main__":
  main()
