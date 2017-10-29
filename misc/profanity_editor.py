from  urllib import request
from urllib import parse


def check_whole_stream(text_to_check,url_to_use):
    connection = request.urlopen(url_to_use + parse.urlencode([('q', text_to_check)]))
    response = connection.read()
    if b"true" in response:
        print("Alert!!!! Bad words, bad time!")
    else:
        print("No problem.")
    connection.close()

def check_each_word(text_to_check,url_to_use):
    for word in text_to_check.split():
        connection = request.urlopen(url_to_use + word)
        response = connection.read()
        if b"true" in response:
            print("Alert!!!! Bad words, bad time!")
        else:
            print("No problem.")
        connection.close()


#try to pen the file and read
try:
    file_to_parse = open("potentially_problemeatic.txt")
except:
    print("cannot find the file to open")
    quit()



text_to_check = file_to_parse.read()
file_to_parse.close()

# send check word by sending as a query parameter to an online service
url_to_use = "http://www.wdylike.appspot.com/?q="
check_whole_stream(text_to_check,url_to_use)




