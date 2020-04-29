# Rating: ~ 2.5 / 10
# Link: https://open.kattis.com/problems/aprizenoonecanwin

def main():
  num_items, min_cost = map(int, input().split())
  prices = [int(x) for x in input().split()]
  prices.sort(reverse=True)

  index = 0
  for i in range(1, num_items):
    if prices[i] + prices[i-1] <= min_cost:
      index = i
      break

  if index == num_items or index == 0:
    print(1)
  else:
    print(num_items - index + 1)


if __name__ == "__main__":
  main()
