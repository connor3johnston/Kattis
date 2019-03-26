# Rating: ~ 3.5 / 10
# Link: https://open.kattis.com/problems/grille

def rotate(grille):
  back = list()
  for col in range(len(grille[0])):
    build = list()
    for row in range(len(grille)-1,-1,-1):
      build.append(grille[row][col])
    back.append(build)
  return back


def main():
  lines = int(input())
  grille = list()
  board = list()
  for x in range(lines):
    grille.append(list(input()))
    board.append(['?']*lines)
  index = 0
  encoded = list(input())
  for _ in range(4):
    for row, line in enumerate(grille):
      for col, sym in enumerate(line):
        if sym == 'X':
          continue
        if index >= len(encoded):
          print('invalid grille')
          return
        board[row][col] = encoded[index]
        index += 1
    grille = rotate(grille)
  out = ''
  for line in board:
    for letter in line:
      if letter == '?':
        print('invalid grille')
        return
      out += letter
  if len(out) < len(encoded):
    out += ''.join(encoded[len(out)::])
  print(out)


if __name__ == "__main__":
  main()
