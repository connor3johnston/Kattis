# Rating: ~ 1.3 / 10
# Link: https://open.kattis.com/problems/speedlimit

def main():
  n = int(input())

  while n != -1:
    total_dist = 0
    prev_mi = 0

    for i in range(n):
      mph, curr_mi = map(int, input().split())
      total_dist += mph * (curr_mi - prev_mi)
      prev_mi = curr_mi

    print(f'{total_dist} miles')
    n = int(input())


if __name__ == "__main__":
  main()
