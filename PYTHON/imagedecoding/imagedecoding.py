# Rating: ~ 3.1 / 10
# Link: https://open.kattis.com/problems/imagedecoding

def main():
  lines = int(input())
  while lines != 0:
    image = list()
    lengths = set()
    for x in range(lines):
      build = ''
      line = input().split()
      curr = line[0]
      for num in line[1::]:
        build += curr * int(num)
        curr = switch(curr)
      image.append(build)
    check = set()
    for _ in image:
      print(_.strip())
      check.add(len(_))
    if len(check) > 1:
      print('Error decoding image')
    lines = int(input())
    if lines != 0:
      print()


def switch(here):
  if here == '#':
    return '.'
  return '#'


if __name__ == "__main__":
  main()
