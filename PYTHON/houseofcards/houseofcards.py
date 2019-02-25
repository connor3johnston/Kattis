# Rating: ~ 3.5 / 10
# Link: https://open.kattis.com/problems/houseofcards

def main():
  bound = int(input())
  start = bound
  while start%40 != 0:
    start -= 1

  here = True
  while True:
    if start >= bound:
      print(start)
      break
    if here:
      start += 5
    else:
      start += 3
    here  = not here


if __name__ == "__main__":
  main()
