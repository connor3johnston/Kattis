# Rating: ~ 1.3 / 10
# Link: https://open.kattis.com/problems/alphabetspam

def main():
  lowerBet = set('abcdefghijklmnopqrstuvwxyz')
  upperBet = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
  space = '_'

  lower = 0
  upper = 0
  white = 0
  other = 0

  line = list(input())

  for letter in line:
    if letter == space:
      white += 1
    elif letter in lowerBet:
      lower += 1
    elif letter in upperBet:
      upper += 1
    else:
      other += 1

  print(white/len(line))
  print(lower/len(line))
  print(upper/len(line))
  print(other/len(line))


if __name__ == "__main__":
  main()
