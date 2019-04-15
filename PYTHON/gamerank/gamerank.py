# Rating: ~ 3.6 / 10
# Link: https://open.kattis.com/problems/gamerank

def needed(rank):
  starsPerRank = {2: (21,25), 3: (16,20), 4: (11,15), 5: (1,10)}
  for stars in starsPerRank:
    if rank >= starsPerRank[stars][0] and rank <= starsPerRank[stars][1]:
      return stars


def main():
  seq = list(input())
  rank = 25
  legend = False
  stars = 0
  conseq = 0
  need = 2
  for result in seq:
    if result == 'W':
      stars += 1
      conseq += 1
      if conseq > 2 and rank > 5:
        stars += 1
    else:
      conseq = 0
      if rank > 0 and rank < 21:
        stars -= 1
      if stars < 0:
        if rank == 20:
          stars = 0
        else:
          rank += 1
          need = needed(rank)
          stars = need - 1
    if stars > need:
      rank -= 1
      stars = stars - need
      need = needed(rank)
      if rank == 0:
        legend = True
        break
  if legend or rank == 0:
    print('Legend')
  else:
    print(rank)


if __name__ == "__main__":
  main()
