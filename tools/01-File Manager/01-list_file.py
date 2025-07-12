"""
Author      : Teeraphat Kullanankanjana
Version     : 1.0  
Date        : 2025-07-12  
Copyright   : © 2025 Teeraphat Kullanankanjana. All rights reserved.  
Description : A recursive function to list all files and directories starting from the given path on CyberPi.
"""

# Import the OS module for interacting with the file system
import os  

def list_all_files(path='/'):
    """
    Recursively lists all files and directories from the specified path.
    
    Args:
        path (str): The root directory path to start listing from (default is root '/')
    """
    # Iterate through all entries in the directory specified by 'path'
    for name in os.listdir(path):
        # Construct the full path of the current entry
        full_path = path + '/' + name if path != '/' else '/' + name

        try:
            # Check if the current path is a directory
            # os.stat(full_path)[0] returns the mode bits of the file/directory
            # 0x4000 bit indicates a directory
            if os.stat(full_path)[0] & 0x4000:
                print('[DIR] ', full_path)  # Print that this is a directory
                list_all_files(full_path)   # Recursively list inside this directory
            else:
                print('[FILE]', full_path)  # Print that this is a file
        except Exception as e:
            # Handle errors such as permission denied or file not found
            print('Error accessing {}: {}'.format(full_path, e))

# Start listing from root directory
list_all_files()
