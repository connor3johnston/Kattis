# Rating: ~ 2.6 / 10
# Link: https://open.kattis.com/problems/pairingsocks

def main():
  numSocks = int(input())
  socks = [int(x) for x in input().split()]
  aux = list()
  moves = 0
  while socks:
    if aux and socks[-1] == aux[-1]:
      aux.pop()
      socks.pop()
    else:
      aux.append(socks.pop())
    moves += 1

  if aux:
    print('impossible')
  else:
    print(moves)


if __name__ == "__main__":
  main()
