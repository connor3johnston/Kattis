# Rating: ~ 1.5 / 10
# Link: https://open.kattis.com/problems/babybites

def main():
  bites = int(input())
  line = input().split()
  check = True
  for i in range(1,bites+1):
	  if line[i-1] == "mumble":
		  continue
	  if int(line[i-1]) != i:
		  check = False
		  break
  if check:
	  print("makes sense")
  else:
	  print("something is fishy")


if __name__ == "__main__":
  main()
