students = []

while True:
    print('Press 1 to ADD Student')
    print('Press 2 to Delete Student')
    print('Press 3 to Search Student')
    print('Press 4 to Edit Student')
    print("Press 5 to print student list")
    print('Press 6 to EXIT')
    option = input('Enter 1-5')
    if option == '6':
        break
    elif option == '5':
        print(students)
    elif option == '1':
        student ={}
        student['Name']= input("Enter Student Name: ")
        student['Father Name']= input("Enter Father's Name: ")
        student['Age']= input("Enter Student Age: ")
        student['Adress']= input("Enter Address: ")
        students.append(student) 
    elif option == '2':
        print("Student elimination")
        to_remove = input("Enter student Name")
        for i in range(len(students)):
            if students[i]==to_remove:
                students.remove(to_remove)
                



