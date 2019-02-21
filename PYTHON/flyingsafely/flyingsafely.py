# Rating: ~ 1.6 / 10
# Link: https://open.kattis.com/problems/flyingsafely

def main():
  cases = int(input())
  for _ in range(cases):
    cities, pilots = map(int, input().split())
    for _ in range(pilots):
      a,b = input().split()
    print(cities-1)


if __name__ == "__main__":
  main()
