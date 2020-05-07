# Rating: ~ 3.3 / 10
# Link: https://open.kattis.com/problems/tgif

def main():
  days_in_month = {'JAN': 31, 'FEB': 28, 'MAR': 31, 'APR': 30,
          'MAY': 31, 'JUN': 30, 'JUL': 31, 'AUG': 31,
          'SEP': 30, 'OCT': 31, 'NOV': 30, 'DEC': 31}

  months = ['JAN', 'FEB', 'MAR', 'APR',
            'MAY', 'JUN', 'JUL', 'AUG',
            'SEP', 'OCT', 'NOV', 'DEC']

  diff = {'SAT': 6, 'SUN': 5, 'MON': 4, 'TUE': 3, 'WED': 2, 'THU': 1, 'FRI': 0}

  pres_day, pres_month = input().split()
  pres_day = int(pres_day)
  jan1 = input()

  days = get_days(months, days_in_month, pres_day, pres_month)
  reg = days % 7

  days_in_month['FEB'] = 29
  days = get_days(months, days_in_month, pres_day, pres_month)
  leap = days % 7

  if reg == diff[jan1] and leap == diff[jan1]:
    print('TGIF')
  elif reg == diff[jan1] or leap == diff[jan1]:
    print('not sure')
  else:
    print(':(')


def get_days(months, days_in_month, pres_day, pres_month):
  days = 0
  for month in months:
    if month == pres_month:
      break

    days += days_in_month[month]
  days += pres_day - 1

  return days


if __name__ == "__main__":
  main()
