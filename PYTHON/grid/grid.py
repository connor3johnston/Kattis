# Rating: ~ 3.0 / 10
# Link: https://open.kattis.com/problems/grid

def bfs(board, start, end, visited):
  q = [start]
  while q:
    current = q.pop(0)
    if current[0] == end[0] and current[1] == end[1]:
      return current[2]
    neighbors(board, current, q, visited)
  return -1


def neighbors(board, current, q, visited):
  r = current[0]
  c = current[1]
  count = current[2]
  moves = int(board[r][c])
  if r - moves > -1 and not visited[r - moves][c]:
    q.append((r - moves, c, count + 1))
    visited[r - moves][c] = True
  if r + moves < len(board) and not visited[r + moves][c]:
    q.append((r + moves, c, count + 1))
    visited[r + moves][c] = True
  if c - moves > -1 and not visited[r][c - moves]:
    q.append((r, c - moves, count + 1))
    visited[r][c - moves] = True
  if c + moves < len(board[0]) and not visited[r][c + moves]:
    q.append((r, c + moves, count + 1))
    visited[r][c + moves] = True


def main():
  n, m = map(int, input().split())
  board = list()
  visited = list()
  for x in range(n):
    board.append(list(input()))
    visited.append([False] * m)
  visited[0][0] = True
  start = (0, 0, 0)
  end = (n-1, m-1)
  count = bfs(board, start, end, visited)
  print(count)


if __name__ == "__main__":
  main()
