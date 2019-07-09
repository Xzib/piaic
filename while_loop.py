lst = [1,2,3,4,5,6]

print("with for loop")
for i in lst:
    print(i)
idx = 0 
print("with while loop")
while idx < len(lst):
    print(lst[idx],end=" ")
    idx += 1