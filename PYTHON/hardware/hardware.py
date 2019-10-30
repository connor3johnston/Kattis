from sys import stdin

# Rating: ~ 2.1 / 10
# Link: https://open.kattis.com/problems/hardware

def main():
  orders = int(stdin.readline().strip())

  for x in range(orders):
    roadName = stdin.readline().strip()
    line = stdin.readline().split()
    buildings = int(line[0])
    nums = {}
    for y in range(10):
      nums[str(y)] = 0

    count = 0
    while count < buildings:
      curr = stdin.readline().split()
      if len(curr) > 1:
        for z in range(int(curr[1]), int(curr[2]) + 1, int(curr[3])):
          num = str(z)
          count += 1
          for digit in num:
            nums[digit] += 1
      else:
        num = str(curr[0])
        count += 1
        for digit in num:
          nums[digit] += 1

    print(roadName)
    print(' '.join(line))

    total = 0
    for i in range(10):
      print('Make %s digit %s' % (nums[str(i)], i))
      total += nums[str(i)]
    if total == 1:
      print('In total 1 digit')
    else:
      print('In total %s digits' % total)


if __name__ == "__main__":
  main()
