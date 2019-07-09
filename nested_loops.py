# my_list = [1,2,3,4,5,6,7,8,9,10]
# for val in my_list:
#     count = len(my_list)
#     item = val*2
#     list_2=item
#     print(list_2)
# for i in my_list:
#     for x in range(4):
#         print(i,x)

user_val = int(input('Énter value one: '))
user_val_1 = int(input('Énter value two: '))

for i in range(user_val,user_val_1+1):
    for x in range(11):
        print (i*x,end=" ")
