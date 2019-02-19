# Rating: ~ 1.9 / 10
# Link: https://open.kattis.com/problems/dasblinkenlights

def main():
  p,q,s = map(int, input().split())
  for x in range (1, s+1):
    if x%p == 0 and x%q == 0:
      print('yes')
      return
  print('no')


if __name__ == "__main__":
  main()
