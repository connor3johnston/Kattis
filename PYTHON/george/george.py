# Rating: ~ 2.0 / 10
# Link: https://open.kattis.com/problems/george

import heapq
import sys

class Graph():

  def __init__(self, vertices):
    self.V = vertices
    self.graph = [dict() for x in range(vertices + 1)]
    self.minister = dict()


  def minDistance(self, dist, sptSet):
    minInt = sys.maxsize
    min_index = -1

    for v in range(1, self.V + 1):
      if dist[v] < minInt  and sptSet[v] == False:
        minInt = dist[v]
        min_index = v

    return min_index


  def dijkstra(self, src, time):
    dist = [sys.maxsize] * (self.V + 1)
    dist[src] = time
    sptSet = [False] * (self.V + 1)

    for cout in range(1, self.V + 1):
      u = self.minDistance(dist, sptSet)

      if u == -1:
        continue

      sptSet[u] = True

      for v in self.graph[u]:
          wait = self.waitTime(u, v, dist[u])

          if dist[v] > dist[u] + wait and sptSet[v] == False:
            dist[v] = dist[u] + wait

    return dist


  def waitTime(self, u, v, time):
    wait = 0
    if (u, v) in self.minister and time >= self.minister[(u, v)][0] and time < self.minister[(u, v)][1]:
      wait = self.minister[(u, v)][1] - time

    return wait + self.graph[u][v]


def main():
  N, M = map(int, input().split())
  A, B, K, G = map(int, input().split())
  graph = Graph(N)
  ministerClosed = [int(x) for x in input().split()]

  for x in range(M):
    X, Y, L = map(int, input().split())
    graph.graph[X][Y] = L
    graph.graph[Y][X] = L

  enter = 0
  for x in range(G - 1):
    left = ministerClosed[x]
    right = ministerClosed[x + 1]
    add = graph.graph[left][right]
    graph.minister[(left, right)] = (enter, enter + add)
    graph.minister[(right, left)] = (enter, enter + add)
    enter += add

  here = graph.dijkstra(A, K)
  print(here[B] - K)


if __name__ == '__main__':
  main()
