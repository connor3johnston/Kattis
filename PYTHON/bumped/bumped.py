import heapq

from sys import maxsize
from sys import stdin

# Rating: ~ 4.5 / 10
# Link: https://open.kattis.com/problems/bumped

class Graph():

  def __init__(self, vertices):
    self.vertices = vertices
    self.graph = [dict() for x in range(vertices)]


  def dijkstra(self, src):
    dist = [maxsize] * self.vertices
    pq = [(0, src)]

    while pq:
      length, city = heapq.heappop(pq)

      if dist[city] == maxsize:
        dist[city] = length

        for dest in self.graph[city]:
          if dist[dest] == maxsize:
            heapq.heappush(pq, (length + self.graph[city][dest], dest))

    return dist


def main():
  n, m, f, s, t = map(int, stdin.readline().split())
  graph = Graph(n)
  flights = list()

  for x in range(m):
    a, b, c = map(int, stdin.readline().split())
    graph.graph[a][b] = c
    graph.graph[b][a] = c

  for y in range(f):
    u, v = map(int, stdin.readline().split())
    flights.append((u, v))

  one = graph.dijkstra(s)
  two = graph.dijkstra(t)

  minCost = one[t]

  for flight in flights:
    if minCost > one[flight[0]] + two[flight[1]]:
      minCost = one[flight[0]] + two[flight[1]]

  print(minCost)


if __name__ == "__main__":
  main()
