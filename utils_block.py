"""
Module: utils_block

Purpose: Reusable Module for My Analytics Projects

Description: This module provides a byline for analytics projects. 
This byline demonstrates the use of the python statistics library to analyze data. Real data gathered by Garmin watch tracking through 2024.

Author: Matthew Block, based on the example by Dr. Case

"""

#####################################
# Import Modules
#####################################

# Import helpful modules from the Python Standard library
# See more at: https://docs.python.org/3/library/

import statistics  # provides mean(), stdev() and more....

#####################################
# Declare Global Variables
#####################################

# declare a boolean variable (has a value True or False)
has_surf_tracking_data: bool = True

# declare an integer variable 
surf_sessions_2024: int = 14

# declare a floating point variable
average_session_distance: float = 2.119285714

# declare a list of strings
surf_locations: list = ["White Plains", "Queens", "Pua'ena"]

# declare a list of numbers so we can illustrate statistics skills
waves_ridden_count: list = [5, 6, 20, 10, 7, 6, 6, 10, 3, 9, 10, 7, 12, 11]

# Calculate basic statistics using built-in Python functions and the statistics module
min_score: float = min(waves_ridden_count)  
max_score: float = max(waves_ridden_count)  
mean_score: float = statistics.mean(waves_ridden_count)
median_score: int = statistics.median(waves_ridden_count)
stdev_score: float = statistics.stdev(waves_ridden_count)

# Use a Python formatted string (f-string) to show information
# TODO: Modify the text in the byline to fit your information
# TODO: Modify the variables in the byline to use your variable names
byline: str = f"""
---------------------------------------------------------
Surfing Data: 2024
---------------------------------------------------------
Tracked Surfing Data:  {has_surf_tracking_data}
Number of Surf Sessions:         {surf_sessions_2024}
Locations:             {surf_locations}
Waves Ridden per Session: {waves_ridden_count}
Minimum Wave Count: {min_score}
Maximum Wave Count: {max_score}
Mean Wave Count: {mean_score:.2f}
Median Wave Count: {median_score}
Standard Deviation of Wave Count: {stdev_score:.2f}
"""

#####################################
# Define global functions (resuable instructions)
#####################################

def get_byline() -> str:
    '''
    Get a byline for my analytics projects.
       
    Returns a string byline that illustrates my specific skills.

    A function is a block of code that performs a task.
    This function just returns our byline.
    We can call this (or other functions) in later modules 
    so we can write it once and reuse it. 
    We use a type hint to indicate this function returns a string
    (that is, it has a Python type of str).
    It doesn't need any additional information passed in, 
    so there's nothing needed inside the parentheses.
    Everything afer the colon must be indented consistently (usually 4 spaces)
    '''
    return byline

#####################################
# Define main function for this module.
#####################################

def main() -> None:
    '''
    Print results of get_byline() when main() is called.

    This function just prints the byline to the console when we run this as a script.
    The type hint indicates this function doesn't return anything when called 
    (that is, it has a Python type of None).
    It doesn't need any additional information passed in, 
    so there's nothing inside the parentheses.
    Everything afer the colon must be indented consistently (usually 4 spaces)
    '''

    print("Starting........")
    print(get_byline())
    print("Complete.......")

#####################################
# Conditional Execution
#####################################

# If we are running this file as a script then call main()
# and verify our code works as expected.

if __name__ == '__main__':
    main()

