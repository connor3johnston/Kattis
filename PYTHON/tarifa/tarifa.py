# Rating: ~ 1.2 / 10
# Link: https://open.kattis.com/problems/tarifa

def main():
  X = int(input())
  N = int(input())
  total = 0
  for i in range(N):
    total += X
    total -= int(input())
  print(total + X);


if __name__ == "__main__":
  main()
