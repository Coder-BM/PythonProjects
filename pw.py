class a(Exception):
    pass
class pw_len_less(a):
    pass

import random
from colorama import Fore, Back, Style
import string

upper = int(input(Fore.BLUE+Style.BRIGHT+"How many uppercase characters would you like? "))
lower = int(input(Fore.GREEN+Style.BRIGHT+"How many lowercase characters would you like? "))
special = int(input(Fore.YELLOW+Style.BRIGHT+"How many special characters would you like? "))
num = int(input(Fore.MAGENTA+Style.BRIGHT+"How many numbers would you like ?"))

sum = upper+lower+special+num

try:
    if sum>=8:
        upper_c = string.ascii_uppercase
        lower_c = string.ascii_lowercase
        special_c = string.punctuation
        num_c = string.digits

        pw = random.choices(upper_c,k=upper)+random.choices(lower_c,k=lower)+random.choices(special_c,k=special)+random.choices(num_c,k=num)

        random.shuffle(pw)
        pw=''.join(pw)
        print(Fore.GREEN + "Your password is Strong ")
        print(Fore.GREEN + "Your password is: " + Fore.WHITE + pw)

    else:
        raise pw_len_less
    
except:
    print(Fore.RED + "Your password is too short.")

