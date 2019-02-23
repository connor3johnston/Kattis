# Rating: ~ 1.3 / 10
# Link: https://open.kattis.com/problems/trik

def main():
  ball = [1,0,0]
  line = input()
  for let in line:
    if let == 'A':
      temp = ball[0]
      ball[0] = ball[1]
      ball[1] = temp
    if let == 'B':
      temp = ball[2]
      ball[2] = ball[1]
      ball[1] = temp
    if let == 'C':
      temp = ball[0]
      ball[0] = ball[2]
      ball[2] = temp
  print(ball.index(1) + 1)


if __name__ == "__main__":
  main()
