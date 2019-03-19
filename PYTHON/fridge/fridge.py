# Rating: ~ 3.3 / 10
# Link: https://open.kattis.com/problems/fridge

def main():
  digits = [int(x) for x in list(input())]
  count = {x:0 for x in range(10)}
  for digit in digits:
    count[digit] += 1
  count[0] += 1
  min_ = 1001
  use = 10
  for key, value in count.items():
    if value < min_ or key < use:
      min_ = value
      use = key
  out = ''
  if use == 0:
    temp = ['0'] * (count[0])
    temp.insert(0,'1')
    out = ''.join(temp)
  else:
    temp = [str(use)] * (min_ + 1)
    out = ''.join(temp)
  print(out)


if __name__ == "__main__":
  main()
