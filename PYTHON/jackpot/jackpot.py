# Rating: ~ 3.2 / 10
# Link: https://open.kattis.com/problems/jackpot

def lcm(a, b):
  return a * b // gcd(a, b)


def gcd(a, b):
  while b > 0:
    a, b = b, a % b
  return a


def main():
  machines = int(input())
  for n in range(machines):
    w = int(input())
    periods = [int(x) for x in input().split()]

    curr_lcm = 1
    overflow = False
    for period in periods:
      curr_lcm = lcm(period, curr_lcm)

      if curr_lcm > 10**9:
        overflow = True
        break

    if overflow:
      print('More than a billion.')
    else:
      print(curr_lcm)


if __name__ == "__main__":
  main()
