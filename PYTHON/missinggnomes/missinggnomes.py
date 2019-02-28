# Rating: ~ 2.3 / 10
# Link: https://open.kattis.com/problems/missinggnomes

def main():
  n, m = map(int, input().split())
  found = list()
  for x in range(m):
    found.append(int(input()))
  check = set(found)
  out = ''
  cur = 0
  for num in found:
    while cur < num:
      cur += 1
      if cur in check:
        continue
      out += str(cur) + '\n'
    out += str(num) + '\n'
  cur += 1
  while cur <= n:
    out += str(cur) + '\n'
    cur += 1
  print(out)


if __name__ == "__main__":
  main()
