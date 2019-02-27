# Rating: ~ 2.2 / 10
# Link: https://open.kattis.com/problems/engineeringenglish

def main():
  seen = set()
  while True:
    try:
      line = input().split()
    except:
      break
    build = ''
    for word in line:
      low = word.lower()
      if low in seen:
        build += '. '
      else:
        build += word + ' '
        seen.add(low)
    build = build.rstrip()
    build = build.lstrip()
    print(build)


if __name__ == "__main__":
  main()
