from collections import deque
from sys import stdin

# Rating: ~ 3.9 / 10
# Link: https://open.kattis.com/problems/selectgroup

def main():
  lines = [x.strip().split() for x in stdin.readlines()]
  groups = {}
  commands = {'intersection': intersection, 'union': union, 'difference': difference}

  for line in lines:
    if line[0] == 'group':
      groups[line[1]] = set(line[3:])
    else:
      commands = {'intersection': intersection, 'union': union, 'difference': difference}
      group_stack = deque([])
      groups['group'] = set()

      if line[0] not in commands:
        print(' '.join(sorted(groups[line[0]])))
      else:
        for term in reversed(line):
          if term in commands:
            s1 = groups[group_stack.pop()]
            s2 = groups[group_stack.pop()]
            groups[f'{s1}_{term}_{s2}'] = commands[term](s1, s2)
            group_stack.append(f'{s1}_{term}_{s2}')
          else:
            group_stack.append(term)

        print(' '.join(sorted(groups[f'{s1}_{term}_{s2}'])))


def intersection(s1, s2):
  return s1.intersection(s2)


def union(s1, s2):
  return s1.union(s2)


def difference(s1, s2):
  return s1.difference(s2)


if __name__ == "__main__":
  main()
