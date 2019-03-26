# Rating: ~ 2.2 / 10
# Link: https://open.kattis.com/problems/primepath

def SieveOfEratosthenes(n):
  check = [True for i in range(n+1)]
  primes = set()
  p = 2
  while (p <= n):
    if (check[p] == True):
      primes.add(str(p))
      for i in range(p * p, n+1, p):
        check[i] = False
    p += 1
  return primes


def bfs(start, end, primes):
  stack = [(start, 0)]
  seen = {start}
  while stack:
    cur = stack.pop()
    if cur[0] == end:
      return cur[1]
    variations(cur, stack, seen, primes)


def variations(cur, stack, seen, primes):
  count = cur[1]
  for index in range(len(cur[0])):
    temp = list(cur[0])
    for x in range(10):
      temp[index] = str(x)
      num = ''.join(temp)
      if num in primes and num not in seen:
        stack.insert(0, (num, count + 1))
        seen.add(num)


def main():
  cases = int(input())
  primes = SieveOfEratosthenes(9999)
  for x in range(cases):
    start, end = map(str, input().split())
    moves = bfs(start, end, primes)
    print(moves)


if __name__ == "__main__":
  main()
