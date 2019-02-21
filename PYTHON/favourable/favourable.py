# Rating: ~ 4.9 / 10
# Link: https://open.kattis.com/problems/favourable

def dfs(pages: dict, ends: dict, check: int, visited: list):
  count = 0
  if check in ends:
    return ends[check]
  visited[check] = True
  paths = pages[check]
  for x in paths:
    if not visited[x]:
      count += dfs(pages, ends, x, visited)
  visited[check] = False
  return count


def main():
  cases = int(input())
  for x in range(cases):
    ends = dict()
    pages = dict()
    num = int(input())
    visited = [False] * 401
    for y in range(num):
      line = input().split()
      if len(line) == 4:
        pages[int(line[0])] = [int(p) for p in line[1::]]
      elif line[1][0] == 'f':
        ends[int(line[0])] = 1
      else:
        ends[int(line[0])] = 0
    count = dfs(pages, ends, 1, visited)
    print(count)


if __name__ == "__main__":
  main()

