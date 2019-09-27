from sys import stdin, stdout

# Rating: ~ 4.4 / 10
# Link: https://open.kattis.com/problems/minspantree

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

    self.graph = sorted(self.graph, key=lambda item:item[2])

    parent = []
    rank = []

    for a in range(self.V):
      parent.append(a)
      rank.append(0)

    while e < self.V - 1 and i < len(self.graph):
      u, v, w = self.graph[i]
      i += 1

      x = self.find(parent, u)
      y = self.find(parent, v)

      if x != y:
        e += 1
        result.append([u, v, w])
        self.union(parent, rank, x, y)

    if len(result) == self.V - 1:
      result = sorted(result)

      cost = sum(a[2] for a in result)
      print(str(cost))

      ans = sorted((a[0], a[1]) for a in result)
      for here in ans:
        print('%s %s' % (here[0], here[1]))
    else:
      print('Impossible')


def main():
  n, m = map(int, stdin.readline().split())

  while n != 0 or m != 0:
    graph = Graph(n)

    for x in range(m):
      u, v, w = map(int, stdin.readline().split())
      u, v = sorted((u, v))
      graph.addEdge(u, v, w)

    graph.KruskalMST()
    n, m = map(int, stdin.readline().split())


if __name__ == "__main__":
  main()
