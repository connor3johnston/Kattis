# Rating: ~ 2.8 / 10
# Link: https://open.kattis.com/problems/kolone

def main():
  num1, num2 = map(int, input().split())
  ants1 = input()
  ants2 = input()
  both = list()
  for x in range(num1):
    both.append(1)
  for y in range(num2):
    both.append(2)
  secs = int(input())
  for z in range(secs):
    a = 0
    while a < num1+num2-1:
      if both[a] < both[a+1]:
        temp = both[a+1]
        both[a+1] = both[a]
        both[a] = temp
        a += 1
      a += 1
  index1 = num1-1
  index2 = 0
  out = ''
  for ant in both:
    if ant == 1:
      out += ants1[index1]
      index1 -= 1
    else:
      out += ants2[index2]
      index2 += 1
  print(out)


if __name__ == "__main__":
  main()
