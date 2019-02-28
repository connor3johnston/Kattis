# Rating: ~ 2.2 / 10
# Link: https://open.kattis.com/problems/gettowork

def main():
  cases = int(input())
  for x in range(cases):
    N, T = map(int, input().split())
    E = int(input())
    towns = dict()
    for y in range(E):
      H, P = map(int, input().split())
      if H == T:
        continue
      if H in towns:
        towns[H].append(P)
      else:
        towns[H] = [P]
    out = 'Case #' + str(x+1) + ': '
    valid = True
    for z in range(1,N+1):
      if z in towns:
        total = len(towns[z])
        here = sorted(towns[z])
        sum_ = sum(towns[z])
        if sum_ < total:
          print('Case #' + str(x+1) + ': IMPOSSIBLE')
          valid = False
          break
        else:
          cars = 0
          while total > 0 and here[-1] != 0:
            total -= here.pop()
            cars += 1
          out += str(cars) + ' '
      else:
        out += '0 '
    if valid:
      print(out)


if __name__ == "__main__":
  main()
