from sys import stdin

# Rating: ~ 3.8 / 10
# Link: https://open.kattis.com/problems/drivingrange

class Graph:

  def __init__(self, vertices):
    self.V = vertices
    self.graph = []


  def addEdge(self, u, v, w):
    self.graph.append([u, v, w])


  def find(self, parent, child):
    if parent[child] == child:
      return child

    parent[child] = self.find(parent, parent[child])
    return parent[child]


  def union(self, parent, rank, x, y):
    xroot = self.find(parent, x)
    yroot = self.find(parent, y)

    if rank[xroot] < rank[yroot]:
      parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
      parent[yroot] = xroot
    else:
      parent[yroot] = xroot
      rank[xroot] += 1


  def KruskalMST(self):
    result = []

    i = 0
    e = 0

    self.graph = sorted(self.graph, key=lambda item: item[2])

    parent = []
    rank = []

    for node in range(self.V):
      parent.append(node)
      rank.append(0)

    while e < self.V - 1:
      u, v, w = self.graph[i]
      i += 1
      x = self.find(parent, u)
      y = self.find(parent, v)

      if x != y:
        e = e + 1
        result.append(w)
        self.union(parent, rank, x, y)

    return result


def main():
  n, m = map(int, stdin.readline().split())

  graph = Graph(n)

  for x in range(m):
    u, v, w = map(int, stdin.readline().split())
    graph.addEdge(u, v, w)

  if m < n:
    print('IMPOSSIBLE')
  else:
    result = graph.KruskalMST()
    print(max(result))


if __name__ == "__main__":
  main()
