n_student = int(input('N student: '))

student_dict = []
for x in range(n_student):
    # temp = []
    temp = input().split(' ')
    student_dict.append(temp)

passed_count = 0
class_ave = 0
for x in student_dict:
    total = sum(int(y) for y in x[2:])
    average = total/3
    status = ''
    if average >= 75:
        status = 'PASSED'
        passed_count += 1
    else:
        status = 'FAILED'
    class_ave += average

    temp = average
    top_ave = 0
    top_stud = ''
    if temp > top_ave:
        top_stud = x[0], x[1], average, status
        top_ave = average

    print(x[0], x[1], average, status)
print(top_stud)
print(passed_count)
print(class_ave/n_student)
