# Rating: ~ 1.4 / 10
# Link: https://open.kattis.com/problems/judgingmoose

def main():
  line = input().split()
  left = int(line[0])
  right = int(line[1])
  moose = True
  high = right
  if left == 0 and right == 0:
	  moose = False
  if left > right:
	  high = left
  if moose:
	  if left == right:
		  print("Even %d" % (high*2))
	  else:
		  print("Odd %d" % (high*2))
  else:
	  print("Not a moose")


if __name__ == "__main__":
  main()
