# Rating: ~ 1.2 / 10
# Link: https://open.kattis.com/problems/quadrant

def main():
  x = int(input())
  y = int(input())
  if x < 0:
    if y < 0:
      print(3)
    else:
      print(2)
  else:
    if y < 0:
      print(4)
    else:
      print(1)


if __name__ == "__main__":
  main()
