def my_function():
    result = 3 * 2
    return result

print(my_function())

#Functions with Outputs
def format_name(f_name, l_name):
    """Take a first and last name and format it
  to return the title case version of the name."""
    # Docstrings are used to give the description of a function. They need to be the first line after the function definition. They need to be included between three commas. And they may spin across several lines.
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    #print(f"{formatted_f_name} {formatted_l_name}")
    return f"{formatted_f_name} {formatted_l_name}"
    #the return should be the last line of the function. Anything after will not be executed

print(format_name("AnGEla", "YU"))
print(format_name(input("What is your first name?"), input("What is your last name?")))