#program to input unique numbers in an array
a = [5]
i = 0

while i < 5:
    print("Enter a number: ")
    x = int(input())
    for j in range(0, i + 1):
        duplicate = 0
        if a[j] == x:
            duplicate = duplicate + 1
            break
    if duplicate == 0:
        a.append(x)
        i = i + 1
    else:
        print("Number duplicated, please enter an alternative number")
print(a)