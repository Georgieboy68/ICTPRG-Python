A_score=85
B_score=70
C_score=55
D_score=50
score=int(input('Input Test Scores:'))
if score >= A_score:
    print('your grade is A')
else:
    if score >= B_score:
       print('Your grade is B')
    else:
        if score >= C_score:
            print('your grade is C')
        else:
            if score >= D_score:
                print('Your grade is D')
            else:
                print('your grade is F')

