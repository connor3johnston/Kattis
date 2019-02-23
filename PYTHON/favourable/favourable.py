# Rating: ~ 4.9 / 10
# Link: https://open.kattis.com/problems/favourable

def dfs(pages, ends, memory, cur):
  count = 0
  if cur in memory:
    return memory[cur]
  if cur in ends:
      return ends[cur]
  add = pages[cur]
  for x in add:
      count += dfs(pages, ends, memory, x)
  memory[cur] = count
  return count


def main():
  cases = int(input())
  for x in range(cases):
    ends = dict()
    pages = dict()
    num = int(input())
    memory = {}
    for y in range(num):
      line = input().split()
      if len(line) == 4:
        pages[int(line[0])] = [int(p) for p in line[1::]]
      elif line[1][0] == 'f':
        ends[int(line[0])] = 1
      else:
        ends[int(line[0])] = 0
    stack = [1]
    count = dfs(pages, ends, memory, 1)
    print(count)


if __name__ == "__main__":
  main()
