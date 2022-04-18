import re

user = input("Please enter the file you want to input:")

if user == "":
    user = "regex_sum_1414800.txt"

# open the file
handle = open(user)

numlist = list()
for line in handle:
    line = line.rstrip()

    stuff = re.findall("[0-9]+", line)
    if len(stuff) < 1:
        continue

    for s in stuff:
        numlist.append(int(s))

# sum
sum = 0
for num in numlist:
    sum += num

print(sum)
