#Task 1: Code Correction Below is a piece of Python code with incorrect indentation. Your task is to correct it.

weather = "sunny"

if weather == "sunny":
    print("Wear sunglasses!")
else:
    print("Take an umbrella!")

#Task 2: Your Mood Today Ask the user how they feel today. If they say "happy", print "That's great to hear!", and if they say "sad", print "I hope your day gets better!". Ensure your if statement is properly indented.

mood = input("How do you feel today? ")

if mood == "happy":
    print("That's great to hear!")  
elif mood == "sad":
    print("I hope your day gets better!")

# Task 3: Code Correction You have been given a piece of code with several variable and constant names that don't follow the Python naming convention. Your task is to correct them:

PI_VALUE = 3.14
user_age = 25
user_location = "New York"
maxlimit = 1000

# Task 4: Code Correction Given below are some variable assignments. Your task is to identify the data type of each variable and then use the type() function to print it out:

variable_a = "Hello, World!"
print(type(variable_a))
variable_b = 23
print(type(variable_b))
variable_c = 3.14
print(type(variable_c))
variable_d = True
print(type(variable_d))

#Task 5: Grocery Store Math Calculate the total cost of three items you'd commonly find in a grocery store, given their individual prices. For example, what would be the cost of bread, peanut butter, and jelly be? Prices don't need to be realistic.

bread = 2.50
peanut_butter = 3.50
jelly = 2.00
total_cost = bread + peanut_butter + jelly
print(total_cost)

#Task 6: Bank Interest (Extra Credit) If you have a savings account with a particular initial amount and a fixed yearly interest rate, calculate the total amount in your account after a year. So if you had $10,000 at a 7% interest write code that would tell us the amount at the end of the year. For the example the expected outcome would be $10,700.

initial_amount = 10000
interest_rate = 0.07
total_amount = initial_amount + (initial_amount * interest_rate)
print(total_amount)

#Task 7: Validating Calculations Calculate the value of a particular arithmetic expression twice: once normally, and once using parentheses. Compare the two results to see if they match.

10 * 5 + 2
(10 * 5) + 2

#Task 8: Mix and Match Combine arithmetic (+), logical (or), and comparison (>) operators in a single expression and predict the outcome. Then, compute the expression to see if the prediction was correct.

(10 > 5) or (5 + 2 > 8) #prediction: 1st is correct