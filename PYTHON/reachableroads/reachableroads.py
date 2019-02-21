# Rating: ~ 2.5 / 10
# Link: https://open.kattis.com/problems/reachableroads

def union(track, l, r):
  parL = find(track, l)
  parR = find(track, r)
  track[parR] = parL


def find(track, x):
  if track[x] == x:
    return x
  track[x] = find(track, track[x])
  return track[x]


def main():
  cases = int(input())
  for x in range(cases):
    roads = int(input())
    track = list(range(0,roads))
    ends = int(input())
    for y in range(ends):
      line = [int(p) for p in input().split()]
      union(track, line[0], line[1])
    print_ = set()
    for _ in range(roads):
      print_.add(find(track, _))
    print(len(print_)-1)


if __name__ == "__main__":
  main()
