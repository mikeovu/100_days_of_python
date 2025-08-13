'''
Work out the total of the numbers between 1 and 100, inclusive of both 1 and 100.
'''

total = 0 

# Always start with the first value, which is 0

for number in range (1,100):
    total += number # Take whatever total is right now and add all numbers between 1 to 100 to it.
print(total)