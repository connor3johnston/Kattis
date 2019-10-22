# Rating: ~ 1.9 / 10
# Link: https://open.kattis.com/problems/raggedright

def main():
  words = list()
  score = 0

  try:
    while True:
      line = input()
      words.append(len(line.strip()))
  except:
    maxLen = max(words)
    for word in words[0:-1]:
      add = (maxLen - word)**2
      score += add

    print(score)


if __name__ == "__main__":
  main()
