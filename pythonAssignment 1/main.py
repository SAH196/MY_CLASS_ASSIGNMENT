A = [10, 20, 30, 40]

number=input("enter the number: ")
number=int(number)
print(type(number))

for i in range(0, len(A)):
    for j in range(1, len(A)):
        if(A[i]+A[j]==number):
            print("elements: ", A[i], " ",  A[j])
            print("index: ", A.index(A[i]), " ", A.index(A[j]))
    exit
