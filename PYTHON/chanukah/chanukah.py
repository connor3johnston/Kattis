# Rating: ~ 1.6 / 10
# Link: https://open.kattis.com/problems/chanukah

def main():
  cases = int(input())
  for case in range(cases):
	  line = input().split()
	  days = int(line[1])
	  candles = days*(days+1)//2+days
	  set = case + 1
	  print("%s %s" % (set, candles))


if __name__ == "__main__":
  main()
