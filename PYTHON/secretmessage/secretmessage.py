# Rating: ~ 1.9 / 10
# Link: https://open.kattis.com/problems/secretmessage

import math

def main():
  cases = int(input())
  for x in range(cases):
    line = input()
    store = list()
    k = math.ceil(math.sqrt(len(line)))
    m = k**2
    for _ in range(m-len(line)):
      line += '*'
    index = 0
    while index < m:
      store.append(line[index:index+k])
      index += k
    out = ''
    for y in range(k):
      for z in range(k-1, -1,-1):
        out += store[z][y]
    out = out.split('*')
    print(''.join(out))


if __name__ == "__main__":
  main()
