#Assigment 2: 5 Subject Percentage Calculator

# Python Program to Calculate Percentage with Grade

print('Welcome to Percentage Calculator')
print('Enter your marks in all 5 subjects respectively')

phy = float(input('Enter your marks in Physics: '))
che = float(input('Enter your marks in Chemistry: '))
math = float(input('Enter your marks in Mathematics: '))
eng = float(input('Enter your marks in English: '))
mar = float(input('Enter your marks in Marathi: '))

# Calculate total and percentage
total = phy + che + math + eng + mar
per = (total / 500) * 100

# Determine grade based on percentage
if per >= 90:
    grade = 'A+'
elif per >= 80:
    grade = 'A'
elif per >= 70:
    grade = 'B+'
elif per >= 60:
    grade = 'B'
elif per >= 50:
    grade = 'C'
else:
    grade = 'F'

# Print results
print('Your HSC Percentage is:', round(per, 2))
print('Your Grade is:', grade)
print('\nThank you for using HSC Percentage Calculator')
