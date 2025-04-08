# Python program to clear the screen using os.system

# import only system from os
from os import system, name

# define our clear function
def clear():
   # for windows
   if name == 'nt':
      _ = system('cls')

   # for mac and linux(here, os.name is 'posix')
   else:
      _ = system('clear')

