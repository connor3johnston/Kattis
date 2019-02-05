# Rating: ~ 2.7 / 10
# Link: https://open.kattis.com/problems/variablearithmetic

def main():
  equation = input()
  variables = {}
  zeroto100 = tuple(str(x) for x in range(0,101))
  while equation != '0':
    workequation = equation.split()
    if '=' in workequation:
      variables[workequation[0]] = workequation[2]
    else:
      useequation = equation.split(' + ')
      simplify = 0
      simp_equation = []
      for part in useequation:
        if part in zeroto100:
          simplify += int(part)
        elif part in variables:
          simplify += int(variables[part])
        else:
          simp_equation.append(part)
      if simplify != 0:
        simp_equation.insert(0,str(simplify))
      print(' + '.join(simp_equation))
    equation = input()


if __name__ == "__main__":
  main()
