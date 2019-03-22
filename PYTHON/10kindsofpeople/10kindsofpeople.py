# Rating: ~ 5.4 / 10
# Link: https://open.kattis.com/problems/10kindsofpeople
# curRow*cols + curCol

def union(connections, in1, in2):
  connections[find(connections, in2)] = find(connections, in1)


def find(connections, index):
  if connections[index] == index:
    return index
  connections[index] = find(connections, connections[index])
  return connections[index]


def main():
  rows, cols = map(int, input().split())
  map_ = list()
  connections = list(range(rows*cols))
  for x in range(rows):
    map_.append(input())
  for r in range(rows):
    for c in range(cols):
      if r < rows-1 and map_[r+1][c] == map_[r][c]:
        union(connections, r*cols+c, (r+1)*cols+c)
      if c < cols - 1 and map_[r][c+1] == map_[r][c]:
        union(connections, r*cols+c, r*cols+c+1)
  cases = int(input())
  for _ in range(cases):
    r1, c1, r2, c2 = map(int, input().split())
    r1 -= 1
    c1 -= 1
    r2 -= 1
    c2 -= 1
    if find(connections, r1 * cols + c1) == find(connections, r2 * cols + c2):
      if map_[r1][c1] == '1':
        print('decimal')
      else:
        print('binary')
    else:
      print('neither')


if __name__ == "__main__":
  main()
