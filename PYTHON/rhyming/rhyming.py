from sys import stdin, stdout

# Rating: ~ 2.5 / 10
# Link: https://open.kattis.com/problems/rhyming

def get(phrase, endings):
  for ending in endings:
    check = phrase[-len(ending): len(phrase)]
    if check == ending:
      return 'YES'
  return 'NO'


def main():
  common = stdin.readline().strip()
  lists = int(stdin.readline().strip())
  endings = set()

  for x in range(lists):
    possible = set(stdin.readline().split())

    for check in possible:
      if common[-len(check):] == check:
        endings = endings.union(possible)
        break

  phrases = int(stdin.readline().strip())

  for y in range(phrases):
    phrase = stdin.readline().strip()
    print(get(phrase, endings))


if __name__ == "__main__":
  main()
