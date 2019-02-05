# Rating: ~ 2.9 / 10
# Link: https://open.kattis.com/problems/parsinghex

def main():
  hex_ = set('0123456789aAbBcCdDeEfF')
  while True:
    try:
      line = input()
      index = 0
      while index < len(line)-1:
        build = line[index:index+2].lower()
        if build == '0x':
          index2 = index+2
          while index2 < len(line):
            if line[index2] in hex_:
              index2 += 1
            else:
              break
          if line[index:index2].lower() != '0x':
            print(line[index:index2],int(line[index:index2],16))
          index = index2
          continue
        index += 1
    except EOFError:
      break


if __name__ == "__main__":
  main()

