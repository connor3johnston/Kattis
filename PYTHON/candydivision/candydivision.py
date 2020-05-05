from math import ceil, sqrt

# Rating: ~ 3.4 / 10
# Link: https://open.kattis.com/problems/candydivision

def main():
  N = int(input())

  valid = set()
  for i in range(0, ceil(sqrt(N))):
    if N % (i + 1) == 0:
      valid.add(i)
      valid.add(N//(i + 1) - 1)

  valid = sorted(valid)
  print(' '.join([str(j) for j in valid]))


if __name__ == "__main__":
  main()
