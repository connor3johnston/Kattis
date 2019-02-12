# Rating: ~ 1.4 / 10
# Link: https://open.kattis.com/problems/icpcawards

def main():
  awards = dict()
  cases = int(input())
  while len(awards) < 12:
    line = input().split()
    if line[0] not in awards:
      awards[line[0]] = line[1]
  for key in awards:
    print(key,awards[key])


if __name__ == "__main__":
  main()
