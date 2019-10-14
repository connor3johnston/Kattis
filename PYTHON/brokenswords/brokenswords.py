# Rating: ~ 1.8 / 10
# Link: https://open.kattis.com/problems/brokenswords

def main():
  num = int(input())
  parts = {0: 0, 1: 0}

  for x in range(num):
    leftover = list(input())

    if leftover[0] == '0':
      parts[0] += 1
    if leftover[1] == '0':
      parts[0] += 1
    if leftover[2] == '0':
      parts[1] += 1
    if leftover[3] == '0':
      parts[1] += 1

  swords = 0
  while parts[0] > 1 and parts[1] > 1:
    swords += 1
    parts[0] -= 2
    parts[1] -= 2

  print(swords, parts[0], parts[1])


if __name__ == '__main__':
  main()
