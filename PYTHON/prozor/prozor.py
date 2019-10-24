# Rating: ~ 1.6 / 10
# Link: https://open.kattis.com/problems/prozor

def count(win, r, c, k):
  here = 0
  for x in range(r + 1, r + k):
    for y in range(c + 1, c + k):
      if win[x][y] == '*':
        here += 1

  return here


def main():
  R, S, K = map(int, input().split())
  win = []
  maxF = 0
  maxR = 0
  maxC = 0

  for x in range(R):
    win.append(list(input()))

  for r in range(R - K + 1):
    for c in range(S - K + 1):
      here = count(win, r, c, K - 1)
      if here > maxF:
        maxF = here
        maxR = r
        maxC = c

  win[maxR][maxC] = '+'
  win[maxR + K - 1][maxC] = '+'
  win[maxR][maxC + K - 1] = '+'
  win[maxR + K - 1][maxC + K - 1] = '+'

  for x in range(maxR + 1, maxR + K - 1):
    win[x][maxC] = '|'
    win[x][maxC + K - 1] = '|'

  for y in range(maxC + 1, maxC + K - 1):
    win[maxR][y] = '-'
    win[maxR + K - 1][y] = '-'

  print(maxF)
  for line in win:
    print(''.join(line))


if __name__ == "__main__":
  main()
