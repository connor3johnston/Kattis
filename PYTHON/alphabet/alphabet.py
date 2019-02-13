# Rating: ~ 2.9 / 10
# Link: https://open.kattis.com/problems/alphabet

def main():
  line = input()
  LIS = [1] * len(line)
  j = 0
  for i in range(1,len(line)):
    while j < i:
      if ord(line[i]) > ord(line[j]):
        LIS[i] =  max(LIS[i], LIS[j]+1)
      j += 1
    j = 0
  print(26-max(LIS))


if __name__ == "__main__":
  main()
