from sys import stdin, stdout

# Rating: ~ 1.6 / 10
# Link: https://open.kattis.com/problems/easiest

def main():
  N = int(stdin.readline())
  while N:
    N_sum = digit_sum(N)
    p = 11
    while True:
      if digit_sum(N * p) == N_sum:
        break
      p += 1

    stdout.write(f'{p}\n')
    N = int(stdin.readline())


def digit_sum(num):
  sum = 0
  while num:
    sum += num % 10
    num //= 10
  return sum


if __name__ == "__main__":
  main()
