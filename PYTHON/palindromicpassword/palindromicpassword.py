# Rating: ~ 3.5 / 10
# Link: https://open.kattis.com/problems/palindromicpassword

def main():
  cases = int(input())
  pals = set()
  for num in range(100000, 1000000):
    cur = list(str(num))
    if cur[0:3] == cur[-1:-4:-1]:
      pals.add(int(''.join(cur)))
  for x in range(cases):
    line = int(input())
    if line in pals:
      print(line)
      continue
    difs = dict()
    for pal in pals:
      dif = abs(line-pal)
      if dif in difs:
        difs[dif].append(pal)
      else:
        difs[dif] = [pal]
    print(min(difs[min(difs)]))


if __name__ == "__main__":
  main()
