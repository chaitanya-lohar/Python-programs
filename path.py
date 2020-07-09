

from pathlib import Path


obj1=Path()
# print(obj1)
# print(obj1.exists())   # by this we can existance
# obj1.mkdir()         # by which we can create any directory
# obj1.rmdir()  # short form of remove directory


for i in obj1.glob("*.py"):    # glob is used to get all files
    print(i)