from math import sqrt

# Rating: ~ 3.0 / 10
# Link: https://open.kattis.com/problems/falling

def main():
  D = int(input())
  found = False

  for i in range(D):
    j = sqrt(D + i ** 2)

    if j == int(j):
      print(i, int(j))
      return
  print('impossible')


if __name__ == "__main__":
  main()
