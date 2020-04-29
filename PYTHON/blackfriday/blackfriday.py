# Rating: ~ 2.2 / 10
# Link: https://open.kattis.com/problems/blackfriday

def main():
  customers = int(input())
  rolls = [int(x) for x in input().split()]

  unique = set()
  for y in range(1, 7):
    if rolls.count(y) == 1:
      unique.add(y)

  if unique:
    print(rolls.index(max(unique)) + 1)
  else:
    print('none')


if __name__ == "__main__":
  main()
