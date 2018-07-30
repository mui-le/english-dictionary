import datetime
import sys

now = datetime.datetime.now()
module_name = ("daily_%0.4d%0.2d%0.2d" %(now.year, now.month, now.day))

__import__(module_name)

dictionary_list = sys.modules[module_name]
dics = dictionary_list.my_word_list

word_list = dics.keys()
for word in word_list:
    print word + "\n"

