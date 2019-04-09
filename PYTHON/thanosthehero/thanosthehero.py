# Rating: ~ 3.5 / 10
# Link: https://open.kattis.com/problems/thanosthehero

def main():
  N = int(input())
  worlds = [int(x) for x in input().split()]
  dead = 0
  for y in range(N-1,0,-1):
    if worlds[y] < y-1:
      print(1)
      return
    if worlds[y] <= worlds[y-1]:
      temp = worlds[y] - 1
      dead += worlds[y-1] - temp
      worlds[y-1] = temp
  print(dead)


if __name__ == "__main__":
  main()
