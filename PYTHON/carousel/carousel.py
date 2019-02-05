# Rating: ~ 2.7 / 10
# Link: https://open.kattis.com/problems/carousel

def main():
  line = [int(x) for x in input().split()]
  lines = line[0]
  most = line[1]
  while not max == 0 and not lines == 0:
	  deals = {}
	  for y in range(lines):
		  here = [int(p) for p in input().split()]
		  if here[0] > most:
			  continue
		  per = here[1]/here[0]
		  if per in deals.keys():
			  temp = deals[per]
			  if here[0] > temp[0]:
				  deals[per] = here
		  else:
			  deals[per] = here
	  if len(deals) > 0:
		  low = min(deals.keys())
		  u = deals[low]
		  print("Buy", u[0], "tickets for $%d" % u[1] )
	  else:
		  print("No suitable tickets offered")
	  line = [int(x) for x in input().split()]
	  lines = line[0]
	  most = line[1]


if __name__ == "__main__":
  main()
