
A_score=90
B_score=80
C_score=70
D_score=50
score=int(input('Input Test Scores:'))
if score >= A_score and score <= 100: 
    print('your grade is High Distiction')
else:
    if score >= B_score and score <= 89:
       print('Your grade is a Distinction')
    else:
        if score >= C_score and score <=79:
            print('your grade is Credit')
        else:
            if score >= D_score and score <=69:
                print('Your grade is Pass')
            else:
                print('your grade is F')