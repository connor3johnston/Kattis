# Rating: ~ 1.7 / 10
# Link: https://open.kattis.com/problems/owlandfox

def main():
  num = int(input())
  for x in range(num):
    val = int(input())

    if val % 10 != 0:
      val -= 1
    elif val % 100000 == 0:
      val -= 100000
    elif val % 10000 == 0:
      val -= 10000
    elif val % 1000 == 0:
      val -= 1000
    elif val % 100 == 0:
      val -= 100
    elif val % 10 == 0:
      val -= 10

    print(val)


if __name__ == "__main__":
  main()
