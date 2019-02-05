# Rating: ~ 2.2 / 10
# Link: https://open.kattis.com/problems/wordcloud

import math
def main():
  line = input().split()
  max_width = int(line[0])
  word_count = int(line[1])
  track = 1
  while max_width != 0 or word_count != 0:
    words = []
    occurences = []
    points = []
    widths = []
    for x in range(word_count):
      temp = input().split()
      words.append(temp[0])
      occurences.append(int(temp[1]))
    cmax = max(occurences)
    for index, cw in enumerate(occurences):
      points.append(math.ceil(8 + ((40*(cw-4))/(cmax-4))))
      widths.append(math.ceil((9*len(words[index])*points[index])/16))
    row = []
    total = 0
    height = 0
    for index, width in enumerate(widths):
      if total + width > max_width:
        total = width
        height += max(row)
        row = []
      else:
        total+= width
      row.append(points[index])
      total += 10
    if row:
      height += max(row)
    print('CLOUD %d: %d' % (track, height))
    track += 1
    line = input().split()
    max_width = int(line[0])
    word_count = int(line[1])


if __name__ == "__main__":
  main()
