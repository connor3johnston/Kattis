from sys import stdin, stdout

# Rating: ~ 2.7 / 10
# Link: https://open.kattis.com/problems/telephones

def main():
  N, M = map(int, stdin.readline().split())

  while N != 0 or M != 0:
    calls = list()
    for y in range(N):
      src, dest, start, dur = map(int, stdin.readline().split())
      calls.append((start, start + dur))

    for z in range(M):
      lower, diff = map(int, stdin.readline().split())
      upper = lower + diff
      count = 0

      for a, b in calls:
        if (lower >= a and upper < b) or (lower <= a and upper > a) or (lower < b and upper >= b):
          count += 1

      print(count)

    N, M = map(int, stdin.readline().split())


if __name__ == "__main__":
  main()
