# Rating: ~ 2.3 / 10
# Link: https://open.kattis.com/problems/missinggnomes

from sys import stdin, stdout

def main():
  line = stdin.readline()
  n, m = map(int, line.split())
  found = list()
  for line in stdin:
    found.append(int(line))
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
  stdout.write(out)


if __name__ == "__main__":
  main()
