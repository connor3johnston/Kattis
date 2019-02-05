# Rating: ~ 1.6 / 10
# Link: https://open.kattis.com/problems/heirsdilemma

def main():
  line = input().split()
  low = int(line[0])
  high = int(line[1])
  count = 0
  for i in range(low, high+1):
	  if i%2 == 1 or str(i).count('0') >= 1:
		  continue
	  here = str(i)
	  check = True
	  seen = []
	  for char in here:
		  if char in seen or i%int(char) != 0:
			  check = False
			  break
		  else:
			  seen.append(char)
	  if check:
		  count += 1
  print(count)


if __name__ == "__main__":
  main()
