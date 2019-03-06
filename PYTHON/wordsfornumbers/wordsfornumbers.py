# Rating: ~ 2.5 / 10
# Link: https://open.kattis.com/problems/wordsfornumbers

def main():
  teens = {'10': 'ten',
           '11': 'eleven',
           '12': 'twelve',
           '13': 'thirteen',
           '14': 'fourteen',
           '15': 'fifteen',
           '16': 'sixteen',
           '17': 'seventeen',
           '18': 'eighteen',
           '19': 'nineteen'}
  others = {'0': ['', 'zero'],
            '1': ['', 'one'],
            '2': ['twenty', 'two'],
            '3': ['thirty', 'three'],
            '4': ['forty', 'four'],
            '5': ['fifty', 'five'],
            '6': ['sixty', 'six'],
            '7': ['seventy', 'seven'],
            '8': ['eighty', 'eight'],
            '9': ['ninety', 'nine']}
  while True:
    try:
      line = input().split()
    except:
      break
    for index, x in enumerate(line):
      if x[0] in others:
        if x in teens:
          line[index] = teens[x]
        else:
          build = ''
          if len(x) == 1:
            build = others[x][1]
          else:
            build = others[x[0]][0] + '-' + others[x[1]][1]
          if build[len(build)-5::] == '-zero':
            temp = list(build)
            temp = temp[0:len(temp)-5]
            build = ''.join(temp)
          line[index] = build
    out = ' '.join(line).capitalize()
    print(out)


if __name__ == "__main__":
  main()
