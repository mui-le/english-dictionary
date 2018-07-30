import datetime
import sys
import os

now = datetime.datetime.now()
module_name = ("daily_%0.4d%0.2d%0.2d" %(now.year, now.month, now.day))

file_name = module_name + '.py'
if os.path.exists(file_name):
    file(file_name, "r+")
else:
    file(file_name, "w")