# Rating: ~ 4.3 / 10
# Link: https://open.kattis.com/problems/calculator

def main():
  while True:
    try:
      print("%.2f" % eval(input()))
    except EOFError:
      break


if __name__ == "__main__":
  main()
