# Rating: ~ 2.7 / 10
# Link: https://open.kattis.com/problems/incognito

def main():
  cases = int(input())
  for x in range(cases):
    num_items = int(input())
    items = {}

    for y in range(num_items):
      name, cat = input().split()
      if cat not in items:
        items[cat] = 0
      items[cat] += 1

    out = 1
    for cat in items:
      out *= items[cat] + 1

    print(out-1)


if __name__ == "__main__":
  main()
