# Rating: ~ 3.6 / 10
# Link: https://open.kattis.com/problems/awkwardparty

def main():
  people = int(input())
  table = [int(x) for x in input().split()]
  repeat = {}
  lowest = people
  track = []
  for index, person in enumerate(table):
    if person in repeat:
      lowest = min(lowest,index - repeat[person])
    repeat[person] = index
  print(lowest)


if __name__ == "__main__":
  main()
