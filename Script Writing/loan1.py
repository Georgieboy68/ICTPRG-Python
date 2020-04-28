salary=float(input('Enter your annual salary: '))
time_in_job=int(input('Enter time in current job: '))
if salary >=50000 and time_in_job >=3:
    print('Loan Approved')
else:
    print('Loan Refused')