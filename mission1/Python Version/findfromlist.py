
#Norman Thien
#Date created: 23/10/2020
#Last Modified: 24/10/2020

#Code used to complete mission 1 of the programming challenge on hackthissite.com
#Essentially recieves input strings in file and tries to unjumble them to one of the words
#in the included dictionary file. Code assumes the jumbled word has unjumbled solution
#in the file.

#sys.exit code 1 should log error to file
#sys.exit code 2 has issues logging error

#Library imports
import sys
import datetime

#Variables
debug = True #just for testing/debugging in visual studio

dictionary_file = "dictionary.txt"
jumbled_file = "jumbled.txt"
results_file = "results.txt"
dictionary_words = []
jumbled_words = []
temp_words = []

#Functions
#File loading function
def load_file(filename, err_num):
    try:
        if debug == True:
            from os.path import dirname, join
            current_dir = dirname(__file__)
            file_path = join(current_dir, filename)
            file = open(file_path)
            return file
        else:
            file = open(filename)
            return file
    except:
        try:
            error_log(err_num, filename)
        except:
            sys.exit([2])
        sys.exit([1])

#File writing function
def write_file(filename, err_num):
    try:
        if debug == True:
            from os.path import dirname, join
            current_dir = dirname(__file__)
            file_path = join(current_dir, "Error_log.txt")
            file = open(file_path, 'a')
            return file
        else:
            file = open("Error_log.txt", 'a')
            return file
    except:
        error_log(err_num, filename)
    sys.exit([2])

#Error logging code: file related
def error_log(err_num, filename = ""):
    if err_num == -1: #Prevent looping when writing error to log
        sys.exit([2])
    err_msg = {
        1: "Error opening file {}".format(filename),
        2: "Error with reading from {}".format(filename),
        3: "Error with closing {}".format(filename),
        4: "Error writing to file {}".format(filename)
        }
    try:
        file = write_file(filename, -1)
        file.write("{} ".format(datetime.datetime.now()))
        file.write("{}\n".format(err_msg.get(err_num)))
        file.close()
    except:
        sys.exit([2])
    sys.exit([1])

#Main code:

#Load dictionary words into array from file.
file = load_file(dictionary_file, 1)

try:
    for x in file: #Dictionary file has each word on it's own line
        dictionary_words.append(x.rstrip())
except:
    error_log(2, dictionary_file)

try:
    file.close()
except:
    error_log(3, dictionary_file)

#Load jumbled words from file
file = load_file(jumbled_file, 1)

try:
    for x in file:
        jumbled_words.append(x.rstrip())
except:
    error_log(2, jumbled_file)

try:
    file.close
except:
    error_log(3, jumbled_file)

if len(jumbled_words) == 0:
    file = write_file(results_file, 4)
    file.write("No jumbled words inputted")
    file.close()
    sys.exit([0])

enabled = False

if enabled == True: # To be done. This is the algorithm done in C converted to python
    #reduce dictionary words to same length word temp list
    for x in jumbled_words:
        str_len = len(x)
        for y in dictionary_words:
            if len(y) == str_len:
                temp_words.append(y)

    #reduce list further to words holding first char of jumbeld word
    #for x in jumbled_words:


else: # Practice to get more familiar with python workings
    for x in jumbled_words: #jumbled_words string loop
        for y in dictionary_words: #dictionary_words string loop
            found = False
            for i in x: #jumbled_words[x] char loop
                found = False
                for j in y: #dictionary_words[y] loop
                    if j == i:
                        found = True
                        break
                if found == True:
                    continue
                else:
                    break
            if found == True:
                print("{}, Found: {}".format(x,y))
                break
print("end")