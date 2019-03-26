# Rating: ~ 3.1 / 10
# Link: https://open.kattis.com/problems/color

def main():
  S, C, K = map(int, input().split())
  temp = [int(x) for x in input().split()]
  socks = sorted(temp)
  count = 1
  capacity = 1
  index = 1
  check = 0
  while index < len(socks):
    dif = abs(socks[index] - socks[check])
    if dif <= K and capacity + 1 <= C:
      capacity += 1
    else:
      count += 1
      check = index
      capacity = 1
    index += 1
  print(count)


if __name__ == "__main__":
  main()
