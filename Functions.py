#-- FUNCTIONS
#--26/10/2019

#1. Write a function named population_density that takes two arguments, population and land_area, and returns a population density calculated from those values. I'
def population_density(population, land_area):
    return population/land_area
# test cases for your function
test1 = population_density(10, 1)
expected_result1 = 10
print("expected result: {}, actual result: {}".format(expected_result1, test1))

test2 = population_density(864816, 121.4)
expected_result2 = 7123.6902801
print("expected result: {}, actual result: {}".format(expected_result2, test2))

#2. Write a function named readable_timedelta. The function should take one argument, an integer days, and return a string that says how many weeks and days that is.
def readable_timedelta(days):
    # use integer division to get the number of weeks
    weeks = days // 7
    # use % to get the number of days that remain
    remainder = days % 7
    return "{} week(s) and {} day(s).".format(weeks, remainder)

# test your function
print(readable_timedelta(10))

#-- VARIABLE SCOPE

# Would return an error since the egg_count variable is outside the scope of the function and hence can't be changed
egg_count = 2

def buy_eggs():
    egg_count += 12 # purchase a dozen eggs

buy_eggs()


#To make it work, create an argument and pass the egg_count into it
egg_count = 0

def buy_eggs(count):
    return count + 12  # purchase a dozen eggs

egg_count = buy_eggs(egg_count)
print(egg_count)

#-- DOCSTRINGS
def readable_timedelta(days):
    # insert your docstring here
    """This tells you how many weeks and days are in a given number of days
    INPUT:
    days: simply the number oof days to be broken down
    OUTPUT:
    weeks = days//7
    rem_days = days % 7
    """
    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)

#-- LAMBDA EXPRESSIONS
# Rewrite this code to be more concise by replacing the mean function with a lambda expression defined within the call to map()

    #-- MAPS METHOD
numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]
"""def mean(num_list):
    return sum(num_list) / len(num_list)
averages = list(map(mean, numbers))
print(averages)"""

averages = list(map(lambda x:sum(x)/len(x), numbers))
print(averages)

    #-- FILTER
#Rewrite this code to be more concise by replacing the is_short function with a lambda expression defined within the call to filter()
cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

"""def is_short(name):
    return len(name) < 10
short_cities = list(filter(is_short, cities))
print(short_cities)"""

short_cities = list(filter(lambda x: len(x)<10, cities))
print(short_cities)