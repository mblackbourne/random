####################################################
#                                                  #
#  Author: Maximus Blackbourne                     #
#                                                  #
#  PassMkr = Password Maker                        #
#                                                  #
#  LIC MIT/GNU HAVE FUN!!                          #
####################################################

import string
from random import *


characters = string.ascii_letters+string.punctuation+string.digits
password = "".join(choice(characters) for x in range(8,16))
print(password)
