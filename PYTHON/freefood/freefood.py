# Rating: ~ 1.3 / 10
# Link: https://open.kattis.com/problems/freefood

def main():
  days = set()
  cases = int(input())
  for x in range(cases):
    line = [int(x) for x in input().split()]
    days = days.union(range(line[0],line[1]+1))
  print(len(days))


if __name__ == "__main__":
  main()
