def my_function():
    result = 3 * 2
    return result

print(my_function())

#Functions with Outputs
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    #print(f"{formatted_f_name} {formatted_l_name}")
    return f"{formatted_f_name} {formatted_l_name}"
    #the return should be the last line of the function. Anything after will not be executed

print(format_name("AnGEla", "YU"))
print(format_name(input("What is your first name?"), input("What is your last name?")))
