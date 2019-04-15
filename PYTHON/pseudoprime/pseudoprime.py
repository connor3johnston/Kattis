# Rating: ~ 3.8 / 10
# Link: https://open.kattis.com/problems/pseudoprime

def isPrime(n):
  for x in range(2,int(n**.5 + 1)):
    if n % x == 0:
      return False
  return True


def main():
  p, a = map(int, input().split())
  while p != 0 or a != 0:
    if not isPrime(p) and pow(a,p,p) == a:
      print('yes')
    else:
      print('no')
    p, a = map(int, input().split())


if __name__ == "__main__":
  main()

