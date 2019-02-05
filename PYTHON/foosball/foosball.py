# Rating: ~ 4.0 / 10
# Link: https://open.kattis.com/problems/foosball

def main():
  num = int(input())
  players = input().split()
  queue = players[4::]
  scores = input()
  dynastys = {}
  WO = players[0]
  WD = players[2]
  BO = players[1]
  BD = players[3]

  dynasty = ''
  count = 1

  if scores[0] == 'W':
    dynasty = WO + ' ' + WD
    temp = WD
    WD = WO
    WO = temp
    queue.append(BD)
    BD = BO
    BO = queue.pop(0)
  else:
    dynasty = BO + ' ' + BD
    temp = BD
    BD = BO
    BO = temp
    queue.append(WD)
    WD = WO
    WO = queue.pop(0)

  for letter in scores[1::]:
    newdynasty = ''
    if letter == 'W':
      newdynasty = WO + ' ' + WD
      newdynasty2 = WD + ' ' + WO
      temp = WD
      WD = WO
      WO = temp
      queue.append(BD)
      BD = BO
      BO = queue.pop(0)
    if letter  == 'B':
      newdynasty = BO + ' '+ BD
      newdynasty2 = BD + ' ' + BO
      temp = BD
      BD = BO
      BO = temp
      queue.append(WD)
      WD = WO
      WO = queue.pop(0)
    if newdynasty == dynasty or newdynasty2 == dynasty:
      count += 1
    else:
      dynastys.setdefault(count,[])
      dynastys[count].append(dynasty)
      dynasty = newdynasty2
      count = 1
  dynastys.setdefault(count,[])
  dynastys[count].append(dynasty)
  max_ = max(dynastys.keys())
  for x in dynastys[max_]:
    print(x)


if __name__ == "__main__":
  main()
