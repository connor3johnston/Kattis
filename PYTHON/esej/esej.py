# Rating: ~ 3.4 / 10
# Link: https://open.kattis.com/problems/esej

import math

alphabet = list('abcdefghijklmnopqrstuvwxyz')

def bfs(letter, words, needed):
  stack = [letter]
  while stack and len(words) < needed:
    cur = stack.pop(0)
    if len(cur) == 15:
      break
    for c in alphabet:
      words.append(cur + c)
      stack.append(cur + c)


def main():
  A, B = map(int, input().split())
  words = list()
  needed = math.ceil(B/2)
  for letter in alphabet:
    if len(words) >= needed:
      break
    words.append(letter)
    bfs(letter, words, needed)
  build = list()
  index = 0
  length = max(needed, A)
  while len(build) < length:
    if index >= len(words):
      index = 0
    build.append(words[index])
    index += 1
  print(' '.join(build))


if __name__ == "__main__":
  main()
