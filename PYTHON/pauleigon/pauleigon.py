# Rating: ~ 1.6 / 10
# Link: https://open.kattis.com/problems/pauleigon

def main():
  list = input().split()
  if ((int(list[1]) + int(list[2]))//int(list[0]))%2 ==0:
	  print("paul")
  else:
	  print("opponent")


if __name__ == "__main__":
  main()
