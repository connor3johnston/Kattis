# Rating: ~ 2.9 / 10
# Link: https://open.kattis.com/problems/icpcteamselection

def main():
  cases = int(input())
  for x in range(cases):
    teams = int(input())
    students = [int(x) for x in input().split()]
    students = sorted(students)
    S = 0
    while students:
      students.pop()
      S += students.pop()
      students.pop(0)
    print(S)


if __name__ == "__main__":
  main()
