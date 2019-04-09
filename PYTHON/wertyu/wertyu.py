# Rating: ~ 3.0 / 10
# Link: https://open.kattis.com/problems/wertyu

def main():
  keyboard = list('`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;\'ZXCVBNM,./')
  while True:
    try:
      line = input()
    except:
      break
    out = ''
    for letter in line:
      if letter == ' ':
        out += ' ';
      else:
        temp = keyboard.index(letter)
        out += keyboard[keyboard.index(letter)-1]
    print(out)


if __name__ == "__main__":
  main()
