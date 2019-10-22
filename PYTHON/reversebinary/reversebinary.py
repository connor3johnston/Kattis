# Rating: ~ 1.4 / 10
# Link: https://open.kattis.com/problems/reversebinary

def main():
  curr = str(bin(int(input())))
  curr = curr.split('b')[1]

  print(int(''.join(reversed(curr)), 2))


if __name__ == "__main__":
  main()
