# Rating: ~ 2.1 / 10
# Link: https://open.kattis.com/problems/peasoup

def main():
  rests = int(input())
  found = list()

  for x in range(rests):
    items = int(input())
    name = input()
    menu = set()

    for y in range(items):
      menu.add(input())

    if "pea soup" in menu and "pancakes" in menu:
      found.append(name)

  if found:
    print(found[0])
  else:
    print("Anywhere is fine I guess")


if __name__ == '__main__':
  main()
