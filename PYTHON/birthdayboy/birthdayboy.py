# Rating: ~ 4.0 / 10
# Link: https://open.kattis.com/problems/birthdayboy

def calcDiff(days, start, end):
  switch = False
  if end[0] < start[0] or (end[0] == start[0] and end[1] < start[1]):
    temp = start
    start = end
    end = temp
    switch = True

  diff = 0
  if end[0] == start[0]:
    diff = end[1] - start[1]
  else:
    diff = days[start[0]] - start[1] + end[1]

  for z in range(start[0] + 1, end[0]):
    diff += days[z]

  if switch:
    diff = 365 - diff

  return diff


def main():
  days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
  num = int(input())
  dates = list()

  for x in range(num):
    name, date = input().split()
    day, month = map(int, date.split('-'))
    dates.append((day, month))

  dates = sorted(dates, key=lambda y: (y[0], y[1]))
  diff = dict()

  for y in range(num - 1):
    day = calcDiff(days, dates[y], dates[y + 1])

    if day in diff:
      diff[day].append(dates[y + 1])
    else:
      diff[day] = [dates[y+1]]

  day = calcDiff(days, dates[-1], dates[0])

  if day in diff:
    diff[day].append(dates[0])
  else:
    diff[day] = [dates[0]]

  maxDiff = max(diff)
  fakes = diff[maxDiff]

  fakes = sorted(fakes, key=lambda y: (calcDiff(days, (10, 29), y), y[0], y[1]))

  fakeMonth, fakeDay = fakes[0]

  fakeDay -= 1

  if fakeDay < 1:
    fakeMonth -= 1

    if fakeMonth < 1:
      fakeMonth, fakeDay = (12, 31)
    else:
      fakeMonth, fakeDay = (fakeMonth, days[fakeMonth])

  print('%02d-%02d' % (fakeMonth, fakeDay))


if __name__ == "__main__":
  main()
