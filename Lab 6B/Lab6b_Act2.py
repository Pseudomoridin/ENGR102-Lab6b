# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name:          Elayne Elphingstone
# Section:       572
# Assignment:    Lab1b, Act 2
# Date:          September 9th, 2021

#This file is the intellectual property of Elayne Elphingstone and anyone submitting the same file will be sued for copyright infringment

num = int(input("Enter an integer: "))
sum = 0
product = 1

for x in range(num + 1):
    if x != 0:
        product *= x
    sum += x

print("The sum of all integers from 0 to {} is {}".format(num, sum))
print("The product of all integers from 1 to {} is {}".format(num, product))
