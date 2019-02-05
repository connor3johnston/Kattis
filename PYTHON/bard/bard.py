# Rating: ~ 2.6 / 10
# Link: https://open.kattis.com/problems/bard

def main():
  N = int(input())
  E = int(input())
  know_all = set(range(1,N+1))
  for night in range(E):
    line = [int(x) for x in input().split()]
    line.pop(0)
    line = set(line)
    if 1 in line:
      know_all = know_all.intersection(line)
    else:
      know_all = know_all.union(line)
  ans = sorted(know_all)
  for x in ans:
    print(x)

if __name__ == "__main__":
  main()
