from sys import stdin, stdout

# Rating: ~ 2.6 / 10
# Link: https://open.kattis.com/problems/snappereasy

def main():
  cases = int(stdin.readline())
  for i in range(cases):
    snappers, snaps = map(int, stdin.readline().split())
    base = 2 ** snappers
    state = 'OFF'

    if (snaps + 1) % base == 0:
      state = 'ON'

    stdout.write(f'Case #{i + 1}: {state}\n')


if __name__ == "__main__":
  main()
