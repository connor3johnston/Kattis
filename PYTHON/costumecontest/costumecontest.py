# Rating: ~ 1.9 / 10
# Link: https://open.kattis.com/problems/costumecontest

def main():
  costumeCount = dict()

  for _ in range(int(input())):
    costume = input()
    if costume in costumeCount:
      costumeCount[costume] += 1
    else:
      costumeCount[costume] = 1

  costumeCount = sorted(costumeCount.items(), key=lambda x: (x[1],x[0]))
  minCount = costumeCount[0][1]
  index = 0

  while index < len(costumeCount) and costumeCount[index][1] == minCount:
    print(costumeCount[index][0])
    index += 1


if __name__ == "__main__":
  main()
