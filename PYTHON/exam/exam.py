# Rating: ~ 1.8 / 10
# Link: https://open.kattis.com/problems/exam

def main():
  know = int(input())
  yours = input()
  theirs = input()
  questions = len(yours)
  same = 0

  for x in range(questions):
    if yours[x] == theirs[x]:
      same += 1

  print(questions - abs(know - same))


if __name__ == "__main__":
  main()
