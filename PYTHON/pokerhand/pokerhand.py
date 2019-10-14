# Rating: ~ 1.3 / 10
# Link: https://open.kattis.com/problems/pokerhand

def main():
  rank = set('A23456789TJQK')
  cards = input().split()
  ranks = dict()

  for card in cards:
    currRank = list(card)[0]
    if currRank in ranks:
      ranks[currRank] += 1
    else:
      ranks[currRank] = 1

  maxRank = 0
  for here in ranks:
    if ranks[here] > maxRank:
      maxRank = ranks[here]

  print(maxRank)


if __name__ == "__main__":
  main()
