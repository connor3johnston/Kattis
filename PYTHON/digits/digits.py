from sys import stdin
import math

# Rating: ~ 4.2 / 10
# Link: https://open.kattis.com/problems/digits

def main():
  line = stdin.readline().strip()

  while line != 'END':

    if line == '1':
      print(1)
    else:
      count = 2
      prev = len(line)
      curr = len(str(prev))

      while prev != curr:
        prev = curr
        curr = len(str(prev))
        count += 1

      print(count)

    line = stdin.readline().strip()


if __name__ == '__main__':
  main()
