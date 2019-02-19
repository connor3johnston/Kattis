# Rating: ~ 2.1 / 10
# Link: https://open.kattis.com/problems/prerequisites

def main():
  terminate = input()
  while terminate != '0':
    courses, cats = map(int, terminate.split())
    course_nums = [int(x) for x in input().split()]
    store = []
    for x in range(cats):
      store.append([int(b) for b in input().split()])
    finish = True
    for y in store:
      uni = y[2::]
      intersect = set(uni).intersection(set(course_nums))
      if len(intersect) < y[1]:
        finish = False
        break
    if finish:
      print('yes')
    else:
      print('no')
    terminate = input()


if __name__ == "__main__":
  main()
