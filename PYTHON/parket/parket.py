import math

# Rating: ~ 2.2 / 10
# Link: https://open.kattis.com/problems/parket

def main():
  R, B = map(int, input().split())
  area = R+B
  out = []

  for x in range(2, math.ceil(math.sqrt(area)) + 1):
    if area % x == 0:
      y = area//x

      if (2 * y) + (2 * x) - 4 == R:
        out.append(x)
        out.append(area//x)

  out = sorted(out)
  print(out[-1], out[0])


if __name__ == '__main__':
  main()
