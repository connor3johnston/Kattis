# Rating: ~ 2.8 / 10
# Link: https://open.kattis.com/problems/averageshard

def main():
  cases = int(input())

  for x in range(cases):
    input()
    nums = input().split()
    ncs = int(nums.pop(0))
    ne = int(nums.pop(0))
    students_total = []
    while len(students_total) != ncs + ne:
      students_total.extend([int(x) for x in input().split()])
    comp_stu = students_total[0:ncs]
    econ_stu = students_total[ncs::]
    comp_avg = sum(comp_stu)/ncs
    econ_avg = sum(econ_stu)/ne
    count = 0
    for student in comp_stu:
      if student > econ_avg and student < comp_avg:
        count += 1
    print(count)


if __name__ == "__main__":
  main()
