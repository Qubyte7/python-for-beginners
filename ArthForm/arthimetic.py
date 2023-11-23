print("Start of the programm")
temporylist = list()
# temporylist=input("enter numbers :")
# print(temporylist)

temporylist = ["32+698","45+43"]
for i in temporylist:
    print(i)
    numbers  = i.split('+')
    num1 = int(numbers[0])
    num2 = int(numbers[1])
    print(num1)

    print("+",num2)
    print("----------")

    sum = num1 + num2
    print(sum)
        








