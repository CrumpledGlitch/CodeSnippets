# This script predicts what percentage of your life you have lived.
# It will take two variables: Birth Year and Average Life Expectancy.
# It will then calculate the percentage of your life you have lived.

# Import the datetime module
import datetime

# Get the current year
current_year = datetime.datetime.now().year

# Get the birth year
birth_year = int(input("What year were you born? "))
# Get the average life expectancy
life_expectancy = int(input("What is the average life expectancy? "))
# Calculate the percentage of life lived
percentage_lived = (current_year - birth_year) / life_expectancy * 100
# Print the percentage of life lived
print("You have lived " + str(percentage_lived) + "% of your life.")

# Output        
# What year were you born? 1980
# What is the average life expectancy? 80
# You have lived 50.0% of your life.






