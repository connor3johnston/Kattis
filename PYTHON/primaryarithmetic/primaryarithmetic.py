# Rating: ~ 3.0 / 10
# Link: https://open.kattis.com/problems/primaryarithmetic

def main():
  line = input().split()
  while line[0] != '0' or line[1] != '0':
    carry = 0
    store = 0
    num1 = list(line[0][::-1])
    num2 = list(line[1][::-1])
    num1.extend(['0']*(10-len(num1)))
    num2.extend(['0']*(10-len(num2)))
    for index in range(10):
      if store + int(num1[index]) + int(num2[index]) > 9:
        carry += 1
        store = 1
      else:
        store = 0
    if carry == 0:
      print('No carry operation.')
    elif carry == 1:
      print('1 carry operation.')
    else:
      print('%d carry operations.' % carry)
    line = input().split()


if __name__ == "__main__":
  main()
