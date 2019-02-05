# Rating: ~ 4.5 / 10
# Link: https://open.kattis.com/problems/collatz

def main():
  line = [int(x) for x in input().split()]
  orig_first = line.pop(0)
  orig_second = line.pop(0)

  while orig_first != 0 and orig_second != 0:
    first = orig_first
    second = orig_second
    track_first = [first]
    track_second = [second]
    while first != 1:
      if first%2 == 0:
        first = first/2
      else:
        first = 3*first+1
      track_first.append(first)

    count = 0
    while second != 1:
      if second in track_first:
        break
      count += 1
      if second%2 == 0:
        second = second/2
      else:
        second = 3*second+1
    index_first = track_first.index(second)
    print('%d needs %d steps, %d needs %d steps, they meet at %d' % (orig_first, index_first, orig_second, count, second))
    line = [int(x) for x in input().split()]
    orig_first = line.pop(0)
    orig_second = line.pop(0)


if __name__ == "__main__":
  main()
