# Rating: ~ 2.7 / 10
# Link: https://open.kattis.com/problems/natrij

from datetime import timedelta

def main():
  line = [int(x) for x in input().split(':')]
  time1 = timedelta(seconds = line[2], minutes = line[1], hours = line[0])
  line = [int(x) for x in input().split(':')]
  time2 = timedelta(seconds = line[2], minutes = line[1], hours = line[0])
  if time1 == time2:
    print('24:00:00')
    return
  dif = time2 - time1
  print_ = str(dif).split(', ')
  answer = print_[0]
  if len(print_) == 2:
    answer = print_[1]
  if len(answer) != 8:
    answer = '0' + answer
  print(answer)


if __name__ == "__main__":
  main()
