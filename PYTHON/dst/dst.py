from sys import stdin, stdout

# Rating: ~ 2.1 / 10
# Link: https://open.kattis.com/problems/dst

def main():
  cases = int(stdin.readline())

  for i in range(cases):
    line = stdin.readline().split()
    roll = line[0]
    D, H, M = map(int, line[1:])

    if roll == 'F':
      hours, mins = divmod(M + D, 60)
    else:
      hours, mins = divmod(M - D, 60)

    hours += H
    hours %= 24
    stdout.write(f'{hours} {mins}\n')


if __name__ == "__main__":
  main()
