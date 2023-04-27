dic = {'A+': 4.5,
       'A0': 4,
       'B+': 3.5,
       'B0': 3,
       'C+': 2.5,
       'C0': 2,
       'D+': 1.5,
       'D0': 1,
       'F': 0}

total_credit = 0
total_grade = 0
for _ in range(20):
    subject, credit, grade = input().split()
    credit = float(credit)
    if grade != 'P':
        total_credit += credit
        total_grade += credit * dic[grade]

print('%.6f' % (total_grade / total_credit))
