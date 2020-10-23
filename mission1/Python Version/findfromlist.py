
#Norman Thien
#Date created: 23/10/2020
#Last Modified: 23/10/2020

#Code used to complete mission 1 of the programming challenge on hackthissite.com
#Essentially recieves input strings in file and tries to unjumble them to one of the words
#in the included dictionary file. Code assumes the jumbled word has unjumbled solution
#in the file.

#exit code 1 should log error to file
#exit code 2 has issues logging error

debug = True #just for testing/debugging in visual studio

dictionary_file = "dictionary.txt"
dictionary_words = []

#Load dictionary words into array from file.
try:
    if debug == True:
        from os.path import dirname, join
        current_dir = dirname(__file__)
        file_path = join(current_dir, dictionary_file)
        file = open(file_path)
    else:
        file = open(dictionary_file)
except:
    try:
        file = open("Error_log.txt", 'a')
        file.write(datetime.datetime.now())
        file.write("Error with opening dictionary file")
        file.close()
    except:
        sys.exit([2])
    sys.exit([1])

#Dictionary file has each word on it's own line
try:
    for x in file:
        dictionary_words.append(x)
except:
    try:
        file = open("Error_log.txt", 'a')
        f.write(datetime.datetime.now())
        f.write("Error with reading from dictionary file")
        f.close()
    except:
        sys.exit([2])
    sys.exit([1])
try:
    file.close()
except:
    try:
        file = open("Error_log.txt", 'a')
        file.write(datetime.datetime.now())
        file.write("Error with closing dictionary file")
        file.close()
    except:
        sys.exit([2])
    sys.exit([1])
