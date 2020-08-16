#Write a script that does the following:

#Ask for user input 3 times. Once for a list of names, once for a list of missing assignment counts, and once for a list of grades. Use this input to create lists for names, assignments, and grades.
#Use a loop to print the message for each student with the correct values. The potential grade is simply the current grade added to two times the number of missing assignments.
#Template code for your script:
names =  input('Enter names in comma seperated format. \ E.g name1, name2, ...,nameN: ').title().split(',')
assignments =  input('Provide list of missing assignment counts per name in coma seperated format. E.g count1, count2, ..., countN: ').split(',')
grades =  input('Provide list of grades in coma seperated format. E.g grade1, grade2, ..., gradeN: ').split(',')

# message string to be used for each student
# HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

# write a for loop that iterates through each set of names, assignments, and grades to print each student's message

input_zipped = zip(names, assignments, grades)
for name, assignment, grade in input_zipped:
    potential_grade = int(grade) + (2*int(assignment))
    print(message.format(name, assignment, grade, potential_grade))
