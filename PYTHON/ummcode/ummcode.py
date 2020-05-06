from string import ascii_lowercase, ascii_uppercase
from sys import stdin, stdout

# Rating: ~ 3.4 / 10
# Link: https://open.kattis.com/problems/ummcode

def main():
  words = stdin.readline().split()
  invalid = set(ascii_lowercase)
  invalid = invalid.union(set(ascii_uppercase))
  invalid = invalid.union(set(range(10)))
  invalid -= set('u')
  invalid -= set('m')

  code = []
  for word in words:
    if not set(word).intersection(invalid):
      for letter in list(word):
        if letter == 'u':
          code.append('1')
        elif letter == 'm':
          code.append('0')

  out = []
  for i in range(0, len(code), 7):
    c = ''.join(code[i: i + 7])
    j = int(c, 2)
    out.append(chr(j))

  stdout.write(f"{''.join(out)}\n")


if __name__ == "__main__":
  main()
