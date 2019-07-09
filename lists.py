numbers = [1,2,3,4,5,6,7,8,9,10,11]
print ("before append")
print(numbers)
print("after append")
numbers.append(12)
print(numbers)
numbers.insert(2,12)
print(numbers)
print("after del")
del numbers[2]
print(numbers)
print("after remove")
numbers.remove(12)
print(numbers)
#negetive indexing start from the r8 with -1 as base of list and positive indexing start from the left with 0 as base
print(numbers[-1])
print("For LOO")
for i in range(len(numbers)):
    print(numbers[i], end=" ")