from sys import stdin, stdout
import math

# Rating: ~ 3.6 / 10
# Link: https://open.kattis.com/problems/communicationssatellite

class Graph:

  def __init__(self, vertices):
    self.V = vertices
    self.graph = []


  def addEdge(self, u, v, w):
    self.graph.append((u, v, w))


  def find(self, parent, child):
    if parent[child] != child:
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


  def kruskals(self):
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
        e += 1
        result.append([u, v, w])
        self.union(parent, rank, x, y)
    return result


def main():
  vertices = int(stdin.readline().strip())
  points = []
  graph = Graph(vertices)

  for x in range(vertices):
    A, B, C = map(int, stdin.readline().split())
    points.append((A, B, C))

  for x in range(vertices - 1):
    for y in range(x + 1, vertices):
      a = points[x][0] - points[y][0]
      b = points[x][1] - points[y][1]
      w = math.sqrt(a*a + b*b) - points[x][2] - points[y][2]
      graph.addEdge(x, y, w)

  out = graph.kruskals()
  print(sum(x[2] for x in out))


if __name__ == '__main__':
  main()
