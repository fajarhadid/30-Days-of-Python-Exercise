# 1. Write a pattern which identifies if a string is a valid python variable
import re
def is_valid_variable(var):
    regex_pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    if re.match(regex_pattern, var):
        return True
    return False

print(is_valid_variable('first_name')) # True
print(is_valid_variable('first-name')) # False
print(is_valid_variable('1first_name')) # False
print(is_valid_variable('firstname')) # True