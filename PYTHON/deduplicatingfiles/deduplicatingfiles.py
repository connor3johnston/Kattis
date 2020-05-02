from sys import stdin, stdout

# Rating: ~ 4.4 / 10
# Link: https://open.kattis.com/problems/deduplicatingfiles

def main():
  files = int(stdin.readline())

  while files:
    hashes = {}
    unique = 0
    collisions = 0

    for i in range(files):
      line = stdin.readline()
      h = get_hash(line)

      if h not in hashes:
        hashes[h] = [0, {}]
      hashes[h][0] += 1

      if line in hashes[h][1]:
        hashes[h][1][line] += 1
      else:
        hashes[h][1][line] = 1

    for key in hashes:
      unique += len(hashes[key][1])
      for v in hashes[key][1].values():
        collisions += (hashes[key][0] - v) * v

    stdout.write(f'{unique} {collisions//2}\n')
    files = int(stdin.readline())


def get_hash(text):
  h = 0
  for byte in text:
    h ^= ord(byte)
  return h


if __name__ == "__main__":
  main()
