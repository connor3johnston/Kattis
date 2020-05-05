from sys import stdin

# Rating: ~ 3.4 / 10
# Link: https://open.kattis.com/problems/dyslectionary

def main():
  lines = stdin.readlines()
  group = []
  max_len = 0
  for line in lines:
    line = line.strip()
    if not line:
      group.sort()
      for word in group:
        print(f'{word[::-1]:>{max_len}}')
      print()
      group = []
      max_len = 0
    else:
      word = line[::-1]
      if len(word) > max_len:
        max_len = len(word)
      group.append(word)

  group.sort()
  for word in group:
    print(f'{word[::-1]:>{max_len}}')


if __name__ == "__main__":
  main()
