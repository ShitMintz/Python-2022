#1
icecream = int(input("How many ice creams do you need?"))
if icecream>20:
	print("Sorry there is not enough ice cream in stock.")
#2
distance = int(input("How far are you travelling?"))
if distance>200:
	print("You might want to fill up your tank")
#3
age = int(input("How old are you?"))
if age >= 18:
	print("You are considered an adult")
else:
	print("You are a minor")
#4
movie = input("What is your favourite movie?").lower()
if movie == "lord of the rings":
	print("You have excelent movie taste")
else:
	print("Lord of the Rings is clearly superior")
#5
darth = input("Have you heard the tale of of Darth Plagueis the Wise. ").lower()
if darth == "no":
	print("Did you ever hear the tragedy of Darth Plagueis The Wise? I thought not. It’s not a story the Jedi would tell you. It’s a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force to influence the midichlorians to create life… He had such a knowledge of the dark side that he could even keep the ones he cared about from dying. The dark side of the Force is a pathway to many abilities some consider to be unnatural. He became so powerful… the only thing he was afraid of was losing his power, which eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep. Ironic. He could save others from death, but not himself.")
else: print("You must be a fan?")
#6
christ = input("who directed Passion of the Christ?").lower()
if christ == "mel gibson":
	print("Correct")
else:
	print("Wrong It’s Mel Gibson")
