from sys import stdin, stdout

# Rating: ~ 2.3 / 10
# Link: https://open.kattis.com/problems/keywords

def main():
  lines = stdin.readlines()
  non = set()

  for word in lines[1:]:
    word = word.strip().lower()
    word = word.replace('-', ' ')
    non.add(word)

  stdout.write(f'{len(non)}\n')


if __name__ == "__main__":
  main()
