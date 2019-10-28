from sys import stdin, stdout
from collections import deque
import math

# Rating: ~ 3.5 / 10
# Link: https://open.kattis.com/problems/brexit

def main():
  C, P, X, L = map(int, stdin.readline().split())
  unions = dict()
  seen = dict()

  for x in range(P):
    A, B = map(int, stdin.readline().split())
    if A in unions:
      unions[A].append(B)
    else:
      unions[A] = [B]

    if B in unions:
      unions[B].append(A)
    else:
      unions[B] = [A]


  for country in unions:
    seen[country] = math.ceil(len(unions[country])/2)

  seen[L] = 0
  check = deque([L])
  while check:
    curr = check.popleft()

    for country in unions[curr]:
      seen[country] -= 1
      if seen[country] == 0:
        check.append(country)

  if seen[X] <= 0:
    print('leave')
  else:
    print('stay')


if __name__ == "__main__":
  main()
