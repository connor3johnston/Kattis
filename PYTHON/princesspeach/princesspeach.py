# Rating: ~ 1.8 / 10
# Link: https://open.kattis.com/problems/princesspeach

def main():
  N, Y = map(int, input().split())
  seen = set()

  for x in range(Y):
    seen.add(int(input()))

  for y in range(N):
    if y not in seen:
      print(y)

  print('Mario got %s of the dangerous obstacles.' % len(seen))


if __name__ == "__main__":
  main()
