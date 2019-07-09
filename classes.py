class Patient():
    def __init__(self,name, age, cnic, father_name = "not specified"):
         print("I am a constructor")
         self.name = name
         self.age = age
         self.cnic = cnic     
         self.father_name = father_name
         self.__abc = "karachi" 
    def describe_full_name(self):
             print(f'{self.name} {self.father_name}')
    def alter_age(self, increment):
        self.age+= increment
    def blah(self):
        print(self.__abc)


new_patient = Patient("Hamza", 25, "42101202300320","ali")
print(new_patient.age)
# new_patient.describe_full_name()
# new_patient.age = 28
# print(new_patient.age)
#  new_patient_2 = Patient("ZOHAIB", 26, "421567302300320")
#  print(new_patient.name)
#  print(new_patient_2.name)
new_patient.alter_age(4)
print(new_patient.age)

print(new_patient.__abc = "jsaim")
new_patient.blah()


        #string formatting
# name = "zoahiab"
# age = 25

# print(f" my name is {name} and my age is {age}")
 