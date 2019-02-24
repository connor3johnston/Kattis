# Rating: ~ 2.1 / 10
# Link: https://open.kattis.com/problems/babelfish

def main():
  line = input()
  words = dict()
  while line != '':
    here = line.split()
    words[here[1]] = here[0]
    line = input()
  while True:
    try:
      word = input()
      if word in words:
        print(words[word])
      else:
        print('eh')
    except:
      break


if __name__ == "__main__":
  main()
