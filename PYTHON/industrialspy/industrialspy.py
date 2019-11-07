from sys import stdin, stdout
from itertools import permutations

# Rating: ~ 3.2 / 10
# Link: https://open.kattis.com/problems/industrialspy

MAX = 10000000

def main():
  sieve = [True for i in range(MAX + 1)]
  sieve[1] = False
  p = 2

  while (p * p <= MAX):
    if sieve[p]:
      for i in range(p * p, MAX + 1, p):
        sieve[i] = False
    p += 1

  cases = int(stdin.readline().strip())

  for x in range(cases):
    num = stdin.readline().strip()

    seen = set()
    seen.add('')
    count = 0

    for y in range(1, len(num) + 1):
      perms = permutations(num, y)
      for perm in perms:
        here = ''.join(perm).strip('0')
        if here not in seen:
          seen.add(here)

          if sieve[int(here)]:
            count += 1

    print(count)


if __name__ == "__main__":
  main()
