# Rating: ~ 1.3 / 10
# Link: https://open.kattis.com/problems/grassseed

def main():
  C = float(input())
  L = int(input())

  total = 0
  for _ in range(L):
    w, l = map(float, input().split())
    total += C * w * l

  print(f'{total:.8f}')


if __name__ == "__main__":
  main()
