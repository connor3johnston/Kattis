# Rating: ~ 4.1 / 10
# Link: https://open.kattis.com/problems/zipfsong

def main():
  n, m = map(int, input().split())
  scores = dict()
  for x in range(1,n+1):
    line = input().split()
    quality = int(line[0]) * x
    if quality in scores:
      scores[quality].append(line[1])
    else:
      scores[quality] = [line[1]]
  here = sorted(scores)
  for x in range(m):
    score = here.pop()
    print(scores[score].pop(0))
    if len(scores[score]) == 0:
      del scores[score]
    else:
      here.append(score)


if __name__ == "__main__":
  main()
