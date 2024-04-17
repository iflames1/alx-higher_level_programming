#!/usr/bin/python3
"""Adds all command line arguments to a Python list
and saves them to a file."""
import os
import sys

# Importing custom functions from previous exercises
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# Name of the file
filename = "add_item.json"

# Create an empty list if the file doesn't exist
if not os.path.exists(filename):
    my_list = []
else:
    # Load the existing list from the file
    my_list = load_from_json_file(filename)

# Add command line arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(my_list, filename)

# Set permissions for the file
os.chmod(filename, 0o744)
