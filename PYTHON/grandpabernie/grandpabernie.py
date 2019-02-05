# Rating: ~ 3.8 / 10
# Link: https://open.kattis.com/problems/grandpabernie

def main():
  trips = int(input())
  dict = {}
  for i in range(trips):
	  line = input().split()
	  x = []
	  if line[0] in dict:
		  x = dict[line[0]]
	  x.append(int(line[1]))
	  dict[line[0]] = x
  qs = int(input())
  for key in dict.keys():
	  y = dict[key]
	  y.sort()
  for p in range(qs):
	  here = input().split()
	  y = dict[here[0]]
	  print(y[int(here[1])-1])


if __name__ == "__main__":
  main()
