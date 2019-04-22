# Rating: ~ 4.0 / 10
# Link: https://open.kattis.com/problems/pikemaneasy

def main():
  problems, length = map(int, input().split())
  A, B, C, prev = map(int, input().split())

  solved = 0
  penalty = 0
  time = 0

  times = [prev]
  for x in range(1,problems):
    temp = ((A*prev+B)%C)+1
    times.append(temp)
    prev = temp
  times = sorted(times)

  while solved  < problems:
    temp = times[solved]
    if time + temp > length:
      break
    time += temp
    penalty += time
    solved += 1
  print(solved, penalty%1000000007)


if __name__ == "__main__":
  main()
