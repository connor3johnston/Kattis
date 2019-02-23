# Rating: ~ 3.0 / 10
# Link: https://open.kattis.com/problems/eatingout

def main():
  m, a, b, c = map(int, input().split())
  menu = [0] * m
  index = 0
  for x in range(a):
    if index == m:
      index = 0
    menu[index] += 1
    index += 1
  for x in range(b):
    if index == m:
      index = 0
    menu[index] += 1
    index += 1
  for x in range(c):
    if index == m:
      index = 0
    menu[index] += 1
    index += 1
  if max(menu) < 3:
    print('possible')
  else:
    print('impossible')


if __name__ == "__main__":
  main()
