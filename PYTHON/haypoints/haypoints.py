# Rating: ~ 2.0 / 10
# Link: https://open.kattis.com/problems/haypoints

def main():
  line = input().split()
  words = int(line[0])
  lines = int(line[1])
  dict = {}
  for x in range(words):
	  next = input().split()
	  dict[next[0]] = int(next[1])
  for y in range(lines):
	  worth = 0
	  check = input()
	  while check != ".":
		  here = check.split()
		  for word in here:
			  if word in dict:
				  worth += dict[word]
		  check = input()
	  print(worth)


if __name__ == "__main__":
  main()
