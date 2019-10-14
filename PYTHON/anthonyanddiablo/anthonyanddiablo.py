from math import pi, sqrt

# Rating: ~ 2.5 / 10
# Link: https://open.kattis.com/problems/anthonyanddiablo

def main():
  A, N = map(float, input().split())
  radius = sqrt(A/pi)
  circum = 2 * pi * radius

  if circum <= N:
    print('Diablo is happy!')
  else:
    print('Need more materials!')


if __name__ == "__main__":
  main()
