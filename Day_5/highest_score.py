'''
You are given a list of exam scores, and you have to print out the highest score from the List. 
You will need to use what you have learnt about Lists, For Loops and Conditionals to print out 
the highest score in the list of student_scores. 
For example, if the scores were:
'''

student_scores = [8, 65, 89, 86, 55, 91, 64, 89]

highest = student_scores[0] # Stores the first number in the list into a variable called highest


for score in student_scores: 
    if score > highest: 
        highest = score

print(highest)

'''
If the new number is bigger than our current best guess (highest), we update largest to hold this new bigger number.
If the new number is smaller or equal, we ignore it and keep our current highest score.
Ever number has been checked against the current highest. highest will contain the biggest number in the list.
'''



