# Rating: ~ 2.1 / 10
# Link: https://open.kattis.com/problems/videospeedup

def main():
  n, p, k = map(int, input().split())
  stamps = [int(x) for x in input().split()]
  stamps.append(k)

  time = stamps[0]
  for x in range(n):
    diff = stamps[x+1] - stamps[x]
    percent = 1 + ((x+1) * p)/100
    time += (diff * percent)

  print(time)


if __name__ == "__main__":
  main()
