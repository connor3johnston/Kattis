from sys import stdin, stdout

# Rating: ~ 5.0 / 10
# Link: https://open.kattis.com/problems/trainsorting

def main():
  cars = int(stdin.readline().strip())
  weights = [-1] * (2 * cars)
  ans = cars

  if cars > 2:
    for x in range(cars):
      weight = int(stdin.readline().strip())
      weights[cars + x] = weight
      weights[cars - x] = weight

    lis = [1] * (2 * cars)
    for i in range(1, 2 * cars):
      for j in range(1, i):
        if weights[i] > weights[j] and lis[j] + 1 > lis[i]:
          lis[i] = lis[j] + 1

    ans = max(lis)

  stdout.write('%s\n' % ans)


if __name__ == "__main__":
  main()
