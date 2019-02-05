# Rating: ~ 2.4 / 10
# Link: https://open.kattis.com/problems/natjecanje

def main():
  line = [int(x) for x in input().split()]
  N = int(line[0])
  S = int(line[1])
  R = int(line[2])
  damaged = [int(x) for x in input().split()]
  reserve = [int(x) for x in input().split()]
  count = S
  for y in reserve:
	  if y in damaged:
		  count -= 1
		  del damaged[damaged.index(y)]
	  elif y - 1 in damaged:
		  count -= 1
		  del damaged[damaged.index(y - 1)]
	  elif y + 1 in damaged:
		  count -= 1
		  del damaged[damaged.index(y + 1)]
  print(count)


if __name__ == "__main__":
  main()
