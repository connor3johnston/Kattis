# Rating: ~ 3.4 / 10
# Link: https://open.kattis.com/problems/lektira

def main():
  line = input()
  perms = set()

  for x in range(len(line) - 2):
    for y in range(x + 1, len(line) - 1):
      word = line[x::-1] + line[y:x:-1] + line[-1:y:-1]
      perms.add(word)

  print(sorted(perms)[0])


if __name__ == "__main__":
  main()
