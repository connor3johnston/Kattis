# Rating: ~ 2.6 / 10
# Link: https://open.kattis.com/problems/multigram

def count(line):
  occur = {}
  for letter in line:
    if letter in occur:
      occur[letter] += 1
    else:
      occur[letter] = 1

  return occur


def get(gram):
  for x in range(1, len(gram)//2 + 1):
    if len(gram) % x != 0:
      continue

    occur = count(gram[0:x])
    here = True
    for y in range(x, len(gram), x):
      check = count(gram[y: y + x])

      if check != occur:
        here = False
        break
    if here:
      return gram[0:x]
  return -1


def main():
  gram = input()
  print(get(gram))


if __name__ == "__main__":
  main()
