# Rating: ~ 2.4 / 10
# Link: https://open.kattis.com/problems/irepeatmyself

def main():
  cases = int(input())
  for x in range(cases):
    line = input()
    build = ''
    timesX = ''
    mult = len(line)
    for index in range(len(line)):
      build += line[index]
      timesX = build * mult
      if len(timesX) != len(line):
        timesX = timesX[0:len(line)]
      if timesX == line:
        print(len(build))
        break


if __name__ == "__main__":
  main()
