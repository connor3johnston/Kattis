# Rating: ~ 3.2 / 10
# Link: https://open.kattis.com/problems/polish

def main():
  validOps = set('+-*')
  case = 1
  while True:
    try:
     eq = input().split()
    except:
      break
    nums = list()
    for var in eq[::-1]:
      if var in validOps:
        try:
          first = int(nums[-1])
          second = int(nums[-2])
          nums.pop()
          nums.pop()
          if var == '*':
            nums.append(str(first * second))
          elif var == '-':
            nums.append(str(first - second))
          else:
            nums.append(str(first + second))
        except:
          nums.append(var)
      else:
        nums.append(var)
    print('Case %d:' % case, end = ' ')
    print(' '.join(list(reversed(nums))))
    case += 1


if __name__ == "__main__":
  main()
