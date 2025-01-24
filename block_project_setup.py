"""
Module: block_project_setup

Purpose: Provide functions to script project folders

Description: This module provides functions for creating a series of project folders.

Author: Matthew Block, with instruction from Dr. Denise Case
"""

#####################################
# Import Modules
#####################################
import pathlib
import utils_block
import time

#####################################
# Global Variables
#####################################

# Create a project path object
project_path = pathlib.Path.cwd()

# Create a project data path object
data_path = project_path.joinpath('data')

# Create the data path if it doesn't exist, otherwise do nothing
data_path.mkdir(exist_ok=True)

#####################################
# Define Function 1. For item in Range: Create a function to generate folders for a given range (e.g., years).
# Pass in an int for the first year
# Pass in an int for the last year
#####################################

def create_folders_for_range(start_year: int = 2024, end_year: int = 2025) -> None:
    '''
    Create folders for a given range of years.
    
    Arguments:
    start_year -- The starting year of the range (inclusive). Default is 2024.
    end_year -- The ending year of the range (inclusive). Default is 2025.
    '''
    for calendar_year in range(start_year, end_year):
        folder_name = f"{project_path}/{calendar_year}"
        pathlib.Path(folder_name).mkdir(parents=True, exist_ok=True)
    
        # Log the function call and its arguments
    print(f"FUNCTION CALLED: create_folders_for_range with start_year={start_year} and end_year={end_year}")

    

  
#####################################
# Define Function Function 2. For Item in List: Develop a function to create folders from a list of names.
# Pass in a list of folder names 
#####################################

def create_folders_from_list(folder_list: list, to_lowercase: bool = True, remove_spaces: bool = True) -> None:
    '''
    Create folders from a list of names.
    
    Arguments:
    folder_list -- A list of folder names.
    to_lowercase -- Convert folder names to lowercase. Default is True.
    remove_spaces -- Replace spaces in folder names with underscores. Default is True.
    '''
    for folder in folder_list:
        if to_lowercase:
            folder = folder.lower()
        if remove_spaces:
            folder = folder.replace(" ", "_")
        folder_name = f"{project_path}/{folder}"
        pathlib.Path(folder_name).mkdir(parents=True, exist_ok=True)
        print(f"Created folder: {folder_name} from list '{folder_list}'")
    # Log the function call and its arguments
    print(f"FUNCTION CALLED: create_folders_from_list with list {folder_list}")

    


  
#####################################
# Define Function 3. List Comprehension: Create a function to create prefixed folders by transforming a list of names and combining each with a prefix (e.g., "data-").
#####################################

def create_prefixed_folders(folder_list: list, prefix: str = 'region') -> None:
    '''Create folders from a list of names, adding a prefix to each.
    
    Arguments:
    folder_list -- A list of folder names. No defaults.
    prefix -- A prefix to add to each folder name. No defaults.
    '''
    for name in folder_list:
        # Pass in a list of folder names (ensuring lower case) and a prefix to add to each
        folder_name = f"{project_path}/{prefix}-{name.lower()}"
        pathlib.Path(folder_name.replace(" ","_")).mkdir(parents=True, exist_ok=True)
        # Log the folder creation
        print(f"Created folder: {folder_name} from list '{folder_list}'")
        
#####################################
# Define Function 4. While Loop: Write a function to create folders periodically (e.g., one folder every 5 seconds).
# Pass in the wait time in seconds
#####################################

def create_folders_periodically(duration_seconds: int = 10, quantity_of_folders: int = 7) -> None:
    '''Create folders every few seconds.
    
    Arguments:
    duration_seconds -- The number of seconds to wait between creating folders. Default is 10.
    quantity_of_folders -- The max number of folders to create. Default is 7.
    '''
    # Create folders at 10-second intervals
    for i in range(1, quantity_of_folders):
        folder_name = f"{project_path}/{i}"
        pathlib.Path(folder_name).mkdir(parents=True, exist_ok=True)
        print(f"Folder '{folder_name}' created successfully!")
        time.sleep(10)  # Wait for 10 seconds before creating the next folder
        # Log the function call and its arguments
    print(f"FUNCTION CALLED: create_folders_periodically with duration_seconds={duration_seconds} and quantity_of_folders={quantity_of_folders}")    

  
#####################################
# Define a main() function for this module.
#####################################

def main() -> None:
    ''' Main function to demonstrate module capabilities. '''

    # Start of main execution
    print("#####################################")
    print("# Starting execution of main()")
    print("#####################################\n")

    # Print byline from imported module
    print(f"Byline: {utils_block.get_byline()}")

    # Call function 1 to create folders for a range (e.g. years)
    create_folders_for_range(start_year=2020, end_year=2023)

    # Call function 2 to create folders given a list
    folder_names = ['data-csv', 'data-excel', 'data-json']
    create_folders_from_list(folder_names)

    # Call function 3 to create folders using comprehension
    folder_names = ['csv', 'excel', 'json']
    prefix = 'data-'
    create_prefixed_folders(folder_names, prefix)

    # Call function 4 to create folders periodically using while
    duration_secs:int = 5  # duration in seconds
    create_folders_periodically(duration_secs)

    # Call your function and test these options
    regions = [
      "North America", 
      "South America", 
      "Europe", 
      "Asia", 
      "Africa", 
      "Oceania", 
      "Middle East"
    ]
    create_folders_from_list(regions, to_lowercase=True, remove_spaces=True)

    # End of main execution
    print("\n#####################################")
    print("# Completed execution of main()")
    print("#####################################")


#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()

