#import os
#os.system('cls' if os.name == 'nt' else 'clear')

import os

print(os.name)

if os.name == "nt":
    print("This seems to be Windows")
else:
    print("likely you run Linux")

