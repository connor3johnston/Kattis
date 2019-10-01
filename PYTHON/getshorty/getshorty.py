from queue import PriorityQueue
import sys

# Rating: ~ 3.4 / 10
# Link: https://open.kattis.com/problems/getshorty

class Graph():

  def __init__(self, vertices):
    self.V = vertices
    self.graph = [[] for column in range(vertices)]


  def dijkstra(self):
    q = PriorityQueue()
    q.put((-1, 0))

    sptSet = [False] * self.V
    path = [0.0 for i in range(self.V + 1)]

    while not q.empty():
      f, t = q.get()

      if sptSet[t]:
        continue

      f *= -1
      path[t] = f
      sptSet[t] = True

      for edge in self.graph[t]:
        factor = edge[1]
        next_target = edge[0]

        q.put((-1 * f * factor, next_target))

    return path


def main():
  n, m = map(int, sys.stdin.readline().split())

  while n != 0 or m != 0:
    graph = Graph(n)

    for x in range(m):
      line = sys.stdin.readline().split()
      u = int(line[0])
      v = int(line[1])
      f = float(line[2])

      graph.graph[u].append((v, f))
      graph.graph[v].append((u, f))

    print('%.4f' % graph.dijkstra()[n - 1])
    n, m = map(int, sys.stdin.readline().split())


if __name__ == "__main__":
  main()
