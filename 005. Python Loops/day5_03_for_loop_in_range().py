# a for loop in range() - is used to repeat code a specific number of times - usually when you want to loop through a sequence of numbers.

# syntax: 
# for i in range(start, stop, step)
#   do something.

# start - the first number (default is 0)
# stop - the number where the loop stops (not included)
# step - how much to increase each time (default is 1)

for i in range(1, 10, 2):
    print(i)

# code challenge: The Gauss Challenge (add 1 - 100)

total = 0
for num in range (1, 101):
    total += num

print(total)