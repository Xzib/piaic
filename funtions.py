
           # Basic Function 
# def arithimetic_operations(operand1, operand2, operator = '+'):
#     if operator == '+':
#         print(operand1 + operand2)  
# arithimetic_operations(2,2,'+')

        #Function with unknown arguments in tuple form
# def functions_with_unknown_args(*aall_params):
#     print(aall_params)
# functions_with_unknown_args(1)
# functions_with_unknown_args(1,2)
# functions_with_unknown_args(1,2,True)

        #Function with unknown arguments in Dictionary form
# def functions_with_unknown_args_double(**aall_params):
#     print(aall_params)
# functions_with_unknown_args_double(Name = 'Zohaib')
# functions_with_unknown_args_double(Name = 'Zohaib',fName = 'Asif')
# functions_with_unknown_args_double(Name = 'Zohaib',fName = 'Asif',age = '25')

        #function with inner funnctions

#scope of a variable
constant = 0
lst = [0,1,2,3]
def adder(*numbers):
        constant = 2*9.81*3.142
        lst = []
        lst.append(1)
        def inner():
                total = 0
                for number in numbers:
                        total += number
                print(numbers)
                print(total)
                print(lst)
                return constant * total
                
        return inner

inner_fn = adder(2,4)
print(inner_fn())
print(constant)
print(lst)                                                                                                                               
  

