# Rating: ~ 1.5 / 10
# Link: https://open.kattis.com/problems/reversebinary

def main():
  print(int(''.join(list(reversed(list(bin(int(input())))[2::]))), 2))


if __name__ == "__main__":
  main()
