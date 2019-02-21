# Rating: ~ 1.4 / 10
# Link: https://open.kattis.com/problems/detaileddifferences

def main():
  cases = int(input())
  for x in range(cases):
    line1 = input()
    line2 = input()
    build = ''
    for index, letter in enumerate(line1):
      if letter == line2[index]:
        build += '.'
      else:
        build += '*'
    print(line1)
    print(line2)
    print(build)
    print()


if __name__ == "__main__":
  main()
