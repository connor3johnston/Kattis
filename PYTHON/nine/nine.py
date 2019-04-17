# Rating: ~ 3.1 / 10
# Link: https://open.kattis.com/problems/nine

def main():
  T = int(input())
  store = dict()
  for x in range(T):
    d = int(input())
    out = (8 * pow(9,d-1,1000000007))%1000000007
    print(out)


if __name__ == "__main__":
  main()
