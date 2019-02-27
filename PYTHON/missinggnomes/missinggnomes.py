# Rating: ~ 2.3 / 10
# Link: https://open.kattis.com/problems/missinggnomes

def main():
  n, m = map(int, input().split())
  found = list()
  max_ = 0
  for x in range(m):
    g = int(input())
    found.append(g)
    if g > max_:
      max_ = g
  check = set(found)
  out = ''
  cur = 0
  for index in range(len(found)):
    num = found[index]
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
