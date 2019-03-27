# Rating: ~ 2.6 / 10
# Link: https://open.kattis.com/problems/bottledup

def main():
  s, v1, v2 = map(int, input().split())
  check = -1
  count1 = 0
  count2 = 0
  for x in range(s+1):
    dif = s - x
    if x % v2 == 0 and dif % v1 == 0:
      check = x
      count1 = dif//v1
      count2 = x//v2
      break
  if check == -1:
    print('Impossible')
  else:
    print(count1, count2)


if __name__ == "__main__":
  main()
