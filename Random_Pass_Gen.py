# Script to Generate Random Passwords
import random

lower_case = "abcdefghijklmnopqrstuvwxyz" 
upper_Case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
number = "0123456789" 
symbols = "!@#$%^&*()_+-\/"
use_for = lower_case + upper_Case + number + symbols  
length_for_pass = 10

password = "".join(random.sample(use_for, length_for_pass))
print("Your password is: ", password)