import datetime
import sys

if len(sys.argv) > 1:
    num_day = int(sys.argv[1]) * -1
    date_time = datetime.date.today() - datetime.timedelta(num_day)
else:
    date_time = datetime.date.today()

module_name = ("daily_%0.4d%0.2d%0.2d" %(date_time.year, date_time.month, date_time.day))

__import__(module_name)

dictionary_list = sys.modules[module_name]
dics = dictionary_list.my_word_list

word_list = dics.keys()
for word in word_list:
    print word + "\n"

