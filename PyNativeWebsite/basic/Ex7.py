# Exercise 7: Return the count of a given substring from a string
# Write a program to find how many times substring “Emma” appears in the given string.

str_x = "Emma is good developer. Emma is a writer"

def cont_occur(substr):
    str_x = "Emma is good developer. Emma is a writer"
    return f"Emma is counted {str_x.count(substr)}"

print(cont_occur('Emma'))