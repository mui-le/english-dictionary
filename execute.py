import datetime
import sys

if len(sys.argv) > 2:
    num_day = int(sys.argv[2]) * -1
    date_time = datetime.date.today() - datetime.timedelta(num_day)
else:
    date_time = datetime.date.today()

module_name = ("daily_%0.4d%0.2d%0.2d" %(date_time.year, date_time.month, date_time.day))

__import__(module_name)

dictionary_list = sys.modules[module_name]
dics = dictionary_list.my_word_list

word = str(sys.argv[1])

if dics.has_key(word) == False: 
    print("Not exist this word: %s" %(word))
else:
    raw_input("Let's say something to decribe this word: ")
    explains = dics[word]['explain']
    if isinstance(explains, list) == False:
        print ("***: %s" %(explains))
    else:
        for exp in explains:
            print ("***: %s" %(exp))

    if len(dics[word]['examples']) >= 1:
        raw_input("Let's write an example: ")
        examples = dics[word]['examples']
        if isinstance(examples, list) == False:
            print ("\n====>: %s" %(examples))
        else:
            for example in examples:
                print ("\n====>: %s" %(example))