# Rating: ~ 3.1 / 10
# Link: https://open.kattis.com/problems/teacherevaluation

def main():
  N, P = map(int, input().split())
  total = sum([int(x) for x in input().split()])
  avg = total/N
  count = 0

  if P == 100:
    print('impossible')
  else:
    while avg < P:
      total += 100
      N += 1
      avg = total/N
      count += 1

    print(count)


if __name__ == "__main__":
  main()
