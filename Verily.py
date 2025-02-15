"""
Question 1: Given an input from a csv file, for example,
Input1 = "id, name, others, \n 1, pixel, 343, \n ..."
What data structures will you choose?
"""

Output1 = [[]] # nested list
Output2 = [{}] # nested dictionary

# I chose 1 and used split twice

# Then if there are some strings that should be reserved
# For example, 'id,_', we want to keep the comma 
# My implementation was to rewrite the split method -> split2

# TODO: can use regex

"""
Question 2: Given an array, find i, j where arr[i] = arr[j], and maximize arr[i] + arr[i+1] + ... + arr[j-1] + arr[j]
这个就不适合用two pointer，因为要比较sum的大小，所以用marker去追踪轨迹
"""

"""
Other non-technical questions:
Why are you interested in Verily?

Tell me about yourself / Discuss your programming experience.

What are your considerations when designing products - choosing tech stacks?
"""
