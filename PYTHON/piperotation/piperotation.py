from sys import stdin, stdout

# Rating: ~ 3.4 / 10
# Link: https://open.kattis.com/problems/piperotation

def main():
  N, M = map(int, stdin.readline().split())
  sewage = [stdin.readline().strip() for i in range(N)]
  req_right = [[False] * M for y in range(N)]
  req_down = [[False] * M for y in range(N)]

  flag = True

  for r in range(N):
    if not flag:
      break

    for c in range(M):
      pipe = sewage[r][c]
      right = False
      down = False
      if c > 0:
        right = req_right[r][c-1]
      if r > 0:
        down = req_down[r-1][c]

      if pipe == 'A' and (right or down):
        flag = False
        break
      elif pipe == 'B':
        if right == down:
          flag = False
          break
        if right:
          req_right[r][c] = True
        elif down:
          req_down[r][c] = True
      elif pipe == 'C':
        if right == down:
          if not right:
            req_right[r][c] = True
            req_down[r][c] = True
        elif right:
          req_down[r][c] = True
        elif down:
          req_right[r][c] = True
      elif pipe == 'D':
        if not right or not down:
          flag = False
          break
        req_right[r][c] = True
        req_down[r][c] = True

  for x in range(N):
    if req_right[x][-1]:
      flag = False
      break
  for y in range(M):
    if req_down[-1][y]:
      flag = False
      break

  if flag:
    stdout.write('Possible\n')
  else:
    stdout.write('Impossible\n')


if __name__ == "__main__":
  main()
