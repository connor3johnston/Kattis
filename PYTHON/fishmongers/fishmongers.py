# Rating: ~ 4.0 / 10
# Link: https://open.kattis.com/problems/fishmongers

def main():
  n, m = map(int, input().split())
  temp = [int(x) for x in input().split()]
  fish = sorted(temp)
  count = dict()
  for _ in range(m):
    a, b = map(int, input().split())
    if b in count:
      count[b].append(a)
    else:
      count[b] = [a]
  monies = sorted(count)
  track = 0
  while monies and fish:
    amount = monies.pop()
    total = sum(count[amount])
    for z in range(total):
      if fish:
        track += amount * fish.pop()
      else:
        break
  print(track)


if __name__ == "__main__":
  main()
