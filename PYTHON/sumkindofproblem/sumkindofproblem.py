# Rating: ~ 1.6 / 10
# Link: https://open.kattis.com/problems/sumkindofproblem

def main():
  cases = int(input())
  for count in range(0, cases):
    line = input().split()
    K = int(line[0])
    N = int(line[1])

    odd = N**2
    even = odd + N
    total = N * (N+1) //2
    print("%d %d %d %d" % (K, total, odd, even))


if __name__ == "__main__":
  main()
