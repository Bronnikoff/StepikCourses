import os.path
import sys

filename = "something/wrong"

try:
    if not os.path.exists(filename):
        raise ValueError("File not found", filename)
    else:
        print("OK!")
except ValueError as err:
    message, name = err.args[0], err.args[1]
    print(err.args)
    print("\n", message, name)

import traceback

try:
    raise ValueError(4, 3)
except ValueError as err:
    print(err)
    raise