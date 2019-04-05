# Rating: ~ 3.5 / 10
# Link: https://open.kattis.com/problems/zebrasocelots

def main():
  num = int(input())
  index = num - 1
  o = list()
  for x in range(num):
    if input() == 'O':
      o.append(index)
    index -= 1
  count = 0
  for here in o:
    count += 2**(here)
  print(count)


if __name__ == "__main__":
  main()
