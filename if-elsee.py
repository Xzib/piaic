isCNICvalid = input('Do you have CNIC which is valid')
if isCNICvalid.lower()=='yes':
    gender = input('Please specify your gender')
    if gender.lower()=='male':
        print('Please go to booth A')
    elif gender.lower()=='female':
        print('please go nto booth B')
else :
    print('Chal bhag')