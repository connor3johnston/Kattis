# Rating: ~ 5.0 / 10
# Link: https://open.kattis.com/problems/iforaneye

def main():
  swaps = {'at': '@',
           'and': '&',
           'one': '1',
           'won': '1',
           'to': '2',
           'too': '2',
           'two': '2',
           'for': '4',
           'four': '4',
           'bea': 'b',
           'be': 'b',
           'bee': 'b',
           'sea': 'c',
           'see': 'c',
           'eye': 'i',
           'oh': 'o',
           'owe': 'o',
           'are': 'r',
           'you': 'u',
           'why': 'y'}

  lines = int(input())

  for x in range(lines):
    line = input()

    out = list()
    index = 0
    length = len(line)

    while index < length:
      possible = list()

      for word in swaps:
        curr = len(word)

        if line[index:index+curr].lower() == word:
          possible.append(word)

      if possible:
        possible.sort()

        replacement = possible[-1]

        if line[index].isupper():
          out.append(swaps[replacement].upper())
        else:
          out.append(swaps[replacement])

        index += len(replacement)
      else:
        out.append(line[index])
        index += 1

    print(''.join(out))


if __name__ == "__main__":
  main()
