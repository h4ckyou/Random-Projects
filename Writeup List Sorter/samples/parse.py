"""
@author: Mark Uche
@date: 27/06/2024
"""

import sys

file_name = sys.argv[1]

with open(file_name, "r") as f:
    content = f.readlines()

reversed_array = content[::-1]

with open("modified.md", "w") as f:
    for value in reversed_array:
        f.write(value)
