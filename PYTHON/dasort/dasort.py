from sys import stdin, stdout

# Rating: ~ 2.9 / 10
# Link: https://open.kattis.com/problems/dasort

def main():
  P = int(stdin.readline())
  for _ in range(P):
    K, N = map(int, stdin.readline().split())
    data = list()
    while len(data) < N:
      data.extend([int(y) for y in stdin.readline().split()])

    da_count = 0
    ordered = sorted(data)
    for i in range(N):
      if data[i] != ordered[i - da_count]:
        da_count += 1

    stdout.write(f'{K} {da_count}\n')


if __name__ == "__main__":
  main()
