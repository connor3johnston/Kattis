from itertools import product

# Rating: ~ 2.8 / 10
# Link: https://open.kattis.com/problems/4thought

def main():
  symbols = ['+', '-', '*', '//']
  equations = product(symbols, repeat=3)
  solved = {}

  for eq in equations:
    formatted = f'4 {eq[0]} 4 {eq[1]} 4 {eq[2]} 4'
    ans = eval(formatted)
    solved[ans] = formatted

  cases = int(input())
  for i in range(cases):
    val = int(input())

    if val in solved:
      out = solved[val].replace('//', '/')
      print(f'{out} = {val}')
    else:
      print('no solution')


if __name__ == "__main__":
  main()
