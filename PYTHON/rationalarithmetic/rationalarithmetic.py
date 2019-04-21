# Rating: ~ 3.3 / 10
# Link: https://open.kattis.com/problems/rationalarithmetic

import math

def main():
  cases = int(input())
  for x in range(cases):
    x1, y1, op, x2, y2 = input().split()
    top = 0
    bottom = 0
    if op == '+':
      top = int(x1)*int(y2)+int(x2)*int(y1)
      bottom = int(y1)*int(y2)
    elif op == '-':
      top = int(x1)*int(y2)-int(x2)*int(y1)
      bottom = int(y1)*int(y2)
    elif op == '/':
      top = int(x1)*int(y2)
      bottom = int(x2)*int(y1)
    else:
      top = int(x1)*int(x2)
      bottom = int(y1)*int(y2)
    gcd = math.gcd(abs(top), abs(bottom))
    while gcd != 1:
      top //= gcd
      bottom //= gcd
      gcd = math.gcd(abs(top), abs(bottom))
    if bottom < 0:
      bottom *= -1
      top *= -1
    print(top, '/', bottom)


if __name__ == "__main__":
  main()
