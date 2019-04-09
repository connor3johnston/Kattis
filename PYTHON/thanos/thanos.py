# Rating: ~ 3.4 / 10
# Link: https://open.kattis.com/problems/thanos

def main():
  planets = int(input())
  for x in range(planets):
    years = 0
    P, R, F = map(int, input().split())
    while P <= F:
      years += 1
      P *= R
    print(years)


if __name__ == "__main__":
  main()
