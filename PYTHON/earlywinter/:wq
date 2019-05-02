# Rating: ~ 1.9 / 10
# Link: https://open.kattis.com/problems/earlywinter

def main():
  n, d = map(int, input().split())
  prev = [int(x) for x in input().split()]
  count = 0
  for year in prev:
    if year > d:
      count += 1
    else:
      break
  if d < min(prev):
    print('It had never snowed this early!')
  else:
    print('It hadn\'t snowed this early in %d years!' % count)


if __name__ == "__main__":
  main()
