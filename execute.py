import datetime
import sys

now = datetime.datetime.now()
module_name = ("daily_%0.4d%0.2d%0.2d" %(now.year, now.month, now.day))

__import__(module_name)

dictionary_list = sys.modules[module_name]
dics = dictionary_list.my_word_list

word = str(sys.argv[1])

if dics.has_key(word) == False: 
    print("Not exist this word: %s" %(word))
else:
    print dics[word]['explain']

    raw_input("Let's write an example: ")
    examples = dics[word]['examples']
    for example in examples:
        print ("\n====>: %s" %(example))