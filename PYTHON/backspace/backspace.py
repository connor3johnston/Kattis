# Rating: ~ 2.6 / 10
# Link: https://open.kattis.com/problems/backspace

def main():
  line = input()
  stack = []
  for item in line:
    if item != '<':
      stack.append(item)
    else:
      stack.pop()
  print(''.join(stack))


if __name__ == "__main__":
  main()
