# Rating: ~ 3.0 / 10
# Link: https://open.kattis.com/problems/bitbybit

def main():
  cases = int(input())
  while cases != 0:
    bits = ['?'] * 32
    for x in range(cases):
      line = input().split()
      command = line[0]
      if command == 'SET':
        bits[int(line[1])] = 1
      elif command == 'CLEAR':
        bits[int(line[1])] = 0
      elif command == 'AND':
        bit1 = bits[int(line[1])]
        bit2 = bits[int(line[2])]
        if bit1 == 0 or bit2 == 0:
          bits[int(line[1])] = 0
        elif bit1 == '?' or bit2 == '?':
          bits[int(line[1])] = '?'
        else:
          bits[int(line[1])] = 1
      else:
        bit1 = bits[int(line[1])]
        bit2 = bits[int(line[2])]
        if bit1 == 1 or bit2 == 1:
          bits[int(line[1])] = 1
        elif bit1 == '?' or bit2 == '?':
          bits[int(line[1])] = '?'
        else:
          bits[int(line[1])] = 0
    out = ''
    for bit in reversed(bits):
      out += str(bit)
    print(out)
    cases = int(input())


if __name__ == "__main__":
  main()
