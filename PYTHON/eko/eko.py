# Rating: ~ 4.7 / 10
# Link: https://open.kattis.com/problems/eko

def main():
  N, M = map(int, input().split())
  heights = [int(x) for x in input().split()]
  heights.sort(reverse=True)

  total = 0
  for i in range(1, N):
    total += i * (heights[i - 1] - heights[i])
    if total >= M:
      break

  top = heights[i]

  if top == heights[-1]:
    i += 1

  req = top + (total - M)//i
  print(req)


if __name__ == "__main__":
  main()
