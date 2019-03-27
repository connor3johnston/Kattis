# Rating: ~ 3.4 / 10
# Link: https://open.kattis.com/problems/chewbacca

def main():
  N, K, Q = map(int, input().split())
  add = K-2
  for x in range(Q):
    left, right = map(int, input().split())
    countL = 0
    countR = 0
    while left != right:
      while left > right:
        countL += 1
        left = (left+add)//K
      while right > left:
        countR += 1
        right = (right+add)//K
    print(countL + countR)


if __name__ == "__main__":
  main()
