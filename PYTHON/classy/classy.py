# Rating: ~ 4.3 / 10
# Link: https://open.kattis.com/problems/classy

def fill(levels):
  scores = list()
  for level in reversed(levels):
    if level[0] == 'u':
      scores.append('2')
    elif level[0] == 'm':
      scores.append('1')
    else:
      scores.append('0')
  while len(scores) != 10:
    scores.append('1')
  return ''.join(scores)


def main():
  cases = int(input())
  for x in range(cases):
    people = int(input())
    store = list()
    for y in range(people):
      line = input().split()
      name = line[0]
      levels = line[1].split('-')
      total = fill(levels)
      store.append((total, name))
    final = sorted(store, key = lambda x: (-int(x[0]), x[1]))
    for z in final:
      temp = list(z[1])
      temp.pop()
      print(''.join(temp))
    print('==============================')


if __name__ == "__main__":
  main()
