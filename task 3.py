n = int(input("please enter n"))
n1 = 0
n2 = 1
count = 0
if n <= 0:
    print("Invalid input!")
elif n == 1:
    print(n1)
else:
    while count<n:
        print(n1)
        sum = n1 + n2
        n1 = n2
        n2 = sum
        count +=1
