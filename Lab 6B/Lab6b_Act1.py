# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name:          Elayne Elphingstone
# Section:       572
# Assignment:    Lab1b, Act 2
# Date:          September 9th, 2021

#This file is the intellectual property of Elayne Elphingstone and anyone submitting the same file will be sued for copyright infringment

init = int(input("Enter a positive integer to compute the Collatz sequence: "))
num = init
num_list = [str(num)]
i = 0

while num != 1:
    if num % 2 == 0:
        num = int(num / 2)
    else:
        num = int(3 * num + 1)
    num_list.append(str(num))
    i += 1


### Output ###
print("Here is the Collatz sequence starting at {}:".format(init))
print(", ".join(num_list))
print("It took {} iterations to reach 1".format(i))
