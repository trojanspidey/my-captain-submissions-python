list1=[]
n = int(input("Enter number of elements to be added in list: "))
for i in range(0,n):
    num = int(input())
    list1.append(num)
set = [num for num in list1 if num>=0]
print(set)
