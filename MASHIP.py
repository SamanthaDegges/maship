from random import randint
print """
>>> Welcome to M.A.S.H.I.P. 
>>> Type your answers the following questions to determine your fate...
""" 

partner1 = raw_input(">>> Who do you like? ")
partner2 = raw_input(">>> Name a celebrity you'd like to date. ")
partner3 = raw_input(">>> What's the name of the person who is nearest to you? ")
partner4 = raw_input(">>> Name a person who likes you. ")

print "\n>>> Well... let's figure out where you could live. "
place1 = raw_input(">>> Name a place that you've always wanted to visit. ")
place2 = raw_input(">>> Name a place you visited and absolutely hated. ")
place3 = raw_input(">>> What's your hometown? ")
place4 = raw_input(">>> That's a nice place to be from. It explains a lot. \n\n >>> Just to shake things up, what country would you like to avoid living in? ")

print """
>>> Did you know that M.A.S.H.I.P. is an acronym?
    \t M is for mansion
    \t A is for apartment
    \t S is for shack
    \t H is for house
    \t I is for igloo
    \t P is for palace
>>> Today you will learn which one of these you will end up living in. But first, you need to provide some numerical data...
"""

number1 = raw_input(">>> What is your favorite number? ")
number2 = raw_input(">>> How many pets do you have? ")
number3 = raw_input(">>> How many years old are you? ")

number4 = raw_input("I need to know these numbers so that I can guess how many children you will have! \nHow many would you like to have? ")

print """
In case you have 100 kids, 
you're going to be working nonstop. 
No time to kiss %s or possibly %s.""" % (partner1, partner2)

job1 = raw_input("What was the title of your first job? ")
job2 = raw_input("What is the job title you've always wanted? ")
job3 = raw_input("What is %s's job? " %partner2) 
job4= "a clerk at the Department of Motor Vehicles"

#Lists
partner = [partner1, partner2, partner3, partner4]
place = [place1, place2, place3, place4]
number = [number1, number2, number3, number4]
job = [job1, job2, job3, job4]
maship = ["a mansion", "an apartment", "a shack", "a house", "an igloo", "a palace"]

'''Below is a function that determines the ultimate variable. It uses a while loop that deducts elements by placement, until one element is left, similar to Eeeny, meeny, miney, moe.
This remaining, final element is the ultimate variable.'''

def ultimate(list):
	x = randint(1,1000)
	while len(list) > 1:
		del(list[x % len(list)])	
	return list[0]


print """
Ok! I've talked to the gods and found out all about your future. I hope you're content with the results. 
	\t* You're going to marry %s.
	\t* You're going to live in %s in %s.
	\t* You're going to work as %s
	\t* You're going to have %r of children! Congratulations!
Thanks for playing M.A.S.H.I.P.""" % (ultimate(partner), ultimate(maship), ultimate(place), ultimate(job), ultimate(number))
