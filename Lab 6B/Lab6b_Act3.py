# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name:          Elayne Elphingstone
# Section:       572
# Assignment:    Lab1b, Act 2
# Date:          September 9th, 2021

#This file is the intellectual property of Elayne Elphingstone and anyone submitting the same file will be sued for copyright infringment

num = str(input("Enter a four-digit integer: "))
init = num
if len(num) < 4:
    for x in range(4 - len(num)):
        num = "0" + num
i = 0

while num != "6174":
    print(int(num),end=" > ")
    i += 1
    if i > 8:
        raise Exception("Something went wrong!")
    digit_list = [num[:1],num[1:2],num[2:3],num[3:]]
    digit_list.sort(reverse=True,key=int)
    descend = ""
    for digit in digit_list:
        descend += digit
    digit_list.sort(key=int)
    ascend = ""
    for digit in digit_list:
        ascend += digit
    num = str(int(descend) - int(ascend))
    if len(num) < 4:
        for x in range(4 - len(num)):
            num = "0" + num
    if int(num) == 0:
        break

print("{}".format(int(num)))

print("{} reaches {} via Kaprekar's routine in {} iterations".format(init, int(num), i))
