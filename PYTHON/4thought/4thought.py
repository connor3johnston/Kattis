def order_of_operations(eq):
  """The equation gathered from the main method is processed into postfix
  notation based on the order of operations. The method employs a list
  that acts as a stack to maintain the seen operators."""
  copy_eq = eq.copy() #Copies original equation so that any appendages do not alter it
  check_operators = set('/*+-') #Checked against for whether or not something is an operator
  operators = [] #Tracks found operators, holding until needed
  operators.append('(') #Used to ensure the loop terminates correctly
  copy_eq.append(')') #Matches the additional left parenthesis from above
  post_fix = [] #A list containing the postfix notation
  for variable in copy_eq:
    if variable == '(':
      operators.append(variable)
    elif variable == ')':
      try:
        check = operators.pop(-1)
        while check != '(':
          post_fix.append(check)
          check = operators.pop(-1)
      except IndexError: #Used to track matching parentheses (leftover right)
        return ['Invalid']
    elif variable in check_operators: #All while loops below maintain operator precedence
      if variable == '^':
        check4 = operators.pop(-1)
        while check4 == '^':
          post_fix.append(check4)
          check4 = operators.pop(-1)
        operators.append(check4)
        operators.append(variable)
      elif variable == '/' or variable == '*':
        check2 = operators.pop(-1)
        loop_control = set('()+-')
        while check2 not in loop_control:
          post_fix.append(check2)
          check2 = operators.pop(-1)
        operators.append(check2)
        operators.append(variable)
      else:
        check3 = operators.pop(-1)
        while check3 != '(':
          post_fix.append(check3)
          check3 = operators.pop(-1)
        operators.append(check3)
        operators.append(variable)
    else:
      post_fix.append(variable)
  if operators: #Used to track matching parentheses (leftover left)
    return ['Invalid']
  else:
    return post_fix


def solve(post_fix):
  """The solve function takes in the postfix notation found
  earlier and solves the equation based on said notation.
  It employs a list as a stack to contain yet to be used
  numbers and returns a float containing the answer."""
  nums = [] #Contains unused numbers
  check_symbs = set('/*+-^') #Checked against for operators
  for variable in post_fix:
    if variable == '' or variable == ' ':
      continue
    if variable in check_symbs:
      try:
        track = 0
        second = nums.pop(-1)
        first = nums.pop(-1)
        if variable == '+': #Adds
          track = first + second
        elif variable == '-': #Subtracts
          track = first - second
        elif variable == '*': #Multiplies
          track = first * second
        elif variable == '/': #Divides
          track = first//second
        else: #Employs exponents
          track = first**second
        nums.append(track) #Places the converted value on the stack
      except ZeroDivisionError: #Catches division by zero
        return 'Invalid'
    else: #Converts the strings to floats and adds them to the stack
      nums.append(int(variable))
  return nums.pop() #Returns number after all operations applied


def main():
  possible_equations = ['4']
  start = possible_equations.pop(0)
  while len(start) <= 12:
    possible_equations.append(start + ' + 4')
    possible_equations.append(start + ' - 4')
    possible_equations.append(start + ' / 4')
    possible_equations.append(start + ' * 4')
    start = possible_equations.pop(0)
  possible_equations.append(start)
  cases = int(input())
  solved = []
  for eq in possible_equations:
    ans = solve(order_of_operations(list(eq)))
    solved.append(ans)
  for x in range(cases):
    check = int(input())
    if check in solved:
      index = solved.index(check)
      print(possible_equations[index],'=',check)
    else:
      print('no solution')



if __name__ == '__main__':
  main()
